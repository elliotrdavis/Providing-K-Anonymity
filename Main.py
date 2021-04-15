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

"""
Binary search for this list:
two concurrent lists: 
- one with height of each node in C
- one with data (C)

for each search:
    calculate kValue for each node on that height
    if found:
        binary search lower
    else: 
        binary search higher level


"""


def samarati():
    C = []
    C = generateLatticeNodes(quasiIdentifiers, C)
    heightArray = []
    for node in C[0]:
        height = 0
        for index in range(1, len(node), 2):  # iterates through all the possible next node ids
            height += int(node[index])
        heightArray.append(height)
    heightList = list(set([i for i in heightArray]))

    low = heightList[0]
    high = heightList[-1]
    while low <= high:
        tryNode = round((low+high)/2)
        toSearch = []
        found = False

        for i in range(len(heightArray)):
            if heightArray[i] == tryNode:
                toSearch.append(i)
                dimDataframe = updateDataframe(C[0][i])
                kValue = frequencySet(dimDataframe)

                if kValue >= kanonymity:
                    found = True
                    break

        if found:
            high = tryNode - 1

        else:
            low = tryNode + 1

    print(dimDataframe)
    print(kValue)
    print("--- %s seconds ---" % (time.time() - start_time))


def incognito():
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

                    # If it matches, add it to visited queue and visited
                    visitedQueue = [i.index(S[0])]
                    visited.append(S[0])
                    S.pop(0)

                    #  visited queue = searching through the parent nodes
                    while visitedQueue:
                        index = visitedQueue[0]
                        visitedQueue.pop(0)

                        for edge in SE:
                            if edge[0] == index and i[edge[1] - 1] not in visited:
                                visited.append(i[edge[1] - 1])
                                visitedQueue.append(i.index(i[edge[1] - 1]) + 1)

                    if len(S) > 0:
                        queue.append(S[0])

                else:
                    # if kvalue false then search through rest of lattice by height, removing edges along the way
                    index = i.index(S[0]) + 1
                    SE[:] = [edge for edge in SE if index != edge[0]]
                    S.pop(0)
                    if len(S) > 0:
                        queue.append(S[0])

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
        kValue = frequencySet(dimDataframe)

        # if kValue >= kanonymity:
        print(node)
        print(dimDataframe)
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
    kanonymity = 2

    # incognito()
    samarati()
