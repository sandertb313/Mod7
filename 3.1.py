from graph import *

"""
G = Graph(False, 4)

print(G)
u = Vertex(G)
print(u)
v = Vertex(G)
G.is_adjacent(u, v)
f = Edge(v, u)
G.add_edge(f)
G.is_adjacent(u, v)
print(G)
w = Vertex(G)
G.add_vertex(w)
e = Edge(u, w)
G += e
print(e.tail)
print(e.head)
print(e.other_end(u))
print(w in G.vertices)
print(e in G.edges)
print(u.degree)
print(v in u.neighbours)
x = Vertex(G, 'X')
G += x
print(G)
print(x)
"""

def cr8pathn(n):

    G = Graph(True, n)

    V = sorted(list(G.vertices), key = lambda v : v.label)
    for i in range(0, len(V)- 1):
        f = Edge(V[i], V[i + 1])
        G.add_edge(f)

    return G

def cr8cycle(n):
    G = Graph(True, n)

    V = sorted(list(G.vertices), key=lambda v: v.label)
    for i in range(0, len(V) -1):
        f = Edge(V[i], V[i + 1])
        G.add_edge(f)

    f = Edge(V[len(V) - 1], V[0])
    G.add_edge(f)
    return G

def cr8CgraphDirected(n):

    G = Graph(True, n)
    V = sorted(list(G.vertices), key=lambda v: v.label)

    for i in range(0, len(V) - 1):
        for j in range(0, len(V)-1 ):
            if i != j:
                f = Edge(V[i], V[j])
                G.add_edge(f)

    return G
#print(cr8pathn(6))
#print(cr8cycle(6))
#print(cr8CgraphDirected(6))
G = Graph(True, 6)
H = Graph(True, 3)
V = sorted(list(H.vertices), key=lambda v: v.label)
E = Edge(V[0], V[1])
H.add_edge(E)
print(H)

print(G.__add__(H))