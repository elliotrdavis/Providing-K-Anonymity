# Create dimension tables

import pandas as pd
import pymysql
from functools import reduce
from itertools import product

from sqlalchemy import create_engine

from KValue import VoterListDF, VoterListColumns

host = 'localhost'
user = 'root'
password = 'root'
database = 'dimindex'

def candidateNodeTable():
    connection = pymysql.connect(host=host, user=user, password=password, database=database)

    my_cursor = connection.cursor()

    # Execute Query
    my_cursor.execute("SELECT * from sex")

    # Fetch the records
    sex = my_cursor.fetchall()

    my_cursor.execute("SELECT * from postcode")
    postcode = my_cursor.fetchall()

    sexList = []
    postcodeList = []
    for i in sex:
        #print(i[2])
        sexList.append(str(i[2]))

    for j in postcode:
        #print(j[2])
        postcodeList.append(str(j[2]))

    comp = [tuple(postcodeList), tuple(sexList)]
    candidateConnections = list(reduce(lambda a, b: [(p[1], *p[0]) for p in product(a, b)], comp))
    #print(candidateConnections)
    # turn this into df
    #[('0', '0'), ('1', '0'), ('0', '1'), ('1', '1'), ('0', '2'), ('1', '2')]
    candidateNodeTable.newCandidateConnections = []
    dimensions = ('Sex', 'Postcode')
    for tuple1 in candidateConnections: # for each tuple in above list
        newTuple = []
        for index in range(len(tuple1)): # for each index in the tuple
            newTuple.append(dimensions[index])
            newTuple.append(tuple1[index])
        candidateNodeTable.newCandidateConnections.append(newTuple)
    #print(newCandidateConnections)
    # add to dataframe
    candidateColumns = ['dim1', 'index1', 'dim2', 'index2']
    candidateConnectionsDF = pd.DataFrame(candidateNodeTable.newCandidateConnections, columns=candidateColumns)
    #print(candidateConnectionsDF)
    #upload to sql server
    engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                           .format(user=user,
                                   pw=password,
                                   db=database))
    candidateConnectionsDF.to_sql('candidate', con=engine, if_exists='replace', chunksize=1000)

    # comp = [('0', '1', '2'), ('0', '1'), ('0', '1',)]
    # print(list(reduce(lambda a, b: [(p[1], *p[0]) for p in product(a, b)], comp)))

    connection.close()


def generateEdges():
    candidateNodeTable()
    # to do
    # Subset property: let T be a relation, and let Q be a set of attributes in T.
    # If T is k-anonymous with respect to Q, then T is k-anonymous with respect to any set of
    # attributes P such that P < Q
    #print(candidateNodeTable.newCandidateConnections)
    # generate edges
    # edges are tuples, create list of tuples and append
    edges = []
    # for each node create its edges
    for node in candidateNodeTable.newCandidateConnections: ## go through every node in candidate nodes
        print('for each now:', node)
        # go through each index, check if legal then add to edge list
        for index in range(1, len(node), 2): # go through every index in each node
            #print(node[index])
            nextNode = int(node[index]) + 1
            #print(nextNode)
            for node2 in range(candidateNodeTable.newCandidateConnections.index(node)+1, len(candidateNodeTable.newCandidateConnections)):
                # iterate through every other node, check for match
                #print('search through for',node[index], candidateNodeTable.newCandidateConnections[node2])
                if(candidateNodeTable.newCandidateConnections[node2][1] == str(nextNode) and
                    candidateNodeTable.newCandidateConnections[node2][3] == '0'):
                    print(candidateNodeTable.newCandidateConnections[node2])






def indexTables():
    sexDim = [["Sex", 0],["Sex", 1]]
    postcodeDim = [["Postcode", 0], ["Postcode", 1],["Postcode", 2]]
    dimColumns = ['dim', 'index']
    indexTables.sexDimDF = pd.DataFrame(data=sexDim, columns=dimColumns)
    indexTables.postcodeDimDF = pd.DataFrame(data=postcodeDim, columns=dimColumns)

def dimensionTables():
    # For each column in table
    # calculate number of dimensions
    # 1 dimension: party
    # 2 dimensions: name, sex, address
    # 3 dimensions: age and postcode
    # for each dimension make a new table with new dimension values
    # add the new table to arraylist for each column

    partyDFList = []
    nameDFList = []
    sexDFList = []
    addressDFList = []
    ageDFList = []
    postcodeDFList = []
    for column in VoterListColumns: # for each column in the table
        #print(column)
        # 1D Items
        if (column == 'Party'):
            party0 = []
            for item in VoterListDF[column]: # for each item in column
                party0.append(item)
            p0 = {'Party': party0}
            dimensionTables.partyDF0 = pd.DataFrame(data=p0)
            partyDFList.append(dimensionTables.partyDF0)

        # 2D Items
        if(column == 'Name'):
            name0 = []
            name1 = []
            for item in VoterListDF[column]:
                name0.append(item)
                item = '-'
                name1.append(item)
            n0 = {'Name': name0}
            n1 = {'Name': name1}
            dimensionTables.nameDF0 = pd.DataFrame(data=n0)
            dimensionTables.nameDF1 = pd.DataFrame(data=n1)
            nameDFList.append(dimensionTables.nameDF0)
            nameDFList.append(dimensionTables.nameDF1)

        if (column == 'Sex'):
            sex0 = []
            sex1 = []
            for item in VoterListDF[column]:
                sex0.append(item)
                item = '-'
                sex1.append(item)
            s0 = {'Sex': sex0}
            s1 = {'Sex': sex1}
            dimensionTables.sexDF0 = pd.DataFrame(data=s0)
            dimensionTables.sexDF1 = pd.DataFrame(data=s1)
            sexDFList.append(dimensionTables.sexDF0)
            sexDFList.append(dimensionTables.sexDF1)

        if (column == 'Address'):
            address0 = []
            address1 = []
            for item in VoterListDF[column]:
                address0.append(item)
                item = '-'
                address1.append(item)
            a0 = {'Address': address0}
            a1 = {'Address': address1}
            dimensionTables.addressDF0 = pd.DataFrame(data=a0)
            dimensionTables.addressDF1 = pd.DataFrame(data=a1)
            addressDFList.append(dimensionTables.addressDF0)
            addressDFList.append(dimensionTables.addressDF1)

        # 3D Items
        if (column == 'Age'):
            age0 = []
            age1 = []
            age2 = []
            for item in VoterListDF[column]:
                age0.append(item)
                if 0 <= item <= 5:
                    range = '0<=x<=5'
                if 5 < item <= 10:
                    range = '5<x<=10'
                if 10 < item <= 15:
                    range = '10<x<=15'
                if 15 < item <= 20:
                    range = '15<x<=20'
                if 20 < item <= 25:
                    range = '20<x<=25'
                if 25 < int(item) <= 30:
                    range = "25<x<=30"
                if 30 < int(item) <= 35:
                    range = "30<x<=35"
                if 35 < int(item) <= 40:
                    range = '35<x<=40'
                age1.append(range)

                if range == '0<=x<=5' or range == '5<x<=10':
                    range = '0<=x<=10'
                if range == '10<x<=15' or range == '15<x<=20':
                    range = '10<x<=20'
                if range == '20<x<=25' or range == '25<x<=30':
                    range = '20<x<=30'
                if range == '30<x<=35' or range == '35<x<=40':
                    range = '30<x<=40'
                age2.append(range)

            ag0 = {'Age': age0}
            ag1 = {'Age': age1}
            ag2 = {'Age': age2}
            dimensionTables.ageDF0 = pd.DataFrame(data=ag0)
            dimensionTables.ageDF1 = pd.DataFrame(data=ag1)
            dimensionTables.ageDF2 = pd.DataFrame(data=ag2)
            ageDFList.append(dimensionTables.ageDF0)
            ageDFList.append(dimensionTables.ageDF1)
            ageDFList.append(dimensionTables.ageDF2)

        if (column == 'Postcode'):
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
            dimensionTables.postcodeDF0 = pd.DataFrame(data=pc0)
            dimensionTables.postcodeDF1 = pd.DataFrame(data=pc1)
            dimensionTables.postcodeDF2 = pd.DataFrame(data=pc2)
            postcodeDFList.append(dimensionTables.postcodeDF0)
            postcodeDFList.append(dimensionTables.postcodeDF1)
            postcodeDFList.append(dimensionTables.postcodeDF2)

