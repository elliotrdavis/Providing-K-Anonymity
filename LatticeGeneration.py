"""
LatticeGeneration.py
Author: Elliot Davis

This file is responsible for

"""

from functools import reduce
from itertools import product
import numpy as np


# Return set of generalization lattice's
def candidateNodeTableIncognito():
    name = [["Name", 0], ["Name", 1]]
    sex = [["Sex", 0], ["Sex", 1]]
    address = [["Address", 0], ["Address", 1]]
    age = [["Age", 0], ["Age", 1], ["Age", 2]]
    postcode = [["Postcode", 0], ["Postcode", 1], ["Postcode", 2]]

    # What are all possible generalization graphs?
    # name - sex, address, age, postcode
    # sex - address, age, postcode
    # address - age, postcode
    # age - postcode
    # put smaller attributes first for nicer table
    twoAttributeList = [[name, sex],[sex,address],[address,age],[age,postcode],[postcode, name]]
    # add what quasi identifiers here
    allCandidateConnection = []

    for twoAttribute in twoAttributeList:
        comp = []
        dimensions = []
        for lists in twoAttribute:
            dimensions.append(lists[0][0])
            temp = []
            for var in lists:
                temp.append(str(var[1]))
            comp.insert(0,tuple(temp))
        dimensions = tuple(dimensions)

        candidateConnections = list(reduce(lambda a, b: [(p[1], *p[0]) for p in product(a, b)], comp))

        # turn this into df
        # [('0', '0'), ('1', '0'), ('0', '1'), ('1', '1'), ('0', '2'), ('1', '2')]
        newCandidateConnections = []
        # dimensions = ('Name', 'Sex', 'Address', 'Age', 'Postcode')
        for tuple1 in candidateConnections:  # for each tuple in above list
            newTuple = []
            for index in range(len(tuple1)):  # for each index in the tuple
                newTuple.append(dimensions[index])
                newTuple.append(tuple1[index])
            newCandidateConnections.append(newTuple)
        allCandidateConnection.append(newCandidateConnections)

    return allCandidateConnection


def generateEdgesIncognito(candidate):
    candidateTableList = candidate
    edgesList = []
    # for each node create its edges
    for candidateTable in candidateTableList:
        edges = []
        for node in candidateTable:  # iterates through all the nodes in candidateTable
            for index in range(1,len(node),2):  # iterates through all the possible next node ids
                nextNode = int(node[index]) + 1
                length = []
                for i in range(1,len(node),2):
                    length.append(i)
                # length = [1,3,5]
                length.remove(index)
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

        edges = removeDuplicates(edges)
        edges = sorted(edges, key=lambda element: (element[0], element[1]))
        edgesList.append(edges)

        root1 = []
        root2 = []
        for i in edges:
            root1.append(i[0])
            root2.append(i[1])
        generateEdges.roots = np.setdiff1d(root1, root2)

    return edgesList


def candidateNodeTable():  # Generates and returns candidate node table
    name = [["Name", 0], ["Name", 1]]
    sex = [["Sex", 0], ["Sex", 1]]
    address = [["Address", 0], ["Address", 1]]
    age = [["Age", 0], ["Age", 1], ["Age", 2]]
    postcode = [["Postcode", 0], ["Postcode", 1], ["Postcode", 2]]

    # What are all possible generalization graphs?
    # name - sex, address, age, postcode
    # sex - address, age, postcode
    # address - age, postcode
    # age - postcode
    # put smaller attributes first for nicer table
    quasiIdentifiers = [name, sex, address, age, postcode]  # add what quasi identifiers here

    comp = []
    dimensions = []
    for lists in quasiIdentifiers:
        dimensions.append(lists[0][0])
        temp = []
        for var in lists:
            temp.append(str(var[1]))
        comp.insert(0,tuple(temp))
    dimensions = tuple(dimensions)

    candidateConnections = list(reduce(lambda a, b: [(p[1], *p[0]) for p in product(a, b)], comp))

    # turn this into df
    # [('0', '0'), ('1', '0'), ('0', '1'), ('1', '1'), ('0', '2'), ('1', '2')]
    newCandidateConnections = []
    # dimensions = ('Name', 'Sex', 'Address', 'Age', 'Postcode')
    for tuple1 in candidateConnections:  # for each tuple in above list
        newTuple = []
        for index in range(len(tuple1)):  # for each index in the tuple
            newTuple.append(dimensions[index])
            newTuple.append(tuple1[index])
        newCandidateConnections.append(newTuple)

    return newCandidateConnections


def generateEdges():
    candidateTable = candidateNodeTable()
    # to do
    # Subset property: let T be a relation, and let Q be a set of attributes in T.
    # If T is k-anonymous with respect to Q, then T is k-anonymous with respect to any set of
    # attributes P such that P < Q
    # print(candidateNodeTable.newCandidateConnections)
    # generate edges
    # edges are tuples, create list of tuples and append

    edges = []
    # for each node create its edges
    for node in candidateTable:  # iterates through all the nodes in candidateTable
        for index in range(1,len(node),2):  # iterates through all the possible next node ids
            nextNode = int(node[index]) + 1
            length = []
            for i in range(1,len(node),2):
                length.append(i)
            # length = [1,3,5]
            length.remove(index)
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

    edges = removeDuplicates(edges)
    edges = sorted(edges, key=lambda element: (element[0], element[1]))

    root1 = []
    root2 = []
    for i in edges:
        root1.append(i[0])
        root2.append(i[1])
    generateEdges.roots = np.setdiff1d(root1, root2)

    # list i need: (1,2) (1,3) (2,4) (3,4) (3,5) (4,6) (5,6)
    return edges


def removeDuplicates(edges):
    return list(set([i for i in edges]))
