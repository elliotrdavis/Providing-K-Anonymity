"""
ColumnConversion.py
Author: Elliot Davis

This file is responsible for

"""

import pandas as pd
from KValue import datasetDF

nameDFList = []
sexDFList = []
addressDFList = []
ageDFList = []
postcodeDFList = []


# Converts column for name
def name(column, dim):

    name0 = []
    name1 = []

    if dim == 0:
        for item in datasetDF[column]:
            name0.append(item)
        n0 = {'Name': name0}
        nameDF0 = pd.DataFrame(data=n0)
        nameDFList.append(nameDF0)

    if dim == 1:
        for item in datasetDF[column]:
            item = '-'
            name1.append(item)
        n1 = {'Name': name1}
        nameDF1 = pd.DataFrame(data=n1)
        nameDFList.append(nameDF1)

    return nameDFList


# Converts column for sex
def sex(column, dim):

    sex0 = []
    sex1 = []

    if dim == 0:
        for item in datasetDF[column]:
            sex0.append(item)
        s0 = {'Sex': sex0}
        sexDF0 = pd.DataFrame(data=s0)
        sexDFList.append(sexDF0)

    if dim == 1:
        for item in datasetDF[column]:
            item = '-'
            sex1.append(item)
        s1 = {'Sex': sex1}
        sexDF1 = pd.DataFrame(data=s1)
        sexDFList.append(sexDF1)

    return sexDFList


# Converts column for address
def address(column, dim):

    address0 = []
    address1 = []

    if dim == 0:
        for item in datasetDF[column]:
            address0.append(item)
        a0 = {'Address': address0}
        addressDF0 = pd.DataFrame(data=a0)
        addressDFList.append(addressDF0)

    if dim == 1:
        for item in datasetDF[column]:
            item = '-'
            address1.append(item)
        a1 = {'Address': address1}
        addressDF1 = pd.DataFrame(data=a1)
        addressDFList.append(addressDF1)

    return addressDFList


# Converts column for age
def age(column, dim):

    age0 = []
    age1 = []
    age2 = []

    if dim == 0:
        for item in datasetDF[column]:
            age0.append(item)
        ag0 = {'Age': age0}
        ageDF0 = pd.DataFrame(data=ag0)
        ageDFList.append(ageDF0)

    if dim == 1:
        for item in ageDFList[0]["Age"]:
            if 0 <= int(item) <= 5:
                ageRange = '0<=x<=5'
            if 5 < int(item) <= 10:
                ageRange = '5<x<=10'
            if 10 < int(item) <= 15:
                ageRange = '10<x<=15'
            if 15 < int(item) <= 20:
                ageRange = '15<x<=20'
            if 20 < int(item) <= 25:
                ageRange = '20<x<=25'
            if 25 < int(item) <= 30:
                ageRange = "25<x<=30"
            if 30 < int(item) <= 35:
                ageRange = "30<x<=35"
            if 35 < int(item) <= 40:
                ageRange = '35<x<=40'
            age1.append(ageRange)
        ag1 = {'Age': age1}
        ageDF1 = pd.DataFrame(data=ag1)
        ageDFList.append(ageDF1)

    if dim == 2:
        for ageRange in ageDFList[1]["Age"]:
            if ageRange == '0<=x<=5' or ageRange == '5<x<=10':
                ageRange = '0<=x<=10'
            if ageRange == '10<x<=15' or ageRange == '15<x<=20':
                ageRange = '10<x<=20'
            if ageRange == '20<x<=25' or ageRange == '25<x<=30':
                ageRange = '20<x<=30'
            if ageRange == '30<x<=35' or ageRange == '35<x<=40':
                ageRange = '30<x<=40'
            age2.append(ageRange)
        ag2 = {'Age': age2}
        ageDF2 = pd.DataFrame(data=ag2)
        ageDFList.append(ageDF2)

    return ageDFList


# Converts column for postcode
def postcode(column, dim):

    postcode0 = []
    postcode1 = []
    postcode2 = []

    if dim == 0:
        for item in datasetDF[column]:
            postcode0.append(item)
        pc0 = {'Postcode': postcode0}
        postcodeDF0 = pd.DataFrame(data=pc0)
        postcodeDFList.append(postcodeDF0)

    if dim == 1:
        for item in datasetDF[column]:
            postcode1.append(item[:3])
        pc1 = {'Postcode': postcode1}
        postcodeDF1 = pd.DataFrame(data=pc1)
        postcodeDFList.append(postcodeDF1)

    if dim == 2:
        for item in datasetDF[column]:
            postcode2.append(item[:2])
        pc2 = {'Postcode': postcode2}
        postcodeDF2 = pd.DataFrame(data=pc2)
        postcodeDFList.append(postcodeDF2)

    return postcodeDFList


# Returns column depending on column name and dimension number parameters
# This method will only generate the generalized column if it hasn't been created yet, otherwise it will call it
# from the respective array
def updateColumn(column, dim):
    # 2D Items
    if column == 'Name':
        if dim <= (len(nameDFList) - 1):
            change = nameDFList[dim]
        else:
            nameList = name(column, dim)
            change = nameList[dim]

    if column == 'Sex':
        if dim <= (len(sexDFList) - 1):
            change = sexDFList[dim]
        else:
            sexList = sex(column, dim)
            change = sexList[dim]

    if column == 'Address':
        if dim <= (len(addressDFList) - 1):
            change = addressDFList[dim]
        else:
            addressList = address(column, dim)
            change = addressList[dim]

    # 3D Items
    if column == 'Age':
        if dim <= (len(ageDFList) - 1):
            change = ageDFList[dim]
        else:
            ageList = age(column, dim)
            change = ageList[dim]

    if column == 'Postcode':
        if dim <= (len(postcodeDFList) - 1):
            change = postcodeDFList[dim]
        else:
            postcodeList = postcode(column, dim)
            change = postcodeList[dim]

    return change


# Updates dataset columns depending on node passed in
# Node is the combination of generalizations needed to be returned e.g. (Name, 1, Sex, 0)
def updateDataframe(node):

    # Iterate through node
    for index in range(1, len(node), 2):
        column = node[index - 1]  # e.g. Name
        dim = int(node[index])  # e.g. 1

        change = updateColumn(column, dim)  # Determine which column to update
        datasetDF[column] = change[column]  # Updates original dataframe with new column

    return datasetDF


# Creates dataframe depending on node passed in - used for incognito algorithm
# Node is the combination of generalizations needed to be returned e.g. (Name, 1, Sex, 0)
def createTempDataframe(node):

    # Create temporary dataframe for incognito algorithm
    data = {}
    df = pd.DataFrame(data)

    # Iterate through node
    for index in range(1, len(node), 2):
        column = node[index - 1]
        dim = int(node[index])

        change = updateColumn(column, dim)  # Determine which column to update
        df[column] = change[column]  # Updates original dataframe with new column

    return df


# def indexTables():  # creates index tables for dimension tables
#     partyDim = [["Party", 0]]
#     nameDim = [["Name", 0], ["Name", 1]]
#     sexDim = [["Sex", 0], ["Sex", 1]]
#     addressDim = [["Address", 0], ["Address", 1]]
#     ageDim = [["Age", 0], ["Age", 1], ["Age", 2]]
#     postcodeDim = [["Postcode", 0], ["Postcode", 1], ["Postcode", 2]]
#
#     dimColumns = ['dim', 'index']
#
#     indexTables.partyDimDF = pd.DataFrame(data=partyDim, columns=dimColumns)
#     indexTables.nameDimDF = pd.DataFrame(data=nameDim, columns=dimColumns)
#     indexTables.sexDimDF = pd.DataFrame(data=sexDim, columns=dimColumns)
#     indexTables.addressDimDF = pd.DataFrame(data=addressDim, columns=dimColumns)
#     indexTables.ageDimDF = pd.DataFrame(data=ageDim, columns=dimColumns)
#     indexTables.postcodeDimDF = pd.DataFrame(data=postcodeDim, columns=dimColumns)

# # Iterates through columns in our dataset to get DFList for each column
# def convertColumns():
#     for column in datasetColumns:
#         # 2D Items
#         if column == 'Name':
#             convertColumns.nameList = name(column)
#         if column == 'Sex':
#             convertColumns.sexList = sex(column)
#         if column == 'Address':
#             convertColumns.addressList = address(column)
#         # 3D Items
#         if column == 'Age':
#             convertColumns.ageList = age(column)
#         if column == 'Postcode':
#             convertColumns.postcodeList = postcode(column)
