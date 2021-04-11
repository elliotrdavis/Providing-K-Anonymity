from ColumnConversion import convertColumns, dimDFConversionIncognito
from LatticeGeneration import candidateNodeTableIncognito, generateEdgesIncognito, candidateNodeTable

"""
TODO:
Optimise column generation
Incognito not marking all nodes if kvalue true
generate edges in pruned genLattice ?


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
    C = candidateNodeTable()
    convertColumns()

    for node in C:
        dimDataframe = dimDFConversionIncognito(node)  # returns dimDataframe
        kValue = frequencySet(dimDataframe)

        if kValue >= kanonymity:
            print(dimDataframe)
            print(kValue)
            break


def incognito(kanonymity):
    C = candidateNodeTableIncognito()
    E = generateEdgesIncognito(C)

    convertColumns()
    queue = []
    SList = []

    # C1 = candidateNodeTable()
    # for node in C1:
    #     dimDataframe = dimDFConversionIncognito(node)  # returns dimDataframe
    #     kValue = frequencySet(dimDataframe)  # returns KValue
    #     if kValue >= 2:
    #         print(kValue)
    #         print(dimDataframe)

    for i, j in zip(C, E):

        # i is the nodes of the original lattice, j is the edges of the original lattice
        S = i[:]  # nodes of current lattice
        SE = j[:]  # edges of current lattice
        roots = [S[0]]
        # print(S[0])
        # print(roots)
        # queue.append(roots)
        queue.append(S[0])
        # print(queue)
        visited = []

        while queue:
            node = queue[0]
            queue.pop(0)
            # print(S)

            if node not in visited:

                if node in roots:
                    # print(node[0])
                    dimDataframe = dimDFConversionIncognito(node)  # returns dimDataframe
                    # print(dimDataframe)
                    kValue = frequencySet(dimDataframe)  # returns KValue
                    # print(kValue)
                    # Compute frequency set by replacing values in i in original table
                else:
                    # print(node[0])
                    dimDataframe = dimDFConversionIncognito(node)  # returns dimDataframe
                    kValue = frequencySet(dimDataframe)  # returns KValue
                    # print(dimDataframe)
                    # print(kValue)
                    # Compute frequency set by replacing values in i parent frequency

                if kValue >= kanonymity:
                    # print(kValue)
                    # if match then mark all direct generalizations by adding to visited
                    # print(S)
                    # print(SE)
                    # print(i)
                    index = i.index(S[0]) + 1
                    # print("index")
                    # print(index)
                    visited.append(i[index-1])
                    # print(i[index-1])
                    for edge in SE:
                        if edge[0] == index:
                            # print(i[edge[1]-1])
                            visited.append(i[edge[1]-1])
                    # frequencySet1 = 0
                else:
                    # if kvalue false then search through rest of lattice by height, removing edges along the way
                    index = i.index(S[0]) + 1
                    SE[:] = [edge for edge in SE if index != edge[0]]
                    S.pop(0)
                    if len(S) > 0:
                        queue.append(S[0])
                        # print(queue)
                        # print(S[0])
                    else:
                        print("queue is empty")
        # print(S)
        # print(SE)
        SList.append(visited)
    graphGen(SList)
    # Graph generation here


def graphGen(nodes):
    # joining phase
    genLattice = []
    for firstNode in nodes[0]:
        genLattice.append(firstNode)

    nodes.pop(0)
    for node in nodes[:-1]:
        for gen in node:
            # print("Gen: " + str(gen))
            for lat in genLattice:

                if lat[-1] == gen[1] and lat[-2] == gen[0]:
                    lat.append(gen[2])
                    lat.append(gen[3])
                # if lat[-1] != gen[1] and lat[-2] == gen[0]:
                #     print("hello")
                #     lat[-1] = gen[1]
                #     genLattice.append(lat)
                if lat[-4] == gen[0] and lat[-3] == gen[1] and lat[-2] == gen[2] and lat[-1] != gen[3]:
                    # lat[-1] = gen[3]
                    newLat = lat[:]
                    newLat[-1] = gen[3]
                    genLattice.append(newLat)
                # print("lat: " + str(lat))

            # .append(gen)
        # print(node)
    # print("Gen Lattice")
    # print(genLattice)
    for node in genLattice:
        dimDataframe = dimDFConversionIncognito(node)  # returns dimDataframe
        print(dimDataframe)
        kValue = frequencySet(dimDataframe)  # returns KValue
        print(kValue)


"""
[['Name', '1', 'Sex', '0'], # wrong ['Name', '0', 'Sex', '1'], ['Name', '1', 'Sex', '1']]
[['Sex', '0', 'Address', '1'], ['Sex', '1', 'Address', '1']]
[['Address', '1', 'Age', '2']]
[['Age', '2', 'Postcode', '1'], # wrong['Age', '0', 'Postcode', '2'], #wrong ['Age', '1', 'Postcode', '2'],
 ['Age', '2', 'Postcode', '2']]

Generate these nodes
Name 1, Sex 0, Address 1, Age 2, Postcode 1, //Name 1
Name 0, Sex 1, Address 1, Age 2, Postcode 1, //Name 1
Name 1, Sex 1, Address 1, Age 2, Postcode 1, //Name 1
Name 1, Sex 0, Address 1, Age 2, Postcode 2, //Name 0/1
Name 0, Sex 1, Address 1, Age 2, Postcode 2, //Name 0/1
Name 1, Sex 1, Address 1, Age 2, Postcode 2, //Name 0/1

Then generate edges..
if node where 1 attribute is 1 above then connect

Then double check if k value is correct
"""


def frequencySet(dataframe):
    # print(dataframe)
    # print(dataframe.columns)
    KValue = dataframe.groupby(list(dataframe.columns)).size().reset_index(name='Count')
    # print("K-Value = ", KValue['Count'].min())
    # print(KValue)
    KValue = KValue['Count'].min()
    # print(KValue)
    return KValue


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # incognito(2)
    samarati(2)
