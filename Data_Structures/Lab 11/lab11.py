class EdgeSet:
    def __init__(self, V = None, E = None):
        if V is not None:
            self.V = V
        else:
            self.V = set()
        if E is not None:
            self.E = E
        else:
            self.E = set()
        return

    def add_vertex(self, v):
        if v in self.V:
            return
        self.V.add(v)
        return

    def remove_vertex(self, v):
        if v not in self.V:
            raise KeyError("Vertex is not in graph.")
        self.V.remove(v)
        return
    def add_edge(self, e):
        if e in self.E:
            return
        self.E.add(e)
        return
    def remove_edge(self, e):
        if e not in self.E:
            raise KeyError("Edge is not in graph.")
        self.E.remove(e)

    def neighbors(self, v):
        neighbors = set()
        for e in self.E:
            if e[0] == v:
                neighbors.add(e[1])
        return neighbors


class AdjacencySet:
    def __init__(self, V = None, E = None):
        if V is not None:
            self.V = V
        else:
            self.V = set()
        if E is not None:
            self.nbrs = dict()
            for e in E:
                if e[0] in self.nbrs:
                    if e[1] in self.nbrs[e[0]]:
                        pass
                    else:
                        self.nbrs[e[0]].add(e[1])
                else:
                    self.nbrs[e[0]] = set()
                    self.nbrs[e[0]].add(e[1])
        else:
            self.nbrs = dict()
        return

    def add_vertex(self, v):
        if v in self.V:
            return
        self.V.add(v)
        self.nbrs[v] = set()
        return

    def remove_vertex(self, v):

        if v not in self.V:
            raise KeyError("Vertex is not in graph.")
        del self.nbrs[v]
        return

    def add_edge(self, e):
        if e[0] in self.nbrs:
            if e[1] in self.nbrs[e[0]]:
                pass
            else:
                self.nbrs[e[0]].add(e[1])
        else:
            self.nbrs[e[0]] = set()
            self.nbrs[e[0]].add(e[1])
        return

    def remove_edge(self, e):
        if e[0] in self.nbrs:
            if e[1] in self.nbrs[e[0]]:
                if len(self.nbrs[e[0]]) == 1:
                    del self.nbrs[e[0]]
                else:
                    self.nbrs[e[0]].remove(e[1])
            else:
                raise KeyError("Edge is not in graph.")
        else:
            raise KeyError("Edge is not in graph.")

    def neighbors(self, v):
        return self.nbrs[v]
class Graph_ES(EdgeSet):
    pass

class Graph_AS(AdjacencySet):
    pass


if __name__ == '__main__':
    # Store the following graph:
    #   1--4--5
    #   |\ | /|
    #   | \|/ |
    #   2--3--6

    vs = {1,2,3,4,5,6}
    es = {(1,2), (1,3), (1,4),               # 1s neighbors: {2, 3, 4}
          (2,1), (2,3),                      # 2s neighbors: {1, 3}
          (3,1), (3,2), (3,4), (3,5), (3,6), # 3s neighbors: {1, 2, 4, 5, 6}
          (4,1), (4,3), (4,5),               # 4s neighbors: {1, 3, 5}
          (5,3), (5,4), (5,6),               # 5s neighbors: {3, 4, 6}
          (6,3), (6,5)}                      # 6s neighbors: {3, 5}

    ########### EdgeSet #############
    print("************ EDGESET TESTS ************ ")
    f = Graph_ES(vs, es)
    print("Checking neighbors Test: ", end="")
    assert (f.neighbors(5) == {3, 4, 6})
    assert (f.neighbors(3) == {1, 2, 4, 5, 6})
    print("PASSED!")

    print("Adding vertex Test: ", end="")
    print(vs)
    f.add_vertex("A")
    print(vs)
    f.add_edge(("A", 5))
    assert(f.neighbors("A") == {5})
    print("PASSED!")


    # f.remove_edge(("A", 6))
    print("Removing non-existing edge Test: ", end="")
    try:
        f.remove_edge(("A", 6))
    except KeyError:
        print("PASSED!")

    ########### AdjacencySet #############
    print()
    vs = {1, 2, 3, 4, 5, 6}
    es = {(1, 2), (1, 3), (1, 4),  # 1s neighbors: {2, 3, 4}
          (2, 1), (2, 3),  # 2s neighbors: {1, 3}
          (3, 1), (3, 2), (3, 4), (3, 5), (3, 6),  # 3s neighbors: {1, 2, 4, 5, 6}
          (4, 1), (4, 3), (4, 5),  # 4s neighbors: {1, 3, 5}
          (5, 3), (5, 4), (5, 6),  # 5s neighbors: {3, 4, 6}
          (6, 3), (6, 5)}  # 6s neighbors: {3, 5}
    print("************ ADJACENCYSET TESTS ************ ")
    g = Graph_AS(vs, es)

    print("Checking vertices Test: ", end="")
    assert (g.V == {1, 2, 3, 4, 5, 6})
    print("PASSED!")

    print("Checking neighbors Test: ", end="")
    assert (g.nbrs[4] == {1, 3, 5})
    print("PASSED!")

    print("Newly added vertex with edges Test: ", end="")
    g.add_vertex(10)
    for e in range (2,4):
        g.add_edge((10, e))

    assert (g.nbrs[10] == {2, 3})
    print("PASSED!")

    print("Removing edge Test: ", end="")
    g.remove_edge((5,6))
    g.remove_edge((6,5))
    assert (g.nbrs[5] == {3, 4})
    assert (g.nbrs[6] == {3})
    print("PASSED!")
