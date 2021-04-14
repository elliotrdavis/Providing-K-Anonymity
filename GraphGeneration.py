"""
GraphGeneration.py
Author: Elliot Davis

This file generates a graph representing the generalization lattice for the respective dataset

"""

import networkx as nx
from matplotlib import pyplot as plt
from LatticeGeneration import generateLatticeNodes, generateLatticeEdges


def latticeGraph():
    G = nx.Graph()

    C = generateLatticeNodes()
    E = generateLatticeEdges()

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

    nx.draw(G,with_labels=False)
    plt.savefig("Graphs/incognito2attr.png")  # save as png
    plt.show()  # display
