"""
Main.py
Author: Elliot Davis

This file implements the Incognito algorithm and the Samariti algorithm, it also contains a function to calculate the
k value of a given data set

"""
import copy
from ColumnConversion import createTempDataframe, updateDataframe
from LatticeGeneration import generateLatticeNodes, generateLatticeEdges
import time
from KValue import readHeader


def samarati():
    solution = None
    heightArray = []

    nodes = []
    nodes = generateLatticeNodes(quasiIdentifiers, nodes)

    for node in nodes[0]:
        height = 0
        for index in range(1, len(node), 2):
            height += int(node[index])
        heightArray.append(height)
    heightSet = list(set([i for i in heightArray]))

    low = heightSet[0]
    high = heightSet[-1]
    while low < high:
        mid = round((low+high)/2)
        found = False

        for i in range(len(heightArray)):
            if heightArray[i] == mid:
                dimDataframe = updateDataframe(nodes[0][i], suppress, numeric, shorten, n2, n3)
                kValue = calculateK(dimDataframe)

                if kValue == kanonymity:
                    print(nodes[0][i])
                    solution = copy.deepcopy(dimDataframe)
                    solutionKValue = kValue
                    found = True
                    break

        if found:
            high = mid - 1

        else:
            low = mid + 1

    if solution is not None:
        print(solution)
        print(solutionKValue)
    else:
        print("no solution found")
    print("--- %s seconds ---" % (time.time() - start_time))


def incognito():
    queue = []
    fullDomainList = []  # List for all nodes which meet requirements

    nodes = []
    # generateLatticeNodes(quasiIdentifiers, nodes)
    # E = generateLatticeEdges(nodes)
    for columnNames in incognitoAttributeList:  # Generates list of all potential nodes
        nodes = generateLatticeNodes(columnNames, nodes)
    E = generateLatticeEdges(nodes)

    for i, j in zip(nodes, E):
        # i is the nodes of the original lattice, j is the edges of the original lattice
        S = i[:]  # nodes of current lattice
        SE = j[:]  # edges of current lattice
        queue.append(S[0])
        visited = []

        while queue:
            node = queue[0]
            queue.pop(0)

            if node not in visited:
                dimDataframe = createTempDataframe(node, suppress, numeric, shorten, n2, n3)  # returns dimDataframe
                kValue = calculateK(dimDataframe)  # returns KValue
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
    seen = set()
    for firstNode in nodeList[0]:  # Adds first set of nodes to list
        genLattice.append(firstNode)
    nodeList.pop(0)

    for nodes in nodeList[:-1]:  # For all the other nodes
        for node in nodes:  # For each node
            for lat in genLattice:  # For each item in current list (lat) check the following
                if lat[-1] == node[1] and lat[-2] == node[0]:  # Check if matching nodes have matching dimensions
                    lat.append(node[2])
                    lat.append(node[3])
                    t = tuple(lat)
                    if t not in seen:
                        genLattice.append(lat)
                        seen.add(t)
                # Check if names are matching but numbers are different, create new node if so
                elif lat[-4] == node[0] and lat[-3] == node[1] and lat[-2] == node[2] and lat[-1] != node[3]:
                    newLat = lat[:]
                    newLat[-1] = node[3]
                    t = tuple(newLat)
                    if t not in seen:
                        genLattice.append(newLat)
                        seen.add(t)

    count = 0
    # Print all full domain generalisations
    if len(genLattice) >= 1:
        for node in genLattice:
            dimDataframe = updateDataframe(node, suppress, numeric, shorten, n2, n3)
            kValue = calculateK(dimDataframe)

            if kValue == kanonymity:
                count = count + 1
                print(node)
                # print(dimDataframe)
                print("kValue", kValue)
    else:
        print("no solution found")

    print("--- %s seconds ---" % (time.time() - start_time))


def simpleSearch():
    C = []
    C = generateLatticeNodes(quasiIdentifiers, C)

    for node in C[0]:  # For each potential node in lattice
        # Node are ordered by height
        dimDataframe = updateDataframe(node, suppress, numeric, shorten, n2, n3)
        kValue = calculateK(dimDataframe)
        if kValue == kanonymity:  # If a node meets requirements, print and break
            print(dimDataframe)
            print(kValue)
            print("--- %s seconds ---" % (time.time() - start_time))
            break


# Returns k-value (how secure the dataset is)
def calculateK(dataframe):
    KValue = dataframe.groupby(list(dataframe.columns)).size().reset_index(name='Count')
    KValue = KValue['Count'].min()
    return KValue


if __name__ == '__main__':
    lines = readHeader()
    suppress = []
    numeric = []
    shorten = []
    n2 = []
    n3 = []
    quasiIdentifiers = []
    incognitoAttributeList = []
    for line in lines:
        line = line.split()
        if line[1][0] == "{":
            suppress.append(line[0])
            supList = [[line[0], 0],[line[0], 1]]
            quasiIdentifiers.append(supList)
        if line[1] == "NUMERIC":
            numeric.append(line[0])
            numList = [[line[0], 0], [line[0], 1], [line[0], 2], [line[0], 3], [line[0], 4], [line[0], 5]]
            quasiIdentifiers.append(numList)
        if line[1] == "SHORTEN":
            shorten.append(line[0])
            shortList = [[line[0], 0], [line[0], 1], [line[0], 2]]
            quasiIdentifiers.append(shortList)
        if line[1] == "N2":
            n2.append(line[0])
            n2List = [[line[0], 0], [line[0], 1], [line[0], 2], [line[0], 3], [line[0], 4], [line[0], 5]]
            quasiIdentifiers.append(n2List)
        if line[1] == "N3":
            n3.append(line[0])
            n3List = [[line[0], 0], [line[0], 1], [line[0], 2]]
            quasiIdentifiers.append(n3List)

    for i in range(0, len(quasiIdentifiers)):
        if i == len(quasiIdentifiers)-1:
            quasiPairs = [quasiIdentifiers[i], quasiIdentifiers[0]]
        else:
            quasiPairs = [quasiIdentifiers[i], quasiIdentifiers[i + 1]]
        incognitoAttributeList.append(quasiPairs)

    for i in range(3,4):
        start_time = time.time()
        kanonymity = i
        print(kanonymity)
        # incognito()
        # samarati()
        simpleSearch()
