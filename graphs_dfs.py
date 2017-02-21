# Simple graph API in Python, implementation uses adjacent lists.
# look also here: 
# Classes: Graph, Depth_first_search, Depth_first_paths
# Usage:
# Creating new graph: gr1 = Graph(v) - creates new graph with no edges and v vertices;

# Search object: gr2 = Depth_first_search(graph, vertex) - creates search object,
# gr2.marked_vertex(vertex) - returns true if given vertex is reachable from source(above)

# Path object: gr3 = Depth_first_paths(graph, vertex)- creates a new path object,
# gr3.has_path(vertex) - thee same as above
# gr3.path_to(vertex) - returns path from source vertex (to the given)
from collections import deque


class Graph:
    """Class graph, creates a graph - described by integers - number
    of vertices - V : v0, v1, ..., v(V-1)"""

    def __init__(self, v_in):
        """constructor -  takes number of vertices and creates a graph
         with no edges (E = 0) and an empty adjacent lists of vertices"""
        self.V = v_in
        self.E = 0
        self.adj = []
        for i in range(v_in):
            self.adj.append([])

    def V(self):
        """returns number of vertices"""
        return self.V

    def E(self):
        """returns number of edges"""
        return self.E

    def add_edge(self, v, w):
        """adds an edge to the graph, takes two integers (two vertices)
         and creates an edge v,w - by modifying appropriate adjacent lists """
        self.adj[v].append(w)
        self.adj[w].append(v)
        self.E += 1

    def adj_list(self, v):
        """Takes an integer - a graph vertex and returns the adjacency lists of it"""
        return self.adj[v]

    def __str__(self):
        """to string method, prints the graph"""
        s = str(self.V) + " vertices, " + str(self.E) + " edges\n"
        for v in range(self.V):
            s += str(v) + ": "
            for w in self.adj[v]:
                s += str(w) + " "
            s += "\n"
        return s


class Depth_first_search:
    """class depth forst search, creates an object,
    constructor takes graph and a vertex"""

    def __init__(self, gr_obj, v_obj):
        self.marked = [False] * gr_obj.V
        self.cnt = 0
        self.__dfs(gr_obj, v_obj)

    def __dfs(self, gr, v):
        """private depth first search, proceed recursively,
        mutates marked - marks the all possible to reach
         from given (v) vertices; also mutates cnt - number of visited vert"""
        self.marked[v] = True
        self.cnt += 1
        for w in gr.adj_list(v):
            if self.marked[w] == False:
                self.__dfs(gr, w)

    def marked_vertex(self, w):
        """Takes an integer - a graph vertex and returns True if it's reachable
        from vertex v (source)"""
        return self.marked[w]

    def count(self):
        """returns number of visited verticles
        (from given in the constructor vertex)"""
        return self.cnt


class Depth_first_paths:
    """class depth first paths, solves
    single paths problem: given graph and a vertex (source vertex), find
    a path to another vertex."""

    def __init__(self, gr_obj, v_obj):
        self.marked = [False] * gr_obj.V
        self.edge_to = [0] * gr_obj.V
        self.s = v_obj
        self.__dfs(gr_obj, v_obj)

    def __dfs(self, gr, v):
        """private recursive depth first search, mutates array marked,
        mutates counter (cnt), and creates a path (filling an array edge_to)"""
        self.marked[v] = True
        for w in gr.adj_list(v):
            if self.marked[w] == False:
                self.edge_to[w] = v
                self.__dfs(gr, w)

    def has_path(self, v):
        """Takes an integer - a graph vertex and returns true if there is a path from the source
        vertex to the given, else false"""
        return self.marked[v]

    def path_to(self, v):
        """Takes an integer - a graph vertex and returns path from source[vertex] to it"""
        if self.has_path(v) == False:
            return None
        path = deque()
        x = v
        while x != self.s:
            path.appendleft(x)
            x = self.edge_to[x]
        path.appendleft(self.s)
        return path


cnt = 0


def dfs(gr, v):
    """depth first search as a function"""
    marked = [False] * gr.V

    def df(grap, w):
        """central dfs recursive method"""
        global cnt
        cnt += 1
        marked[w] = True
        for x in grap.adj_list(w):
            if marked[x] == False:
                df(grap, x)

    df(gr, v)
    return marked, cnt


if __name__ == '__main__':
    gr1 = Graph(4)
    print(gr1)
    print(gr1.adj_list(1))
    gr1.add_edge(2, 3)
    print(gr1)
    print(gr1.E)
    print(gr1.adj_list(2))
    print(gr1.adj_list(0))
    print("---------dfs------------")
    gr2 = Graph(6)
    gr2.add_edge(0, 5)
    # gr2.add_edge(2, 4)
    gr2.add_edge(2, 3)
    gr2.add_edge(1, 2)
    gr2.add_edge(0, 1)
    # gr2.add_edge(3, 4)
    gr2.add_edge(3, 5)
    gr2.add_edge(0, 2)
    print(gr2)
    print(dfs(gr2, 0))
    df = dfs(gr2, 0)
    print("---------class Depth_first_search---------")
    df1 = Depth_first_search(gr2, 0)
    print(df1.count())
    print("------------class Depth_first_paths-----------")
    dfp1 = Depth_first_paths(gr2, 0)
    print(dfp1.path_to(3))
