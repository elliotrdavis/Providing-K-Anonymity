import networkx as nx
from matplotlib import pyplot as plt

from DimensionTables import candidateNodeTable, generateEdges


def incognitoGraph():
    G = nx.Graph()

    C = candidateNodeTable()
    E = generateEdges()

    for node in C:
        string = ''.join(node)
        G.add_node(string)

    for edge in E:
        edge1 = C[edge[0]-1]
        edge2 = C[edge[1]-1]
        edge1String = ''.join(edge1)
        edge2String = ''.join(edge2)
        edge3 = (edge1String, edge2String)
        G.add_edge(*edge3)

    nx.draw(G,with_labels=True)
    plt.savefig("Graphs/incognito2attr.png")  # save as png
    plt.show()  # display
