from KValue import VoterListDF, VoterListColumns, exampleTables
from ImportData import importTable, dimTableToSQL, readSQL, dimSQL
from DimensionTables import dimensionTables, candidateNodeTable, generateEdges

# TODO:
# Potential for SQL to python at somepoint
# 1) Make up some input and divide input into T, Q and set of dimension tables
# Code dimension tables 
# DONE
#  https://appdividend.com/2020/04/27/python-pandas-how-to-convert-sql-to-dataframe/
# Learn how to make the domain generalization hierarchies of attributes in Q
# Read up on incognito properties
# 2) Start to translate pseudocode into python
# Make graph of generalizations (C and E)
# Graph consists of the all the different combinations of nodes - check rules
# 
# Input
# A table T to be k-anonymised - MedicalList and VoterList
# A set Q of n quasi-identifier attributes
# A set of dimension tables
#
# Output: the set of k-anonymous full-domain generalizations of T
# Nodes (verticies/points)
# Edges (links)


#def input():
    
T = VoterListDF
Q = VoterListColumns
# Columns: 'Name','Age','Sex','Address','Party','Postcode'
# Dimension table: current requirements
# Name: P0 (name), P1 (-)
# Age: P0 (original), P1 (5 age range), P2 (10 age range), P3 (20 age range)
# Sex: P0 (male/female), P1 (-)
# Address: P0 (address), P1 (-)
# Party: P0 (important info)
# Postcode: P0 (original), P1 (First 3 letters), P2 (First 2 Letters)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #exampleTables()
    #print(T, Q)
    #dimensionTables()
    #importTable()
    #dimTableToSQL()
    #readSQL()
    #dimSQL()
    #candidateNodeTable()
    generateEdges()


