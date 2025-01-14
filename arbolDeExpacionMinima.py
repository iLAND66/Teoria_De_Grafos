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

mst = nx.minimum_spanning_tree(G, weight='weight')

print("Árbol de expansión mínima:")
for edge in mst.edges(data=True):
    print(edge)

# Visualizar el grafo original
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
pos = nx.spring_layout(G, seed=42)  # Posiciones fijas para comparación
nx.draw_networkx(G, pos, with_labels=True, node_size=500, font_size=10)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title("Grafo original")
plt.axis("off")

# Visualizar el MST
plt.subplot(1, 2, 2)
nx.draw_networkx(mst, pos, with_labels=True, node_size=500, font_size=10, edge_color='purple')
mst_labels = nx.get_edge_attributes(mst, 'weight')
nx.draw_networkx_edge_labels(mst, pos, edge_labels=mst_labels)
plt.title("Árbol de expansión mínima (MST)")
plt.axis("off")

plt.tight_layout()
plt.show()
