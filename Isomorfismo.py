# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import networkx as nx

G = nx.Graph()
G.add_edges_from([("u1", "u4"), ("u1", "u5"), ("u1", "u6"),
                  ("u2", "u4"), ("u2", "u5"), ("u2", "u6"),
                  ("u3", "u4"), ("u3", "u5"), ("u3", "u6"),
                  ])

G_prima = nx.Graph()
G_prima.add_edges_from([("v1", "v2"), ("v1", "v4"), ("v1", "v6"),
                        ("v2", "v5"), ("v2", "v3"), ("v3", "v6"),
                        ("v3", "v4"), ("v4", "v5"), ("v5", "v6"),
                        ])

GM = nx.isomorphism.GraphMatcher(G, G_prima)
son_isomorfos = GM.is_isomorphic()

if son_isomorfos:
    print("Los grafos G y G' son isomorfos.")
    print("Relación uno a uno de los vértices:")
    for vertice_G, vertice_G_prima in GM.mapping.items():
        print(f"{vertice_G} -> {vertice_G_prima}")
else:
    print("Los grafos G y G' no son isomorfos.")

nx.draw_networkx(G, with_labels= True)
print(G.degree())

nx.draw_networkx(G_prima, with_labels=True)
print(G_prima.degree)
    