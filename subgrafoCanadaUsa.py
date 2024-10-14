import matplotlib.pyplot as plt
import networkx as nx

G1 = nx.Graph()
e = [("Alburqueque", "Dallas"), ("Alburqueque", "Kansas City"), ("Alburqueque", "Denver"),
    ("Dallas", "Kansas City"), ("Dallas", "New Orleans"), ("Dallas", "Atlanta"),
    ("New Orleans", "Atlanta"), ("New Orleans", "Miami"),
    ("Miami", "Atlanta"), ("Miami", "Washington"),
    ("Washington", "Atlanta"), ("Washington", "Chicago"), ("Washington", "New York"),
    ("New York", "Chicago"), ("New York", "Montreal"),
    ("Montreal", "Chicago"), ("Montreal", "Duluth"),
    ("Duluth", "Chicago"), ("Duluth", "Kansas City"), ("Duluth", "Winnipeg"), ("Duluth", "Denver"),
    ("Winnipeg", "Helena"),
    ("Helena", "Denver"),
    ("Denver", "Kansas City"),
    ("Kansas City", "Chicago"), ("Kansas City", "Atlanta"),
    ("Atlanta", "Chicago")]

G1.add_edges_from(e)

vs = ["Denver", "Kansas City", "Dallas", "New Orleans", "Miami", "Atlanta", "Washington", "New York", "Montreal", "Chicago", "Duluth", "Winnipeg", "Helena"]
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
