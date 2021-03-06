"""
KValue.py
Author: Elliot Davis

In this file I have created some example datasets and can calculate the k-value

"""

import pandas as pd
import csv


def readHeader():
    # file1 = open('data/census/census-header-edited-10.txt', 'r')
    file1 = open('data/voterlist/voterlist-header.txt', 'r')
    lines = file1.readlines()
    return lines


def readFiles():
    newList = []
    datasetColumns = []
    count = 0

    with open('data/census/census-income_ALL-edited-10.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if count == 5000:
                break
            count = count + 1
            newList.append(row)

    lines = readHeader()
    for line in lines:
        line = line.split()
        datasetColumns.append(line[0])

    newList = VoterList
    datasetDF = pd.DataFrame(newList, columns=datasetColumns)
    return datasetDF


MedicalList = [[56183, 35, "Male", 96, "Asthma", "Inhaler", "SE5 6AH"],
               [11023, 25, "Female", 65, "Back Pain", "Physiotherapy", "SE7 6LF"],
               [74128, 21, "Female", 56, "Cancer", "Chemotherapy", "SE7 9PQ"],
               [86300, 35, "Male", 86, "Cancer", "Chemotherapy", "SE5 8LP"],
               [53754, 28, "Male", 68, "Asthma", "Inhaler", "SE7 8QX"],
               [12848, 23, "Female", 82, "Cancer", "Chemotherapy", "SE6 9WG"],
               [53245, 32, "Female", 75, "Cancer", "Chemotherapy", "SE7 6RF"],
               [98753, 34, "Female", 48, "Back Pain", "Physiotherapy", "SE7 7LF"],
               [54894, 29, "Female", 53, "Back Pain", "Physiotherapy", "SE6 3NG"],
               [84653, 29, "Male", 90, "Asthma", "Inhaler", "SE7 3FE"]]

VoterList = [["Oskar Green", "35", "Male", "10 Bairstow Road", "Conservative", "SE5 6AH"],
             ["Carys Newton", "25", "Female", "24 South Road", "Labour", "SE7 6LF"],
             ["Lily Page", "21", "Female", "37 Tennyson Close", "Labour", "SE7 9PQ"],
             ["Finn Mack", "35", "Male", "70 Godolphin Close", "Conservative", "SE5 8LP"],
             ["Clyde Knapp", "28", "Male", "12 Silverdale", "Conservative", "SE7 8QX"],
             ["Andrea Lucas", "23", "Female", "6 Telford Mews", "Conservative", "SE6 9WG"],
             ["Athena Hart", "32", "Female", "11 Angel Yard", "Labour", "SE7 6RF"],
             ["Isabel Mason", "34", "Female", "27 Church Road", "Labour", "SE7 7LF"],
             ["Carolyn Snider", "29", "Female", "33 Chatto Road", "Conservative", "SE6 3NG"],
             ["Jacob Thompson", "29", "Male", "5 The Lerburne", "Conservative", "SE7 3FE"]]

MedicalListColumns = ['Patient ID', 'Age', 'Sex', 'Weight (kg)', 'Medical Issue', 'Treatment', 'Postcode']
MedicalListDF = pd.DataFrame(MedicalList, columns=MedicalListColumns)

VoterListColumns = ['name', 'age', 'sex', 'address', 'party', 'postcode']
VoterListDF = pd.DataFrame(VoterList, columns=VoterListColumns)
#datasetDF = VoterListDF
# # Change which dataset is used for the algorithm here
# datasetDF = MedicalListDF
# datasetColumns = MedicalListColumns


# Generates some example tables, used early on in the project
def exampleTables():
    # print(MedicalListDF.groupby(['Patient ID','Age','Sex','Weight (kg)','Medical Issue','Treatment',
    # 'Postcode']).size().reset_index(name='Count'))

    # Voter list

    # Suppressed voter list
    SupVoterList = [["-", 35, "Male", "-", "Conservative", "SE5 6AH"],
                    ["-", 25, "Female", "-", "Labour", "SE7 6LF"],
                    ["-", 21, "Female", "-", "Labour", "SE7 9PQ"],
                    ["-", 39, "Male", "-", "Conservative", "SE5 8LP"],
                    ["-", 28, "Male", "-", "Conservative", "SE7 8QX"],
                    ["-", 23, "Female", "-", "Conservative", "SE6 9WG"],
                    ["-", 32, "Female", "-", "Labour", "SE7 6RF"],
                    ["-", 34, "Female", "-", "Labour", "SE7 7LF"],
                    ["-", 29, "Female", "-", "Conservative", "SE6 3NG"],
                    ["-", 29, "Male", "-", "Conservative", "SE7 3FE"]]

    # Generalized and Suppressed voter list
    GenSupVoterList = [["-", "30<x<=40", "Male", "-", "Conservative", "SE5"],
                       ["-", "20<x<=30", "Female", "-", "Labour", "SE7"],
                       ["-", "20<x<=30", "Female", "-", "Labour", "SE7"],
                       ["-", "30<x<=40", "Male", "-", "Conservative", "SE5"],
                       ["-", "20<x<=30", "Male", "-", "Conservative", "SE7"],
                       ["-", "20<x<=30", "Female", "-", "Conservative", "SE6"],
                       ["-", "30<x<=40", "Female", "-", "Labour", "SE7"],
                       ["-", "30<x<=40", "Female", "-", "Labour", "SE7"],
                       ["-", "20<x<=30", "Female", "-", "Conservative", "SE6"],
                       ["-", "20<x<=30", "Male", "-", "Conservative", "SE7"]]

    # print(VoterListDF.groupby(['Name','Age','Sex','Address','Party','Postcode']).size().reset_index(name='Count'))

    SupVoterListDF = pd.DataFrame(SupVoterList, columns=['Name', 'Age', 'Sex', 'Address', 'Party', 'Postcode'])
    # print(SupVoterListDF.groupby(['Name','Age','Sex','Address','Party','Postcode']).size().reset_index(name='Count'))

    GenSupVoterListDF = pd.DataFrame(GenSupVoterList, columns=['Name', 'Age', 'Sex', 'Address', 'Party', 'Postcode'])
    # print(GenSupVoterListDF.groupby(['Name','Age','Sex','Address','Party','Postcode']).size().reset_index(name='Count'))
    KValue = GenSupVoterListDF.groupby(['Name', 'Age', 'Sex', 'Address', 'Party', 'Postcode']).size().reset_index(
        name='Count')
    # print(KValue)

    GenSupVoterList = [["-", "30<x<=40", "Male", "-", "Conservative", "SE5"],
                       ["-", "20<x<=30", "Female", "-", "Labour", "SE7"],
                       ["-", "20<x<=30", "Female", "-", "Labour", "SE7"],
                       ["-", "30<x<=40", "Male", "-", "Conservative", "SE5"],
                       ["-", "20<x<=30", "Male", "-", "Conservative", "SE7"],
                       ["-", "20<x<=30", "Female", "-", "Conservative", "SE6"],
                       ["-", "30<x<=40", "Female", "-", "Labour", "SE7"],
                       ["-", "30<x<=40", "Female", "-", "Labour", "SE7"],
                       # ["hi", "30<x<=40", "Female", "-", "Labour", "SE7"],
                       ["-", "20<x<=30", "Female", "-", "Conservative", "SE6"],
                       ["-", "20<x<=30", "Male", "-", "Conservative", "SE7"]]

    GenSupVoterListDF = pd.DataFrame(GenSupVoterList, columns=['Name', 'Age', 'Sex', 'Address', 'Party', 'Postcode'])
    # print(GenSupVoterListDF.groupby(['Name','Age','Sex','Address','Party','Postcode']).size().reset_index(name='Count'))
    KValue = GenSupVoterListDF.groupby(['Name', 'Age', 'Sex', 'Address', 'Party', 'Postcode']).size().reset_index(
        name='Count')

    # print(KValue)
    # print("K-Value = ", KValue['Count'].min())



