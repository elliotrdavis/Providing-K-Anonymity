"""
LatticeGeneration.py
Author: Elliot Davis

This file generates the generalization lattices (nodes and edges)

"""

from functools import reduce
from itertools import product


# Returns list of all nodes in the lattice
def generateLatticeNodes(attributeDimensions, allCandidateNodes):

    depth = []  # Depth is for each attributes generalization depth e.g (0, 1) for Name
    dimensionNameList = []  # For list of attribute names (e.g. Name, Sex, Address)
    for dimensions in attributeDimensions:  # dimensions is list of each possible dimension e.g. [[Name, 0],[Name, 1]]
        dimensionNameList.append(dimensions[0][0])
        dimArray = []  # will temporarily hold all dim numbers for each attribute
        for dim in dimensions:  # For each individual dimension e.g. [Name,0]
            dimArray.append(str(dim[1]))
        depth.insert(0,tuple(dimArray))  # Adds dimension depth number for each attribute

    dimensionNameList = tuple(dimensionNameList)
    # attributeCombinations generates a list of all combinations of node depths in order (will allow easier
    # computation for Samariti's algorithm)
    attributeCombinations = list(reduce(lambda a, b: [(p[1], *p[0]) for p in product(a, b)], depth))

    candidateNodes = []
    for node in attributeCombinations:  # for each node in lattice
        newNode = []
        for index in range(len(node)):  # for each index in the node
            # Generates list with respective attribute name and depth next to each other
            newNode.append(dimensionNameList[index])
            newNode.append(node[index])
        candidateNodes.append(newNode)  # Adds all possible nodes to one list
    allCandidateNodes.append(candidateNodes)  # Add to second list (used for incognito algorithm, not samariti)

    return allCandidateNodes


# Returns list of all edges in lattice
def generateLatticeEdges(candidateTableList):
    edgesList = []

    for candidateTable in candidateTableList:  # for each node create its edges
        edges = []
        for node in candidateTable:  # iterates through all the nodes in candidateTable
            for index in range(1,len(node),2):  # iterates through all the possible next node ids
                nextNode = int(node[index]) + 1
                length = []
                for i in range(1,len(node),2):
                    length.append(i)
                length.remove(index)  # remove current node from list
                for nodeCheck in range(candidateTable.index(node) + 1, len(candidateTable)):
                    # if another node matches with nextNode then add to edge
                    # check against current nodes
                    total = 0
                    for i in length:
                        if candidateTable[nodeCheck][i] == node[i]:
                            total += 1
                    if candidateTable[nodeCheck][index] == str(nextNode) and total == len(length):
                        edges.append((candidateTable.index(node) + 1, nodeCheck + 1))
                        break

        edges = list(set([i for i in edges]))  # Removes duplicates
        edges = sorted(edges, key=lambda element: (element[0], element[1]))  # Sorts list
        edgesList.append(edges)

    return edgesList
