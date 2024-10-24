import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.euler import eulerian_path, eulerian_circuit

G = nx.Graph()
G.add_edges_from([("A", "B"), ("A", "C"),
                  ("B", "D"), ("D", "C"), ])

a = nx.Graph()
a.add_edges_from([(1, 2), (1, 3), (3, 2)])

b = nx.Graph()
b.add_edges_from([(4, 5)])

c = nx.MultiGraph()
c.add_edges_from([(6, 7), (6, 7)])

d = nx.Graph()
d.add_edges_from([(8, 9), (8, 10), (10, 9)])

e = nx.Graph()
e.add_edges_from([(11, 12), (11, 13), (11, 14),
                  (13, 12), (13, 14)])

f = nx.Graph()
f.add_edges_from([(15, 16), (15, 19), (16, 17),
                  (16, 18), (16, 19), (17, 18)])

def euleriano(grafo):
    if(nx.is_eulerian(grafo)):
        print(f"El grafo {grafo} es euleriano")
        eulerian_circuit = list(nx.eulerian_circuit(grafo))
        print(f"el circuito euleriano es: {eulerian_circuit}")
        eulerian_path = list(nx.eulerian_path(grafo))
        print(f"el camino euleriano es: {eulerian_path}")
    else:
        print("El grafo no es euleriano")
    nx.draw_networkx(grafo, with_labels=True)

euleriano(G)
euleriano(a)
euleriano(b)
euleriano(c)
euleriano(d)
euleriano(e)
euleriano(f)

ax = plt.gca()
ax.margins(0.008)
plt.axis("off")
plt.tight_layout()
plt.show()