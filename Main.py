"""
Main.py
Author: Elliot Davis

This file implements the Incognito algorithm and the Samariti algorithm, it contains a function to calculate the
k value of a given data set

"""

from ColumnConversion import createTempDataframe, updateDataframe
from LatticeGeneration import generateLatticeNodes, generateLatticeEdges
import time

"""
TODO:
Incognito not marking all nodes if kvalue true - not necessary
generate edges in pruned genLattice - not necessary


Columns: 'Name','Age','Sex','Address','Party','Postcode'
Dimension table: current requirements
Name: P0 (name), P1 (-)
Age: P0 (original), P1 (5 age range), P2 (10 age range), P3 (20 age range)
Sex: P0 (male/female), P1 (-)
Address: P0 (address), P1 (-)
Party: P0 (important info)
Postcode: P0 (original), P1 (First 3 letters), P2 (First 2 Letters)
"""


def samarati(kanonymity):
    C = []
    C = generateLatticeNodes(quasiIdentifiers,C)
    E = generateLatticeEdges(C)

    for node in C[0]:  # For each potential node in lattice
        # Node are ordered by height
        dimDataframe = updateDataframe(node)
        kValue = frequencySet(dimDataframe)

        if kValue >= kanonymity:  # If a node meets requirements, print and break
            print(dimDataframe)
            print(kValue)
            print("--- %s seconds ---" % (time.time() - start_time))
            break


def incognito(kanonymity):
    C = []
    for columnNames in incognitoAttributeList:  # Generates list of all potential nodes
        C = generateLatticeNodes(columnNames, C)
    E = generateLatticeEdges(C)

    queue = []
    fullDomainList = []  # List for all nodes which meet requirements

    for i, j in zip(C, E):
        # i is the nodes of the original lattice, j is the edges of the original lattice
        S = i[:]  # nodes of current lattice
        SE = j[:]  # edges of current lattice
        queue.append(S[0])
        visited = []

        while queue:
            node = queue[0]
            queue.pop(0)

            if node not in visited:
                dimDataframe = createTempDataframe(node)  # returns dimDataframe
                kValue = frequencySet(dimDataframe)  # returns KValue
                # Compute frequency set by replacing values in i in original table

                if kValue >= kanonymity:
                    # if meets kanonymity requirement then add direct generalizations to visited
                    visitedQueue = [i.index(S[0]) + 1]
                    visited.append(i[index - 1])
                    while visitedQueue:
                        index = visitedQueue[0]
                        visitedQueue.pop(0)

                        for edge in SE:
                            if edge[0] == index:
                                visited.append(i[edge[1]-1])
                                visitedQueue.append(i.index(i[edge[1]-1]) + 1)
                    print(visited)
                else:
                    # if kvalue false then search through rest of lattice by height, removing edges along the way
                    index = i.index(S[0]) + 1
                    SE[:] = [edge for edge in SE if index != edge[0]]
                    S.pop(0)
                    if len(S) > 0:
                        queue.append(S[0])
                    else:
                        print("queue is empty")
        fullDomainList.append(visited)
    graphGen(fullDomainList)


# Generates all potential full domain generalizations which meet kanonymity requirement
def graphGen(nodeList):
    genLattice = []
    for firstNode in nodeList[0]:  # Adds first set of nodes to list
        genLattice.append(firstNode)
    nodeList.pop(0)

    for nodes in nodeList[:-1]:  # For all the other nodes
        for node in nodes:  # For each node
            for lat in genLattice:  # For each item in current list (lat) check the following
                if lat[-1] == node[1] and lat[-2] == node[0]:  # Check if matching nodes have matching dimensions
                    lat.append(node[2])
                    lat.append(node[3])
                # Check if names are matching but numbers are different, create new node if so
                if lat[-4] == node[0] and lat[-3] == node[1] and lat[-2] == node[2] and lat[-1] != node[3]:
                    newLat = lat[:]
                    newLat[-1] = node[3]
                    genLattice.append(newLat)

    # Print all full domain generalisations
    for node in genLattice:
        dimDataframe = updateDataframe(node)
        print(dimDataframe)
        kValue = frequencySet(dimDataframe)
        print(kValue)
    print("--- %s seconds ---" % (time.time() - start_time))


# Returns k-value (how secure the dataset is)
def frequencySet(dataframe):
    KValue = dataframe.groupby(list(dataframe.columns)).size().reset_index(name='Count')
    KValue = KValue['Count'].min()
    return KValue


if __name__ == '__main__':
    start_time = time.time()

    name = [["Name", 0], ["Name", 1]]
    sex = [["Sex", 0], ["Sex", 1]]
    address = [["Address", 0], ["Address", 1]]
    age = [["Age", 0], ["Age", 1], ["Age", 2]]
    postcode = [["Postcode", 0], ["Postcode", 1], ["Postcode", 2]]

    incognitoAttributeList = [[name, sex], [sex, address], [address, age], [age, postcode], [postcode, name]]
    quasiIdentifiers = [name, sex, address, age, postcode]

    incognito(2)
    # samarati(2)

    # if node in roots:
    #     dimDataframe = createTempDataframe(node)  # returns dimDataframe
    #     kValue = frequencySet(dimDataframe)  # returns KValue
    #     # Compute frequency set by replacing values in i in original table
    # else:
    #     dimDataframe = createTempDataframe(node)  # returns dimDataframe
    #     kValue = frequencySet(dimDataframe)  # returns KValue
    #     # Compute frequency set by replacing values in i parent frequency
