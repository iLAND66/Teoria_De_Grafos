import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()

G.add_edges_from([("A", "B"), ("A", "C"), ("B", "C"), ("B", "D"), ("B", "E"), ("C", "D"), 
("C", "G"), ("D", "E"), ("D", "G"), ("D", "F"), ("E", "F"), ("F", "G"), ("F", "H"), 
("G", "H")])


nodes_for_subgraph = ["A", "B", "C", "D"] 
H = nx.induced_subgraph(G, ["A", "B", "C", "D"])


nx.draw_networkx(G, with_labels=True)
#nx.draw_networkx(H, with_labels=True)

ax = plt.gca()
ax.margins(0.08)
plt.axis("off")
plt.tight_layout()
plt.show()
