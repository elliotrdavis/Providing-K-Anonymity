import networkx as nx
from matplotlib import pyplot as plt

from DimensionTables import candidateNodeTable, generateEdges


def incognitoGraph():
    G = nx.Graph()
    candidateNodeTable()
    generateEdges()
    C = candidateNodeTable.newCandidateConnections
    E = generateEdges.edges
    # print(E)
    # print(C)
    # adding just one node:
    # for tuple in E:
    #     for edge in tuple:
    #         edge -= 1
    #         print(edge)
    # print(E)

    for node in C:
        string = ''.join(node)
        G.add_node(string)
    # a list of nodes:
    # G.add_nodes_from(["b", "c"])

    for edge in E:
        edge1 = C[edge[0]-1]
        edge2 = C[edge[1]-1]
        edge1String = ''.join(edge1)
        edge2String = ''.join(edge2)
        #print(edge1String, edge2String)
        edge3 = (edge1String, edge2String)
        G.add_edge(*edge3)

    # G.add_edge(1, 2)
    # edge = ("a", "b")
    # G.add_edge(*edge)
    # # adding a list of edges:
    # G.add_edges_from([("a", "c"), ("c", "d"), ("a", 1), (1, "d"), ("a", 2)])
    nx.draw(G,with_labels=True)
    plt.savefig("Graphs/incognito2attr.png")  # save as png
    plt.show()  # display

    print("Nodes of graph: ")
    print(G.nodes())
    print("Edges of graph: ")
    print(G.edges())
