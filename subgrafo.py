import networkx as nx
import matplotlib.pyplot as plt
G1 = nx.Graph()
e = [(1, 2), (1, 3), (2, 3),
     (2, 5), (3, 4), (3, 6),
     (3, 8), (4, 5), (5, 6),
     (6, 7), (7, 8), (8, 1)]

G1.add_edges_from(e)

vs = [1, 2, 3, 4, 5]
subgraf = G1.subgraph(vs)


color_vertice = []
for nodo in G1.nodes():
    if nodo is subgraf.nodes():
        color_vertice.append("red")
    else:
        color_vertice.append("blue")
