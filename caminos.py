from importlib.util import source_hash

import networkx as nx
import matplotlib.pyplot as plt

grafito = nx.Graph()
e = [("A", "B"), ("A", "C"),
     ("B", "E"), ("B", "F"),
     ("C", "D"), ("C", "G"), ("C", "Z"),
     ("D", "E"), ("D", "G"),
     ("E", "F"), ("E", "J"), ("E", "N"),
     ("G", "N"), ("G", "W"), ("G", "Z"),
     ("J", "W"),
     ("N", "W")]
grafito.add_edges_from(e)

W = ["A", "B", "C"]
W = ["A", "E", "G"]

W1 = ["A", "C", "D", "E", "J"]
W2 = ["A", "F", "J", "W"]

print(nx.is_simple_path(grafito, W1))
print(nx.is_simple_path(grafito, W2))

caminos = nx.all_simple_paths(grafito, source="D", target="B")
for i in caminos:
    print(i)

nx.draw_networkx(grafito, with_labels=True)

ax = plt.gca()
ax.margins(0.08)
plt.axis("off")
plt.tight_layout()
plt.show()