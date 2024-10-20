import networkx as nx
import matplotlib.pyplot as plt

galaxia = nx.Graph()
galaxia.add_edges_from([("a", "b"), ("a", "c"),
                        ("b", "g"),
                        ("c", "g"), ("c", "f"), ("c", "d"),
                        ("d", "f"), ("g", "f"),
                        ("e", "i"), ("e", "p"),
                        ("p", "i"), ("p", "l"),
                        ("h", "i"), ("h", "l"), ("h", "j"),
                        ("j", "l"), ("j", "k"), ("j", "l"),
                        ("k", "m"), ("k", "n"), ("k", "l"),
                        ("m", "n"),
                        ("n", "l"),
                        ("s", "t"), ("s", "u"), ("s", "v"), ("s", "r"),
                        ("t", "u"),
                        ("u", "r"),
                        ("v", "q"),
                        ("q", "r")
                        ])

if(nx.is_connected(galaxia)):
    nx.draw_networkx(galaxia, with_labels=True)
else:
    print(nx.number_connected_components(galaxia))
    estrellas = nx.connected_components(galaxia)
    for i in estrellas:
        print(nx.subgraph(galaxia, i))

nx.draw_networkx(galaxia, with_labels=True)

ax = plt.gca()
ax.margins(0.08)
plt.axis("off")
plt.tight_layout()
plt.show()