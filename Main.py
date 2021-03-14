from KValue import VoterListDF, VoterListColumns, exampleTables
from ImportData import importTable, dimTableToSQL, readSQL
from DimensionTables import candidateNodeTable, generateEdges, dimDFConversion, convertColumns
from GraphGeneration import incognitoGraph


# TODO:
# Ability for n attributes
# Fix up incognito()
#
#
#
#
#
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


# def input():


# Columns: 'Name','Age','Sex','Address','Party','Postcode'
# Dimension table: current requirements
# Name: P0 (name), P1 (-)
# Age: P0 (original), P1 (5 age range), P2 (10 age range), P3 (20 age range)
# Sex: P0 (male/female), P1 (-)
# Address: P0 (address), P1 (-)
# Party: P0 (important info)
# Postcode: P0 (original), P1 (First 3 letters), P2 (First 2 Letters)

def incognito():
    T = VoterListDF
    Q = VoterListColumns
    # set of dim tables = DimensionTables.py
    n = 2  # num of quasi identifier attributes
    C = candidateNodeTable()
    E = generateEdges()
    convertColumns() # creates columns dfs
    queue = []
    # print(C)

    for i in range(1, n):
        S = C
        roots = C[int(generateEdges.roots) - 1]
        # print(roots)
        # define roots - roots is tuple where no edges directed to them
        queue.append(roots)  # keep queue sorted by height
        # generateEdges.edges = sorted(generateEdges.edges, key=lambda element: (element[0], element[1]))
        visited = []
        while queue:
            node = queue[0]
            queue.pop(0)
            # dimDFConversion(node)
            if node not in visited:
                if node in roots:
                    dimDataframe = dimDFConversion(node)  # returns dimDataframe
                    kValue = frequencySet(dimDataframe)  # returns KValue
                    # find k value of current node
                else:
                    dimDataframe = dimDFConversion(node)
                    kValue = frequencySet(dimDataframe)
                    # find k value of parent

                # check if frequencySet is k-anonymous
                print(dimDataframe, )
                if kValue == n:
                    print(dimDataframe, kValue)
                    break;
                else:
                    S.pop(0)
                    if len(S) != 0:
                        queue.append(S[0])
                    else:
                        print(dimDataframe, kValue)
                        break
                    print(kValue)


def frequencySet(dataframe):
    KValue = dataframe.groupby(['Name', 'Age', 'Sex', 'Address', 'Party', 'Postcode']).size().reset_index(name='Count')
    # print("K-Value = ", KValue['Count'].min())
    print(KValue)
    KValue = KValue['Count'].min()
    # print(KValue)
    return KValue


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # exampleTables()
    # print(T, Q)
    # dimensionTables()
    # importTable()
    # dimTableToSQL()
    # readSQL()
    # dimSQL()
    # candidateNodeTable()
    # generateEdges()
    incognito()
    # dimDFConversion()
    # incognitoGraph()
