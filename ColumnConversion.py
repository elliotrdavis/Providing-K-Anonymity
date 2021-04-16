"""
ColumnConversion.py
Author: Elliot Davis

This file is responsible for converting the columns for each attribute we want to generalize.

"""
import pandas as pd
from KValue import readFiles

datasetDF = readFiles()
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
        if len(nameDFList) == 0:
            name(column, 0)
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
        if len(sexDFList) == 0:
            sex(column, 0)
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
        if len(addressDFList) == 0:
            address(column, 0)
        for item in datasetDF[column]:
            item = '-'
            address1.append(item)
        a1 = {'Address': address1}
        addressDF1 = pd.DataFrame(data=a1)
        addressDFList.append(addressDF1)

    return addressDFList


# Converts column for patientID
def patientID(column, dim):

    patientID0 = []
    patientID1 = []

    if dim == 0:
        for item in datasetDF[column]:
            patientID0.append(item)
        p0 = {'Patient ID': patientID0}
        patientIDDF0 = pd.DataFrame(data=p0)
        patientIDDFList.append(patientIDDF0)

    if dim == 1:
        if len(patientIDDFList) == 0:
            patientID(column, 0)
        for item in datasetDF[column]:
            item = '-'
            patientID1.append(item)
        p1 = {'Patient ID': patientID1}
        patientIDDF1 = pd.DataFrame(data=p1)
        patientIDDFList.append(patientIDDF1)

    return patientIDDFList


# Converts column for treatment
def treatment(column, dim):

    treatment0 = []
    treatment1 = []

    if dim == 0:
        for item in datasetDF[column]:
            treatment0.append(item)
        t0 = {'Treatment': treatment0}
        treatmentDF0 = pd.DataFrame(data=t0)
        treatmentDFList.append(treatmentDF0)

    if dim == 1:
        if len(treatmentDFList) == 0:
            treatment(column, 0)
        for item in datasetDF[column]:
            item = '-'
            treatment1.append(item)
        t1 = {'Treatment': treatment1}
        treatmentDF1 = pd.DataFrame(data=t1)
        treatmentDFList.append(treatmentDF1)

    return treatmentDFList


# Converts column for age
def age(column, dim):

    age0 = []
    age1 = []
    age2 = []
    age3 = []

    if dim == 0:
        for item in datasetDF[column]:
            age0.append(item)
        ag0 = {'Age': age0}
        ageDF0 = pd.DataFrame(data=ag0)
        ageDFList.append(ageDF0)

    if dim == 1:
        if len(ageDFList) == 0:
            age(column, 0)
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
            if 40 < int(item) <= 45:
                ageRange = '40<x<=45'
            if 45 < int(item) <= 50:
                ageRange = '45<x<=50'
            if 50 < int(item) <= 55:
                ageRange = '50<x<=55'
            if 55 < int(item) <= 60:
                ageRange = '55<x<=60'
            if 60 < int(item) <= 65:
                ageRange = '60<x<=65'
            if 65 < int(item) <= 70:
                ageRange = '65<x<=70'
            if 70 < int(item) <= 75:
                ageRange = '70<x<=75'
            if 75 < int(item) <= 80:
                ageRange = '75<x<=80'
            if 80 < int(item) <= 85:
                ageRange = '80<x<=85'
            if 85 < int(item) <= 90:
                ageRange = '85<x<=90'
            if 90 < int(item) <= 95:
                ageRange = '90<x<=95'
            if 95 < int(item) <= 100:
                ageRange = '95<x<=100'
            age1.append(ageRange)
        ag1 = {'Age': age1}
        ageDF1 = pd.DataFrame(data=ag1)
        ageDFList.append(ageDF1)

    if dim == 2:
        if len(ageDFList) == 0:
            age(column, 0)
        if len(ageDFList) == 1:
            age(column, 1)
        for ageRange in ageDFList[1]["Age"]:
            if ageRange == '0<=x<=5' or ageRange == '5<x<=10':
                ageRange = '0<=x<=10'
            if ageRange == '10<x<=15' or ageRange == '15<x<=20':
                ageRange = '10<x<=20'
            if ageRange == '20<x<=25' or ageRange == '25<x<=30':
                ageRange = '20<x<=30'
            if ageRange == '30<x<=35' or ageRange == '35<x<=40':
                ageRange = '30<x<=40'
            if ageRange == '40<x<=45' or ageRange == '45<x<=50':
                ageRange = '40<x<=50'
            if ageRange == '50<x<=55' or ageRange == '55<x<=60':
                ageRange = '50<x<=60'
            if ageRange == '60<x<=65' or ageRange == '65<x<=70':
                ageRange = '60<x<=70'
            if ageRange == '70<x<=75' or ageRange == '75<x<=80':
                ageRange = '70<x<=80'
            if ageRange == '80<x<=85' or ageRange == '85<x<=90':
                ageRange = '80<x<=90'
            if ageRange == '90<x<=95' or ageRange == '95<x<=100':
                ageRange = '90<x<=100'
            age2.append(ageRange)
        ag2 = {'Age': age2}
        ageDF2 = pd.DataFrame(data=ag2)
        ageDFList.append(ageDF2)

    if dim == 3:
        if len(ageDFList) == 0:
            age(column, 0)
        if len(ageDFList) == 1:
            age(column, 1)
        if len(ageDFList) == 2:
            age(column, 2)
        for item in datasetDF[column]:
            item = '-'
            age3.append(item)
        a3 = {'Age': age3}
        ageDF3 = pd.DataFrame(data=a3)
        ageDFList.append(ageDF3)

    return ageDFList


# Converts column for weight
def weight(column, dim):

    weight0 = []
    weight1 = []
    weight2 = []

    if dim == 0:
        for item in datasetDF[column]:
            weight0.append(item)
        w0 = {'Weight (kg)': weight0}
        weightDF0 = pd.DataFrame(data=w0)
        weightDFList.append(weightDF0)

    if dim == 1:
        if len(weightDFList) == 0:
            weight(column, 0)
        for item in weightDFList[0]["Weight (kg)"]:
            if 0 <= int(item) <= 5:
                weightRange = '0<=x<=5'
            if 5 < int(item) <= 10:
                weightRange = '5<x<=10'
            if 10 < int(item) <= 15:
                weightRange = '10<x<=15'
            if 15 < int(item) <= 20:
                weightRange = '15<x<=20'
            if 20 < int(item) <= 25:
                weightRange = '20<x<=25'
            if 25 < int(item) <= 30:
                weightRange = "25<x<=30"
            if 30 < int(item) <= 35:
                weightRange = "30<x<=35"
            if 35 < int(item) <= 40:
                weightRange = '35<x<=40'
            if 40 < int(item) <= 45:
                weightRange = '40<x<=45'
            if 45 < int(item) <= 50:
                weightRange = '45<x<=50'
            if 50 < int(item) <= 55:
                weightRange = '50<x<=55'
            if 55 < int(item) <= 60:
                weightRange = '55<x<=60'
            if 60 < int(item) <= 65:
                weightRange = '60<x<=65'
            if 65 < int(item) <= 70:
                weightRange = '65<x<=70'
            if 70 < int(item) <= 75:
                weightRange = '70<x<=75'
            if 75 < int(item) <= 80:
                weightRange = '75<x<=80'
            if 80 < int(item) <= 85:
                weightRange = '80<x<=85'
            if 85 < int(item) <= 90:
                weightRange = '85<x<=90'
            if 90 < int(item) <= 95:
                weightRange = '90<x<=95'
            if 95 < int(item) <= 100:
                weightRange = '95<x<=100'
            weight1.append(weightRange)
        w1 = {'Weight (kg)': weight1}
        weightDF1 = pd.DataFrame(data=w1)
        weightDFList.append(weightDF1)

    if dim == 2:
        if len(weightDFList) == 0:
            weight(column, 0)
        if len(weightDFList) == 1:
            weight(column, 1)
        for weightRange in weightDFList[1]["Weight (kg)"]:
            if weightRange == '0<=x<=5' or weightRange == '5<x<=10':
                weightRange = '0<=x<=10'
            if weightRange == '10<x<=15' or weightRange == '15<x<=20':
                weightRange = '10<x<=20'
            if weightRange == '20<x<=25' or weightRange == '25<x<=30':
                weightRange = '20<x<=30'
            if weightRange == '30<x<=35' or weightRange == '35<x<=40':
                weightRange = '30<x<=40'
            if weightRange == '40<x<=45' or weightRange == '45<x<=50':
                weightRange = '40<x<=50'
            if weightRange == '50<x<=55' or weightRange == '55<x<=60':
                weightRange = '50<x<=60'
            if weightRange == '60<x<=65' or weightRange == '65<x<=70':
                weightRange = '60<x<=70'
            if weightRange == '70<x<=75' or weightRange == '75<x<=80':
                weightRange = '70<x<=80'
            if weightRange == '80<x<=85' or weightRange == '85<x<=90':
                weightRange = '80<x<=90'
            if weightRange == '90<x<=95' or weightRange == '95<x<=100':
                weightRange = '90<x<=100'
            weight2.append(weightRange)
        w2 = {'Weight (kg)': weight2}
        weightDF2 = pd.DataFrame(data=w2)
        weightDFList.append(weightDF2)

    return weightDFList


# Converts column for postcode
def postcode(column, dim):

    postcode0 = []
    postcode1 = []
    postcode2 = []
    postcode3 = []

    if dim == 0:
        for item in datasetDF[column]:
            postcode0.append(item)
        pc0 = {'Postcode': postcode0}
        postcodeDF0 = pd.DataFrame(data=pc0)
        postcodeDFList.append(postcodeDF0)

    if dim == 1:
        if len(postcodeDFList) == 0:
            postcode(column, 0)
        for item in datasetDF[column]:
            postcode1.append(item[:3])
        pc1 = {'Postcode': postcode1}
        postcodeDF1 = pd.DataFrame(data=pc1)
        postcodeDFList.append(postcodeDF1)

    if dim == 2:
        if len(postcodeDFList) == 0:
            postcode(column, 0)
        if len(postcodeDFList) == 1:
            postcode(column, 1)
        for item in datasetDF[column]:
            postcode2.append(item[:2])
        pc2 = {'Postcode': postcode2}
        postcodeDF2 = pd.DataFrame(data=pc2)
        postcodeDFList.append(postcodeDF2)

    if dim == 3:
        if len(postcodeDFList) == 0:
            postcode(column, 0)
        if len(postcodeDFList) == 1:
            postcode(column, 1)
        if len(postcodeDFList) == 2:
            postcode(column, 2)
        for item in datasetDF[column]:
            item = '-'
            postcode3.append(item)
        p3 = {'Postcode': postcode3}
        postcodeDF3 = pd.DataFrame(data=p3)
        postcodeDFList.append(postcodeDF3)

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

    if column == 'Patient ID':
        if dim <= (len(patientIDDFList) - 1):
            change = patientIDDFList[dim]
        else:
            patientIDList = patientID(column, dim)
            change = patientIDList[dim]

    if column == 'Treatment':
        if dim <= (len(treatmentDFList) - 1):
            change = treatmentDFList[dim]
        else:
            treatmentList = treatment(column, dim)
            change = treatmentList[dim]

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

    if column == 'Weight (kg)':
        if dim <= (len(weightDFList) - 1):
            change = weightDFList[dim]
        else:
            weightList = weight(column, dim)
            change = weightList[dim]

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
