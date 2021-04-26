"""
ColumnConversion.py
Author: Elliot Davis

This file is responsible for converting the columns for each attribute we want to generalize.

"""
import pandas as pd
import copy
from KValue import readFiles

datasetDF = readFiles()


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
            if len(item) == 0:
                item = 0
            item = float(item)
            if 0 <= item <= 5:
                genRange = '0<=x<=5'
            elif 5 < item <= 10:
                genRange = '5<x<=10'
            elif 10 < item <= 15:
                genRange = '10<x<=15'
            elif 15 < item <= 20:
                genRange = '15<x<=20'
            elif 20 < item <= 25:
                genRange = '20<x<=25'
            elif 25 < item <= 30:
                genRange = "25<x<=30"
            elif 30 < item <= 35:
                genRange = "30<x<=35"
            elif 35 < item <= 40:
                genRange = '35<x<=40'
            elif 40 < item <= 45:
                genRange = '40<x<=45'
            elif 45 < item <= 50:
                genRange = '45<x<=50'
            elif 50 < item <= 55:
                genRange = '50<x<=55'
            elif 55 < item <= 60:
                genRange = '55<x<=60'
            elif 60 < item <= 65:
                genRange = '60<x<=65'
            elif 65 < item <= 70:
                genRange = '65<x<=70'
            elif 70 < item <= 75:
                genRange = '70<x<=75'
            elif 75 < item <= 80:
                genRange = '75<x<=80'
            elif 80 < item <= 85:
                genRange = '80<x<=85'
            elif 85 < item <= 90:
                genRange = '85<x<=90'
            elif 90 < item <= 95:
                genRange = '90<x<=95'
            elif 95 < item <= 100:
                genRange = '95<x<=100'
            columnToGen.append(genRange)
        data = {column: columnToGen}
        return pd.DataFrame(data=data)

    if dim == 2:
        for item in datasetDF[column]:
            if len(item) == 0:
                item = 0
            item = float(item)
            if 0 <= item <= 10:
                genRange = '0<=x<=10'
            elif 10 < item <= 20:
                genRange = '10<x<=20'
            elif 20 < item <= 30:
                genRange = '20<x<=30'
            elif 30 < item <= 40:
                genRange = "30<x<=40"
            elif 40 < item <= 50:
                genRange = '40<x<=50'
            elif 50 < item <= 60:
                genRange = '50<x<=60'
            elif 60 < item <= 70:
                genRange = '60<x<=70'
            elif 70 < item <= 80:
                genRange = '70<x<=80'
            elif 80 < item <= 90:
                genRange = '80<x<=90'
            elif 90 < item <= 100:
                genRange = '90<x<=100'
            columnToGen.append(genRange)
        data = {column: columnToGen}
        return pd.DataFrame(data=data)

    if dim == 3:
        for item in datasetDF[column]:
            if len(item) == 0:
                item = 0
            item = float(item)
            if 0 <= item <= 20:
                genRange = '0<=x<=20'
            elif 20 < item <= 40:
                genRange = '20<x<=40'
            elif 40 < item <= 60:
                genRange = '40<x<=60'
            elif 60 < item <= 80:
                genRange = "60<x<=80"
            elif 80 < item <= 100:
                genRange = '80<x<=100'
            columnToGen.append(genRange)
        data = {column: columnToGen}
        return pd.DataFrame(data=data)

    if dim == 4:
        for item in datasetDF[column]:
            if len(item) == 0:
                item = 0
            item = float(item)
            if 0 <= item <= 50:
                genRange = '0<=x<=50'
            elif 50 < item <= 100:
                genRange = '50<x<=100'
            columnToGen.append(genRange)
        data = {column: columnToGen}
        return pd.DataFrame(data=data)

    if dim == 5:
        for item in datasetDF[column]:
            item = '-'
            columnToGen.append(item)
        data = {column: columnToGen}
        return pd.DataFrame(data=data)


def generalizeNumericList2(column, dim):
    columnToGen = []
    if dim == 0:
        for item in datasetDF[column]:
            columnToGen.append(item)
        data = {column: columnToGen}
        return pd.DataFrame(data=data)

    if dim == 1:
        for item in datasetDF[column]:
            item = float(item)
            if 0 <= item <= 200:
                genRange = '0<=x<=200'
            elif 200 < item <= 400:
                genRange = '200<x<=400'
            elif 400 < item <= 600:
                genRange = '400<x<=600'
            elif 600 < item <= 800:
                genRange = '600<x<=800'
            elif 800 < item <= 1000:
                genRange = '800<x<=1000'
            elif 1000 < item <= 1200:
                genRange = "1000<x<=1200"
            elif 1200 < item <= 1400:
                genRange = "1200<x<=1400"
            elif 1400 < item <= 1600:
                genRange = '1400<x<=1600'
            elif 1600 < item <= 1800:
                genRange = '1600<x<=1800'
            elif 1800 < item <= 2000:
                genRange = '1800<x<=2000'
            elif 2000 < item <= 2200:
                genRange = '2000<x<=2200'
            elif 2200 < item <= 2400:
                genRange = '2200<x<=2400'
            elif 2400 < item <= 2600:
                genRange = '2400<x<=2600'
            elif 2600 < item <= 2800:
                genRange = '2600<x<=2800'
            elif 2800 < item <= 3000:
                genRange = '2800<x<=3000'
            elif 3000 < item <= 3200:
                genRange = '3000<x<=3200'
            elif 3200 < item <= 3400:
                genRange = '3200<x<=3400'
            elif 3400 < item <= 3600:
                genRange = '3400<x<=3600'
            elif 3600 < item <= 3800:
                genRange = '3600<x<=3800'
            elif 3800 < item <= 4000:
                genRange = '3800<x<=4000'
            elif item > 4000:
                genRange = 'x>4000'
            columnToGen.append(genRange)
        data = {column: columnToGen}
        return pd.DataFrame(data=data)

    if dim == 2:
        for item in datasetDF[column]:
            item = float(item)
            if 0 <= item <= 400:
                genRange = '0<=x<=400'
            elif 400 < item <= 800:
                genRange = '400<x<=800'
            elif 800 < item <= 1200:
                genRange = '800<x<=1200'
            elif 1200 < item <= 1600:
                genRange = '1200<x<=1600'
            elif 1600 < item <= 2000:
                genRange = '1600<x<=2000'
            elif 2000 < item <= 2400:
                genRange = "2000<x<=2400"
            elif 2400 < item <= 2800:
                genRange = "2400<x<=2800"
            elif 2800 < item <= 3200:
                genRange = '2800<x<=3200'
            elif 3200 < item <= 3600:
                genRange = '3200<x<=3600'
            elif 3600 < item <= 4000:
                genRange = '3600<x<=4000'
            elif item > 4000:
                genRange = 'x>4000'
            columnToGen.append(genRange)
        data = {column: columnToGen}
        return pd.DataFrame(data=data)

    if dim == 3:
        for item in datasetDF[column]:
            item = float(item)
            if 0 <= item <= 800:
                genRange = '0<=x<=800'
            elif 800 < item <= 1600:
                genRange = '800<x<=1600'
            elif 1600 < item <= 2400:
                genRange = '1600<x<=2400'
            elif 2400 < item <= 3200:
                genRange = '2400<x<=3200'
            elif 3200 < item <= 4000:
                genRange = '3200<x<=4000'
            elif item > 4000:
                genRange = 'x>4000'
            columnToGen.append(genRange)
        data = {column: columnToGen}
        return pd.DataFrame(data=data)

    if dim == 4:
        for item in datasetDF[column]:
            item = float(item)
            if item <= 1600:
                genRange = 'x<=1600'
            elif item > 1600:
                genRange = 'x>1600'
            columnToGen.append(genRange)
        data = {column: columnToGen}
        return pd.DataFrame(data=data)

    if dim == 5:
        for item in datasetDF[column]:
            item = '-'
            columnToGen.append(item)
        data = {column: columnToGen}
        return pd.DataFrame(data=data)


def generalizeNumericList3(column, dim):
    columnToGen = []
    if dim == 0:
        for item in datasetDF[column]:
            columnToGen.append(item)
        data = {column: columnToGen}
        return pd.DataFrame(data=data)

    if dim == 1:
        for item in datasetDF[column]:
            item = float(item)
            if 0 <= item <= 2:
                genRange = '0<=x<=2'
            elif 2 < item <= 4:
                genRange = '2<x<=4'
            elif 4 < item <= 6:
                genRange = '4<x<=6'
            elif item > 6:
                genRange = 'x>6'
            columnToGen.append(genRange)
        data = {column: columnToGen}
        return pd.DataFrame(data=data)

    if dim == 2:
        for item in datasetDF[column]:
            item = '-'
            columnToGen.append(item)
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
def updateColumn(column, dim, suppress, numeric, shorten, n2, n3):
    if column in suppress:
        change = suppressList(column, dim)
    elif column in numeric:
        change = generalizeNumericList(column, dim)
    elif column in shorten:
        change = shortenList(column, dim)
    elif column in n2:
        change = generalizeNumericList2(column, dim)
    elif column in n3:
        change = generalizeNumericList3(column, dim)
    return change


# Updates dataset columns depending on node passed in
# Node is the combination of generalizations needed to be returned e.g. (Name, 1, Sex, 0)
def updateDataframe(node, suppress, numeric, shorten, n2, n3):
    datasetDF1 = copy.deepcopy(datasetDF)
    # Iterate through node
    for index in range(1, len(node), 2):
        column = node[index - 1]  # e.g. Name
        dim = int(node[index])  # e.g. 1

        change = updateColumn(column, dim, suppress, numeric, shorten, n2, n3)  # Determine which column to update
        datasetDF1[column] = change[column]  # Updates original dataframe with new column

    return datasetDF1


# Creates dataframe depending on node passed in - used for incognito algorithm
# Node is the combination of generalizations needed to be returned e.g. (Name, 1, Sex, 0)
def createTempDataframe(node, suppress, numeric, shorten, n2, n3):

    # Create temporary dataframe for incognito algorithm
    data = {}
    df = pd.DataFrame(data)

    # Iterate through node
    for index in range(1, len(node), 2):
        column = node[index - 1]
        dim = int(node[index])

        change = updateColumn(column, dim, suppress, numeric, shorten, n2, n3)  # Determine which column to update
        df[column] = change[column]  # Updates original dataframe with new column

    return df
