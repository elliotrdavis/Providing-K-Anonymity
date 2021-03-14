# Create dimension tables

import pandas as pd
import pymysql
from functools import reduce
from itertools import product
import numpy as np

from sqlalchemy import create_engine

from KValue import VoterListDF, VoterListColumns

host = 'localhost'
user = 'root'
password = 'root'
database = 'dimindex'


def candidateNodeTable():  # Generates and returns candidate node table
    # connection = pymysql.connect(host=host, user=user, password=password, database=database)
    #
    # my_cursor = connection.cursor()
    #
    # # Execute Query
    # my_cursor.execute("SELECT * from sex")
    #
    # # Fetch the records
    # sex = my_cursor.fetchall()
    #
    # my_cursor.execute("SELECT * from postcode")
    # postcode = my_cursor.fetchall()

    name = [["Name", 0], ["Name", 1]]
    sex = [["Sex", 0], ["Sex", 1]]
    address = [["Address", 0], ["Address", 1]]
    age = [["Age", 0], ["Age", 1], ["Age", 2]]
    postcode = [["Postcode", 0], ["Postcode", 1], ["Postcode", 2]]

    quasiIdentifiers = [name, sex, address, age, postcode]  # add what quasi identifiers here
    # put smaller attributes first for nicer table

    # nameList = ['0', '1']
    # sexList = ['0', '1']
    # addressList = ['0', '1']
    # ageList = ['0', '1', '2']
    # postcodeList = ['0', '1', '2']

    # for i in sex:  # for 2 attribute lists
    #     # print(i[2])
    #     nameList.append(str(i[1]))
    #     sexList.append(str(i[1]))
    #     addressList.append(str(i[1]))
    #
    # for i in postcode:  # for 3 attribute lists
    #     # print(j[2])
    #     ageList.append(str(i[1]))
    #     postcodeList.append(str(i[1]))
    comp = []
    dimensions = []
    for lists in quasiIdentifiers:
        dimensions.append(lists[0][0])
        temp = []
        for var in lists:
            temp.append(str(var[1]))
        comp.insert(0,tuple(temp))
    dimensions = tuple(dimensions)

    # print(comp, dimensions)
    # comp = [tuple(postcodeList), tuple(ageList), tuple(addressList), tuple(sexList), tuple(nameList)]
    candidateConnections = list(reduce(lambda a, b: [(p[1], *p[0]) for p in product(a, b)], comp))
    # print(candidateConnections)
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
    # print(newCandidateConnections)
    # add to dataframe
    #candidateColumns = ['dim1', 'index1', 'dim2', 'index2', 'dim3', 'index3', 'dim4', 'index4', 'dim5', 'index5']
    candidateConnectionsDF = pd.DataFrame(newCandidateConnections)
    # print(candidateConnectionsDF)
    # upload to sql server
    engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                           .format(user=user,
                                   pw=password,
                                   db=database))
    candidateConnectionsDF.to_sql('candidate', con=engine, if_exists='replace', chunksize=1000)
    # print(candidateConnectionsDF)
    # comp = [('0', '1', '2'), ('0', '1'), ('0', '1',)]
    # print(list(reduce(lambda a, b: [(p[1], *p[0]) for p in product(a, b)], comp)))
    # connection.close()
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
    for node in candidateTable: # iterates through all the nodes in candidateTable
        #print(node)
        for index in range(1,len(node),2): # iterates through all the possible next node ids
            nextNode = int(node[index]) + 1
            #print("index, node:", index, nextNode)
            length = []
            for i in range(1,len(node),2):
                # print(i)
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
                #print("nodecheck", candidateTable[nodeCheck])
                if candidateTable[nodeCheck][index] == str(nextNode) and total == len(length):
                    #print("matching node", candidateTable[nodeCheck])
                    edges.append((candidateTable.index(node) + 1, nodeCheck + 1))
                    break
    # for node in candidateTable:  # go through every node in candidate nodes
    #     # print('from:', node)
    #     # go through each index, check if legal then add to edge list
    #     for index in range(1, len(node), 2):  # go through every index in each node
    #         # print(node[index])
    #         nextNode = int(node[index]) + 1
    #         # print(nextNode)
    #         for node2 in range(candidateTable.index(node) + 1,
    #                            len(candidateTable)):
    #             # iterate through every other node, check for match
    #             # print('search through for',node[index], candidateNodeTable.newCandidateConnections[node2])
    #             nextNodeSex = int(node[1]) + 1
    #             if (candidateTable[node2][1] == str(nextNodeSex) and
    #                     candidateTable[node2][3] == node[3]):
    #                 # print('to', candidateNodeTable.newCandidateConnections[node2])
    #                 edges.append((candidateTable.index(node) + 1, node2 + 1))
    #
    #             nextNodePostcode = int(node[3]) + 1
    #             if (candidateTable[node2][3] == str(nextNodePostcode) and
    #                     candidateTable[node2][1] == node[1]):
    #                 # print('to', candidateNodeTable.newCandidateConnections[node2])
    #                 edges.append((candidateTable.index(node) + 1, node2 + 1))

    # print('original list', edges)
    edges = removeDuplicates(edges)
    # print('remove dupes', edges)
    edges = sorted(edges, key=lambda element: (element[0], element[1]))
    #print('sorted', edges)

    root1 = []
    root2 = []
    for i in edges:
        root1.append(i[0])
        root2.append(i[1])
    generateEdges.roots = np.setdiff1d(root1, root2)
    # print(roots)
    # list i need: (1,2) (1,3) (2,4) (3,4) (3,5) (4,6) (5,6)
    return edges


def removeDuplicates(edges):
    return list(set([i for i in edges]))


def indexTables():  # creates index tables for dimension tables
    partyDim = [["Party", 0]]
    nameDim = [["Name", 0], ["Name", 1]]
    sexDim = [["Sex", 0], ["Sex", 1]]
    addressDim = [["Address", 0], ["Address", 1]]
    ageDim = [["Age", 0], ["Age", 1], ["Age", 2]]
    postcodeDim = [["Postcode", 0], ["Postcode", 1], ["Postcode", 2]]

    dimColumns = ['dim', 'index']

    indexTables.partyDimDF = pd.DataFrame(data=partyDim, columns=dimColumns)
    indexTables.nameDimDF = pd.DataFrame(data=nameDim, columns=dimColumns)
    indexTables.sexDimDF = pd.DataFrame(data=sexDim, columns=dimColumns)
    indexTables.addressDimDF = pd.DataFrame(data=addressDim, columns=dimColumns)
    indexTables.ageDimDF = pd.DataFrame(data=ageDim, columns=dimColumns)
    indexTables.postcodeDimDF = pd.DataFrame(data=postcodeDim, columns=dimColumns)


# def party(column):
#     partyDFList = []
#     party0 = []
#     for item in VoterListDF[column]:  # for each item in column
#         party0.append(item)
#     p0 = {'Party': party0}
#     partyDF0 = pd.DataFrame(data=p0)
#     partyDFList.append(partyDF0)
#     return partyDFList


def name(column):
    nameDFList = []
    name0 = []
    name1 = []
    for item in VoterListDF[column]:
        name0.append(item)
        item = '-'
        name1.append(item)
    n0 = {'Name': name0}
    n1 = {'Name': name1}
    nameDF0 = pd.DataFrame(data=n0)
    nameDF1 = pd.DataFrame(data=n1)
    nameDFList.append(nameDF0)
    nameDFList.append(nameDF1)
    return nameDFList


def sex(column):
    sexDFList = []
    sex0 = []
    sex1 = []
    for item in VoterListDF[column]:
        sex0.append(item)
        item = '-'
        sex1.append(item)
    s0 = {'Sex': sex0}
    s1 = {'Sex': sex1}
    sexDF0 = pd.DataFrame(data=s0)
    sexDF1 = pd.DataFrame(data=s1)
    sexDFList.append(sexDF0)
    sexDFList.append(sexDF1)
    return sexDFList


def address(column):
    addressDFList = []
    address0 = []
    address1 = []
    for item in VoterListDF[column]:
        address0.append(item)
        item = '-'
        address1.append(item)
    a0 = {'Address': address0}
    a1 = {'Address': address1}
    addressDF0 = pd.DataFrame(data=a0)
    addressDF1 = pd.DataFrame(data=a1)
    addressDFList.append(addressDF0)
    addressDFList.append(addressDF1)
    return addressDFList


def age(column):
    ageDFList = []
    age0 = []
    age1 = []
    age2 = []
    for item in VoterListDF[column]:
        age0.append(item)
        if 0 <= item <= 5:
            ageRange = '0<=x<=5'
        if 5 < item <= 10:
            ageRange = '5<x<=10'
        if 10 < item <= 15:
            ageRange = '10<x<=15'
        if 15 < item <= 20:
            ageRange = '15<x<=20'
        if 20 < item <= 25:
            ageRange = '20<x<=25'
        if 25 < int(item) <= 30:
            ageRange = "25<x<=30"
        if 30 < int(item) <= 35:
            ageRange = "30<x<=35"
        if 35 < int(item) <= 40:
            ageRange = '35<x<=40'
        age1.append(ageRange)

        if ageRange == '0<=x<=5' or ageRange == '5<x<=10':
            ageRange = '0<=x<=10'
        if ageRange == '10<x<=15' or ageRange == '15<x<=20':
            ageRange = '10<x<=20'
        if ageRange == '20<x<=25' or ageRange == '25<x<=30':
            ageRange = '20<x<=30'
        if ageRange == '30<x<=35' or ageRange == '35<x<=40':
            ageRange = '30<x<=40'
        age2.append(ageRange)

    ag0 = {'Age': age0}
    ag1 = {'Age': age1}
    ag2 = {'Age': age2}
    ageDF0 = pd.DataFrame(data=ag0)
    ageDF1 = pd.DataFrame(data=ag1)
    ageDF2 = pd.DataFrame(data=ag2)
    ageDFList.append(ageDF0)
    ageDFList.append(ageDF1)
    ageDFList.append(ageDF2)
    return ageDFList


def postcode(column):
    postcodeDFList = []
    postcode0 = []
    postcode1 = []
    postcode2 = []
    for item in VoterListDF[column]:
        postcode0.append(item)
        postcode1.append(item[:3])
        postcode2.append(item[:2])
    pc0 = {'Postcode': postcode0}
    pc1 = {'Postcode': postcode1}
    pc2 = {'Postcode': postcode2}
    postcodeDF0 = pd.DataFrame(data=pc0)
    postcodeDF1 = pd.DataFrame(data=pc1)
    postcodeDF2 = pd.DataFrame(data=pc2)
    postcodeDFList.append(postcodeDF0)
    postcodeDFList.append(postcodeDF1)
    postcodeDFList.append(postcodeDF2)
    return postcodeDFList


def convertColumns():  # creates dataframe lists once at the start of algorithm
    for column in VoterListColumns:
        if column == 'Name':
            convertColumns.nameList = name(column)
        if column == 'Sex':
            convertColumns.sexList = sex(column)
        if column == 'Address':
            convertColumns.addressList = address(column)
        # 3D Items
        if column == 'Age':
            convertColumns.ageList = age(column)
        if column == 'Postcode':
            convertColumns.postcodeList = postcode(column)


def dimDFConversion(node):  # converts to dim dataframe for incognito algorithm
    # dimensionTables()
    # sexList = dimensionTables.sexDF
    # postcodeList = postcode(column)

    for index in range(1, len(node), 2):
        column = node[index - 1]
        dim = int(node[index])
        # print(column, dim)

        # print(name(column))

        # # 1D Items
        # if column == 'Party':
        #     change = party(column)
        # 2D Items
        if column == 'Name':
            change = convertColumns.nameList[dim]
        if column == 'Sex':
            change = convertColumns.sexList[dim]
        if column == 'Address':
            change = convertColumns.addressList[dim]
        # 3D Items
        if column == 'Age':
            change = convertColumns.ageList[dim]
        if column == 'Postcode':
            change = convertColumns.postcodeList[dim]
        # if column == 'Sex':
        #     temp = sexList[dim]
        # if column == 'Postcode':
        #     temp = postcodeList[dim]

        # print(temp)
        # data1 = {name: temp}
        # tempDF = pd.DataFrame(data=data1)
        # print(tempDF)
        VoterListDF[column] = change[column]
    # print(VoterListDF)
    # dimDataframe = VoterListDF
    return VoterListDF


# def dimensionTables():  # converts columns for each dim dataframe depending on dimension
#     # 1 dimension: party
#     # 2 dimensions: name, sex, address
#     # 3 dimensions: age and postcode
#
#     for column in VoterListColumns:  # for each column in the table
#         # print(column)
#         # 1D Items
#         if column == 'Party':
#         # 2D Items
#         if column == 'Name':
#             if column == 'Sex':
#                 if column == 'Address':
#         # 3D Items
#         if column == 'Age':
#             if column == 'Postcode':
