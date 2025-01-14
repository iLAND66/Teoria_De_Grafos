import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()
G.add_edges_from([
    ("Montreal", "New York", {"weight": 1}), ("Montreal", "Chicago", {"weight": 3}), ("Montreal", "Duluth", {"weight": 3}), ("New York", "Chicago", {"weight": 3}),
    ("New York", "Washington", {"weight": 1}), ("Washington", "Chicago", {"weight": 3}), ("Washington", "Atlanta", {"weight": 2}), ("Washington", "Miami", {"weight": 4}),
    ("Miami", "Atlanta", {"weight": 2}), ("Miami", "New Orleans", {"weight": 3}), ("New Orleans", "Atlanta", {"weight": 1}), ("New Orleans", "Dalas", {"weight": 2}),
    ("Dalas", "Atlanta", {"weight": 3}), ("Dalas", "Kansas City", {"weight": 1}), ("Dalas", "Alburquerque", {"weight": 3}), ("Alburquerque", "Kansas City", {"weight": 3}),
    ("Alburquerque", "Denver", {"weight": 1}), ("Denver", "Kansas City", {"weight": 2}), ("Denver", "Duluth", {"weight": 4}), ("Denver", "Helena", {"weight": 2}),
    ("Helena", "Winnipeg", {"weight": 3}), ("Winnipeg", "Duluth", {"weight": 1}), ("Duluth", "Chicago", {"weight": 1}), ("Duluth", "Kansas City", {"weight": 2}),
    ("Chicago", "Kansas City", {"weight": 1}), ("Chicago", "Atlanta", {"weight": 2}), ("Kansas City", "Atlanta", {"weight": 3})
    ])

def calcular_distancia_mas_corta(G, origen, destino):
    return nx.shortest_path_length(G, source=origen, target=destino, weight="weight")

aem = nx.minimum_spanning_tree(G, weight='weight')

print("Árbol de expansión mínima:")
for edge in aem.edges(data=True):
    print(edge)

if __name__ == "__main__":
    distancia = calcular_distancia_mas_corta(G, "Montreal", "Denver")
    print(f"La distancia más corta entre Montreal y Denver es: {distancia}")
    nx.draw_networkx(G, with_labels=True)
    ax = plt.gca()
    ax.margins(0.08)
    plt.axis("off")
    plt.tight_layout()
    plt.show()
