# -*- coding: utf-8 -*-

class AdjacentVertex:
    """ This class allows us to represent a tuple
    with an adjacent v1
    and the weight associated (by default None, for non-unweighted graphs)"""
    def __init__(self, vertex: object, weight: int = 1) -> None:
        self.vertex = vertex
        self.weight = weight

    def __str__(self) -> str:
        """ returns the tuple (v1, weight)"""
        if self.weight is not None:
            return '(' + str(self.vertex) + ',' + str(self.weight) + ')'
        else:
            return str(self.vertex)


class Graph:
    def __init__(self, vertices: list, directed: bool = True) -> None:
        """ We use a dictionary to represent the graph
        the dictionary's keys are the vertices
        The value associated for a given key will be the list of their neighbours.
        Initially, the list of neighbours is empty"""
        self._vertices = {}
        for v in vertices:
            self._vertices[v] = []
        self._directed = directed

    def add_vertex(self, vertex: str) -> None:
        if vertex in self._vertices.keys():
            print(vertex, ' already exists!')
            return
        self._vertices[vertex] = []

    def add_edge(self, start: object, end: object, weight: int = 1) -> None:
        if start not in self._vertices.keys():
            print(start, ' does not exist!')
            return
        if end not in self._vertices.keys():
            print(end, ' does not exist!')
            return

        # adds to the end of the list of neighbours for start
        self._vertices[start].append(AdjacentVertex(end, weight))

        if not self._directed:
            # adds to the end of the list of neighbors for end
            self._vertices[end].append(AdjacentVertex(start, weight))

    def contain_edge(self, start: object, end: object) -> int:
        """ checks if the edge (start, end) exits. It does
        not exist return 0, eoc returns its weight or 1 (for unweighted graphs)"""
        if start not in self._vertices.keys():
            print(start, ' does not exist!')
            return 0
        if end not in self._vertices.keys():
            print(end, ' does not exist!')
            return 0

        # we search the AdjacentVertex whose v is equal to end
        for adj in self._vertices[start]:
            if adj.vertex == end:
                return adj.weight

        return 0  # does not exist

    def remove_edge(self, start: object, end: object):
        """ removes the edge (start, end)"""
        if start not in self._vertices.keys():
            print(start, ' does not exist!')
            return
        if end not in self._vertices.keys():
            print(end, ' does not exist!')
            return

        # we must look for the adjacent AdjacentVertex (neighbour)  whose v1 is end, and then remove it
        for adj in self._vertices[start]:
            if adj.vertex == end:
                self._vertices[start].remove(adj)
        if not self._directed:
            # we must also look for the AdjacentVertex (neighbour)  whose v1 is end, and then remove it
            for adj in self._vertices[end]:
                if adj.vertex == start:
                    self._vertices[end].remove(adj)

    def __str__(self) -> str:
        """ returns a string containing the graph"""
        result = ''
        for v in self._vertices:
            result += '\n'+str(v)+':'
            for adj in self._vertices[v]:
                result += str(adj)+"  "
        return result

    def get_adjacent_vertices(self, vertex: object) -> list:
        """ returns a Python list containing the adjacent
        vertices of v1. The list only contains the vertices"""
        if vertex not in self._vertices.keys():
            print(vertex, ' does not exist!')
            return None
        lst_adjacent_vertices = []
        for adj in self._vertices[vertex]:
            u = adj.vertex
            lst_adjacent_vertices.append(u)
        return lst_adjacent_vertices

    def get_origins(self, vertex: object) -> list:
        """ returns a Python list containing those vertices that have
        an edge to v1. The list is formed with objects of AdjacentVertex"""
        if vertex not in self._vertices.keys():
            print(vertex, ' does not exist!')
            return None
        lst_origins = []
        for v in self._vertices:
            for adj in self._vertices[v]:
                u = adj.vertex
                if vertex == u:
                    lst_origins.append(v)
                    break
        return lst_origins


if __name__ == '__main__':
    # We use the class to represent an undirected graph without weights :
    # <img src='https://computersciencesource.files.wordpress.com/2010/05/dfs_1.png' width='35%'/>

    labels = ['A', 'B', 'C', 'D', 'E']
    g = Graph(labels, False)
    g.add_edge('A', 'B')  # A:0,  B:1
    g.add_edge('A', 'C')  # A:0,  C:2
    g.add_edge('A', 'E')  # A:0,  E:5
    g.add_edge('B', 'D')  # B:1,  D:4
    g.add_edge('B', 'E')  # C:2,  B:1
    # g.add_edge('A', 'H', 8)

    print(g)
    for c in labels:
        print("adjacent vertices of {} : {} ".format(c, str(g.get_adjacent_vertices(c))))
        print("origins for {} : {} ".format(c, str(g.get_origins(c))))
        print()

    # Now,  we use the implementation to represent this graph:
    # <img src='https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/CPT-Graphs-directed-weighted-ex1.svg/722px-CPT-Graphs-directed-weighted-ex1.svg.png' width='25%'/>

    labels = ['A', 'B', 'C', 'D', 'E']
    g = Graph(labels)

    # Now, we add the edges
    g.add_edge('A', 'C', 12)  # A->(12)C
    g.add_edge('A', 'D', 60)  # A->(60)D
    g.add_edge('B', 'A', 10)  # B->(10)A
    g.add_edge('C', 'B', 20)  # C->(20)B
    g.add_edge('C', 'D', 32)  # C->(32)D
    g.add_edge('E', 'A', 7)   # E->(7)A

    print(g)
    print(g.contain_edge('C', 'B'))
    print(g.contain_edge('B', 'C'))
    g.remove_edge('C', 'B')
    print(g)
    g.remove_edge('A', 'D')
    print(g)
    for c in g._vertices:
        print("adjacent vertices of {} : {} ".format(c, str(g.get_adjacent_vertices(c))))
        print("origins for {} : {} ".format(c, str(g.get_origins(c))))
        print()
