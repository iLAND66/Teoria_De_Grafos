import networkx as nx
import matplotlib.pyplot as plt

pollito = nx.DiGraph([("A", "B"), ("A", "C"), ("A", "E"),
                        ("B", "F"),
                        ("C", "E"), ("C", "D"), ("C", "G"), ("C", "K"),
                        ("D", "G"), ("D", "J"), ("D", "K"),
                        ("E", "F"), ("E", "H"),
                        ("F", "H"), ("F", "I"),
                        ("G", "H"), ("G", "I"), ("G", "J"),
                        ("H", "I"),
                        ("I", "J"),
                        ("J", "K")])

#nx.is_tournament(pollito)
nx.tournament.hamiltonian_path(pollito)

nx.draw_networkx(pollito, with_labels=True)

ax = plt.gca()
ax.margins(0.08)
plt.axis("off")
plt.tight_layout()
plt.show()
