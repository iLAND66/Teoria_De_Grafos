import networkx as nx

G1 = nx.Graph()
G1.add_edges_from([("a", "b"), ("b", "c"), ("c", "d"),
                  ("d", "e"), ("e", "a")
                  ])

G2 = nx.Graph()
G2.add_edges_from([("z", "x"), ("z", "r"), ("y", "r"),
                   ("y", "w"), ("x", "w")
                   ])

GM = nx.isomorphism.GraphMatcher(G1, G2)
son_isomorfos = GM.is_isomorphic()

if nx.is_isomorphic(G1, G2) == True:
    print("Si son isomorfos")
    print("Relación uno a uno de los vértices:")
    for vertice_G1, vertice_G2 in GM.mapping.items():
        print(f"{vertice_G1} -> {vertice_G2}")
else:
    print("No son isomorfos")

nx.draw_networkx(G1, with_labels= True)

nx.draw_networkx(G2, with_labels=True)
