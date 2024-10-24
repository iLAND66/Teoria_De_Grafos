import networkx as nx
import matplotlib.pyplot as plt

pollito = nx.Graph()
pollito.add_edges_from([(1, 2), (1, 3), (1, 5),
                        (2, 6),
                        (3, 5), (3, 4), (3, 7), (3, 11),
                        (4, 7), (4, 10), (4, 11),
                        (5, 6), (5, 8),
                        (6, 8), (6, 9),
                        (7, 8), (7, 9), (7, 10),
                        (8, 9),
                        (9, 10),
                        (10, 11)])

nx.tournament.hamiltonian_path(pollito)

nx.draw_networkx(pollito, with_labels=True)

ax = plt.gca()
ax.margins(0.08)
plt.axis("off")
plt.tight_layout()
plt.show()