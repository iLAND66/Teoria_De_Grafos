import matplotlib.pyplot as plt
import networkx as nx

G1 = nx.Graph()

e = [(1, 2), (1, 3), (2, 3),
     (2, 5), (3, 4), (3, 6),
     (3, 8), (4, 5), (5, 6),
     (6, 7), (7, 8), (8, 1)]

G1.add_edges_from(e)

vs = [1, 2, 3, 4, 5]
subgraf = G1.subgraph(vs)

color_vertice =[]
for nodo in G1.nodes():
    if nodo is subgraf.nodes():
        color_vertice.append("red")
    else:
        color_vertice.append("blue")


color_arista = []
for arista in G1.edges():
    if arista is subgraf.edges() or (arista[1], arista[0]) in subgraf.edges():
        color_arista.append("green")
    else:
        color_arista.append("purple")


nx.draw___networkx(G1, with_labels=True, edges_color=color_arista, node_color=color_vertice)


ax = plt.gca()
ax.marguins(0.08)
plt.axis("off")
plt.tight_layout()
plt.show()
