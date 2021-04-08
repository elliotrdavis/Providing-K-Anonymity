from KValue import VoterListDF, VoterListColumns
from DimensionTables import candidateNodeTable, generateEdges, dimDFConversion, convertColumns
from GraphGeneration import incognitoGraph


# TODO:
# Change copy dimDFConversion to do 2 attribute tables
# Search through each graph, calculate frequency sets
# New function GraphGeneration to generate combination of all 2 attribute tables
#
# Output: the set of k-anonymous full-domain generalizations of T
# Nodes (verticies/points)
# Edges (links)

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
    n = len(VoterListColumns)  # num of quasi identifier attributes
    C = candidateNodeTable()
    E = generateEdges()
    convertColumns()  # creates columns dfs
    queue = []
    # print(C)

    # for each 2-attribute generalization graphs
    for i in range(1, n):
        S = C
        roots = C[int(generateEdges.roots) - 1]
        # define roots - roots is tuple where no edges directed to them
        queue.append(roots)  # keep queue sorted by height
        # generateEdges.edges = sorted(generateEdges.edges, key=lambda element: (element[0], element[1]))
        visited = []

        # while queue is not empty
        while queue:
            node = queue[0]
            queue.pop(0)

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
                    break
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
    incognito()
