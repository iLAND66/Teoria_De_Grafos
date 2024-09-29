import networkx as nx

G1 = nx.Graph()
G1.add_edges_from([("a", "b"), ("a", "c"), 
                  ("b", "d"), ("b", "f"), ("b", "c"),
                  ("c", "d"), ("c", "e"),
                  ("d", "f"), ("d", "e"), ("d", "g"), ("d", "h"),
                  ("e", "i"), ("e", "h"),
                  ("f", "g"),
                  ("g", "h"), ("g", "j"),
                  ("h", "i"),
                  ("j", "i"),
                  ])

G2 = nx.Graph()
G2.add_edges_from([("1", "2"), ("1", "3"), ("1", "4"), ("1", "5"), ("1", "6"),
                   ("2", "3"), ("2", "4"), ("2", "5"), ("2", "6"),
                   ("3", "4"), ("3", "5"), ("3", "6"),
                   ("4", "5"), ("4", "6"),
                   ("5", "6"),
                   ])

G3 = nx.Graph()
G3.add_edges_from([("a", "b"), ("a", "c"),
                   ("b", "d"), ("b", "e"),
                   ("c", "d"),
                   ("d", "f"), ("d", "g"),
                   ("e", "f"),
                   ("f", "i"), ("f", "h"),
                   ("g", "h"),
                   ("h", "j"),
                   ("j", "i"),
                   ])
'''isomorfismo entre G1 & G2'''
GM1y2 = nx.isomorphism.GraphMatcher(G1, G2)
son_isomorfos = GM1y2.is_isomorphic()

if son_isomorfos:
    print("Los grafos G1 y G2 son isomorfos.")
    print("Relación uno a uno de los vértices:")
    for vertice_G1, vertice_G2 in GM1y2.mapping.items():
        print(f"{vertice_G1} -> {vertice_G2}")
else:
    print("Los grafos G1 y G2 no son isomorfos.")
    

'''isomorfismo entre G1 & G3'''
GM1y3 = nx.isomorphism.GraphMatcher(G1, G2)
son_isomorfos = GM1y3.is_isomorphic()

if son_isomorfos:
    print("Los grafos G1 y G3 son isomorfos.")
    print("Relación uno a uno de los vértices:")
    for vertice_G1, vertice_G3 in GM1y3.mapping.items():
        print(f"{vertice_G1} -> {vertice_G3}")
else:
    print("Los grafos G1 y G3 no son isomorfos.")


'''isomorfismo entre G2 & G3'''
GM2y3 = nx.isomorphism.GraphMatcher(G2, G3)
son_isomorfos = GM2y3.is_isomorphic()

if son_isomorfos:
    print("Los grafos G2 y G3 son isomorfos.")
    print("Relación uno a uno de los vértices:")
    for vertice_G2, vertice_G3 in GM2y3.mapping.items():
        print(f"{vertice_G2} -> {vertice_G3}")
else:
    print("Los grafos G2 y G3 no son isomorfos.")


'''Bipartitas G1, G2 & G3'''
print("G1 es bipartita") if nx.is_bipartite(G1) else print("G1 no es bipartita")

print("G2 es bipartita") if nx.is_bipartite(G2) else print("G2 no es bipartita")

print("G3 es bipartita") if nx.is_bipartite(G3) else print("G3 no es bipartita")


'''Grafo completo'''
grafoSeis = nx.complete_graph(6, create_using=None)


nx.draw_networkx(G1, with_labels= True)

nx.draw_networkx(G2, with_labels=True)

nx.draw_networkx(G3, with_labels=True)

nx.draw_networkx(grafoSeis, with_labels=True)
    