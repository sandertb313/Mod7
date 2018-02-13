from graph import *
from graph_io import *
from mygraphs import *
"""
G = Graph(True, 4)

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
print("YOLO")
print(v in u.neighbours)
print(u.neighbours)
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

"""
#print(cr8pathn(6))
#print(cr8cycle(6))
#print(cr8CgraphDirected(6))
G = Graph(False, 6)
H = Graph(False, 3)
V = sorted(list(H.vertices), key=lambda v: v.label)
E = Edge(V[0], V[1])


H.add_edge(E)
print(V[0] in V[1].neighbours)
print(H)

print(G.__add__(H))
"""

def ex2(file, fileout):
    from graph_io import load_graph, save_graph
    with open(file) as f:
        G = load_graph(f)


        f = Vertex(G)
        G.add_vertex(f)

        g = Vertex(G)
        G.add_vertex(g)

        h = Vertex(G)
        G.add_vertex(h)

        G.add_edge(Edge(g, h))
        G.add_edge(Edge(f, g))

    with open(fileout, 'w') as f:
        save_graph(G, f)

def complement(filein, fileout, writedot):
    from graph_io import load_graph, save_graph
    with open(filein) as f:

        G = load_graph(f)

        Dict = {}

        graph = Graph(True)

        """Creates vertices and puts them in dictionary"""
        V = sorted(list(G.vertices), key=lambda v: v.label)
        for i in V:
            v = Vertex(graph)
            graph.add_vertex(v)
            Dict[i] = v

        """Checks if an edge existed in old graph, if it didnt exist an edge is created"""
        for key, value in Dict.items():
            for key1, value1 in Dict.items():
                if not key in key1.neighbours and key != key1:
                    e = Edge(value1, value)
                    graph.add_edge(e)


    with open(fileout, 'w') as f:
        save_graph(graph, f)


def writedotfile(file):

    from graph_io import load_graph, save_graph

    print("loading")
    with open(file) as f:
        G = load_graph(f)

    print("writing")
    with open('mygraph.dot', 'w') as j:
        write_dot(G, j)

def writedotgraph(graph):
    print("writing")
    with open('mygraph.dot', 'w') as j:
        write_dot(graph, j)

#complement('examplegraph.gr', 'examplegraph3.gr')

#writedot('examplegraph.gr')


G = Graph(True, 4)

print(G)
u = Vertex(G)
print(u)
v = Vertex(G)
G.is_adjacent(u, v)
f = Edge(v, u)
G.add_edge(f)
G.is_adjacent(u, v)
print(G)
G.del_edge(f)
print(G)
