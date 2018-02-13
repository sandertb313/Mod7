from queue import *
from graph import *
from ex31 import *


def BFS(graph):
    frontier = Queue()
    closed = []
    i = 1
    data = {}

    start = sorted(list(graph.vertices), key=lambda v: v.label)[0]

    frontier.put(start)
    data[start] = [None, None, i]

    print(start.label)
    i = 2

    while not frontier.empty():
        node = frontier.get()
        closed.append(start)
        """adds node neighbours info and adds node to dictionary"""
        if node.neighbours != []:

            for j in node.neighbours:
                if j not in closed:
                    j.label = i
                    print(j.label)
                    data[j] = [node, 1, i]
                    frontier.put(j)
                    closed.append(j)
                    i += 1

    return graph


def connected(graph):
    data = BFS(graph)
    nodes = sorted(list(graph.vertices), key=lambda v: v.label)

    for i in nodes:
        if i not in data:
            return False

    return True


def DFS(graph):
    frontier = []
    closed = []
    i = 1

    start = (sorted(list(graph.vertices), key=lambda v: v.label))[0]

    frontier.append(start)

    while not len(frontier) == 0:
        node = frontier.pop()
        if node not in closed:
            closed.append(node)
            print(str(len(closed)) + " closed")
            node.label = i
            i += 1
            print(str(i) + " label")
            neigbours = node.neighbours
            print(str(len(neigbours)) + "neighbours")
            for n in neigbours:
                if n not in frontier and n not in closed:
                    print("added to frontier" + str(len(frontier)))
                    frontier.append(n)

    return graph


from graph_io import load_graph, save_graph

with open('examplegraph.gr') as f:
    G = load_graph(f)
    F = DFS(G)
    print(F)
    print(connected(G))
    writedotgraph(F)
