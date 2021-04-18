"""
ColumnConversion.py
Author: Elliot Davis

This file is responsible for converting the columns for each attribute we want to generalize.

"""
import pandas as pd
# from KValue import readFiles
import copy

from KValue import readFiles

datasetDF = readFiles()
# from KValue import datasetDF

nameDFList = []
sexDFList = []
addressDFList = []
patientIDDFList = []
treatmentDFList = []
ageDFList = []
postcodeDFList = []
weightDFList = []

patientID = [["Patient ID", 0], ["Patient ID", 1]]
weight = [["Weight (kg)", 0], ["Weight (kg)", 1], ["Weight (kg)", 2]]
treatment = [["Treatment", 0], ["Treatment", 1]]


def suppressList(column, dim):
    columnToSup = []
    if dim == 0:
        for item in datasetDF[column]:
            columnToSup.append(item)
        data = {column: columnToSup}
        return pd.DataFrame(data=data)
    if dim == 1:
        for item in datasetDF[column]:
            item = '-'
            columnToSup.append(item)
        data = {column: columnToSup}
        return pd.DataFrame(data=data)


def generalizeNumericList(column, dim):
    columnToGen = []
    if dim == 0:
        for item in datasetDF[column]:
            columnToGen.append(item)
        data = {column: columnToGen}
        return pd.DataFrame(data=data)

    if dim == 1:
        for item in datasetDF[column]:
            item = float(item)
            if 0 <= item <= 5:
                genRange = '0<=x<=5'
            if 5 < item <= 10:
                genRange = '5<x<=10'
            if 10 < item <= 15:
                genRange = '10<x<=15'
            if 15 < item <= 20:
                genRange = '15<x<=20'
            if 20 < item <= 25:
                genRange = '20<x<=25'
            if 25 < item <= 30:
                genRange = "25<x<=30"
            if 30 < item <= 35:
                genRange = "30<x<=35"
            if 35 < item <= 40:
                genRange = '35<x<=40'
            if 40 < item <= 45:
                genRange = '40<x<=45'
            if 45 < item <= 50:
                genRange = '45<x<=50'
            if 50 < item <= 55:
                genRange = '50<x<=55'
            if 55 < item <= 60:
                genRange = '55<x<=60'
            if 60 < item <= 65:
                genRange = '60<x<=65'
            if 65 < item <= 70:
                genRange = '65<x<=70'
            if 70 < item <= 75:
                genRange = '70<x<=75'
            if 75 < item <= 80:
                genRange = '75<x<=80'
            if 80 < item <= 85:
                genRange = '80<x<=85'
            if 85 < item <= 90:
                genRange = '85<x<=90'
            if 90 < item <= 95:
                genRange = '90<x<=95'
            if 95 < item <= 100:
                genRange = '95<x<=100'
            columnToGen.append(genRange)
        data = {column: columnToGen}
        return pd.DataFrame(data=data)

    if dim == 2:
        for item in datasetDF[column]:
            item = float(item)
            if 0 <= item <= 10:
                genRange = '0<=x<=10'
            if 10 < item <= 20:
                genRange = '10<x<=20'
            if 20 < item <= 30:
                genRange = '20<x<=30'
            if 30 < item <= 40:
                genRange = "30<x<=40"
            if 40 < item <= 50:
                genRange = '40<x<=50'
            if 50 < item <= 60:
                genRange = '50<x<=60'
            if 60 < item <= 70:
                genRange = '60<x<=70'
            if 70 < item <= 80:
                genRange = '70<x<=80'
            if 80 < item <= 90:
                genRange = '80<x<=90'
            if 90 < item <= 100:
                genRange = '90<x<=100'
            columnToGen.append(genRange)
        data = {column: columnToGen}
        return pd.DataFrame(data=data)


def shortenList(column, dim):
    columnToGen = []
    if dim == 0:
        for item in datasetDF[column]:
            columnToGen.append(item)
        data = {column: columnToGen}
        return pd.DataFrame(data=data)

    if dim == 1:
        for item in datasetDF[column]:
            columnToGen.append(item[:3])
        data = {column: columnToGen}
        return pd.DataFrame(data=data)

    if dim == 2:
        for item in datasetDF[column]:
            columnToGen.append(item[:2])
        data = {column: columnToGen}
        return pd.DataFrame(data=data)


# Returns column depending on column name and dimension number parameters
# This method will only generate the generalized column if it hasn't been created yet, otherwise it will call it
# from the respective array
def updateColumn(column, dim, suppress, numeric, shorten):
    if column in suppress:
        change = suppressList(column, dim)
    if column in numeric:
        change = generalizeNumericList(column, dim)
    if column in shorten:
        change = shortenList(column, dim)
    return change


# Updates dataset columns depending on node passed in
# Node is the combination of generalizations needed to be returned e.g. (Name, 1, Sex, 0)
def updateDataframe(node, suppress, numeric, shorten):
    datasetDF1 = copy.deepcopy(datasetDF)
    # Iterate through node
    for index in range(1, len(node), 2):
        column = node[index - 1]  # e.g. Name
        dim = int(node[index])  # e.g. 1

        change = updateColumn(column, dim, suppress, numeric, shorten)  # Determine which column to update
        datasetDF1[column] = change[column]  # Updates original dataframe with new column

    return datasetDF1


# Creates dataframe depending on node passed in - used for incognito algorithm
# Node is the combination of generalizations needed to be returned e.g. (Name, 1, Sex, 0)
def createTempDataframe(node, suppress, numeric, shorten):

    # Create temporary dataframe for incognito algorithm
    data = {}
    df = pd.DataFrame(data)

    # Iterate through node
    for index in range(1, len(node), 2):
        column = node[index - 1]
        dim = int(node[index])

        change = updateColumn(column, dim, suppress, numeric, shorten)  # Determine which column to update
        df[column] = change[column]  # Updates original dataframe with new column

    return df
