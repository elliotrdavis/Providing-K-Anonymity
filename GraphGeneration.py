import networkx as nx

def incognitoGraph():
    G=nx.Graph()

    print(G.nodes())
    print(G.edges())

    print(type(G.nodes()))
    print(type(G.edges()))