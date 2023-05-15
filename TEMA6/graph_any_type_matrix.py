# -*- coding: utf-8 -*-

class GraphMatrix:
    """This class is an implementation for a graph using a matrix of adjacency.
    It allows ys to represent any type of graph:
    weighted, unweighted, directed and undirected graphs"""

    def __init__(self, list_vertices: list, directed=False) -> None:
        """ gets a list of vertices (which could be strings or numbers),
        and a boolean indicating if the graph is directed (True) or not.
        The default value is False (undirected)."""
        self._vertices = list_vertices
        self._directed = directed
        n = len(vertices)
        # we initialize the matrix with 0s
        self._matrix = [[0 for _ in range(n)] for _ in range(n)]

    def _index(self, v: object) -> int:
        """ gets a v1 and returns its index.
        If v does not exist, it shows an error message and returns -1"""
        try:
            index = self._vertices.index(v)
        except ValueError:
            print(v, ' is not a v1!!!')
            index = -1
        return index

    def add_edge(self, start: object, end: object, w: int = 1) -> None:
        """gets two vertices and adds an edge from start to end.
        The parameter w is the weight of the edge (start, end).
        By default, its value is 1"""
        # first, we get their indexes
        i, j = self._index(start), self._index(end)
        if i == -1 or j == -1:
            return
        # now, we modify its element in the matrix
        self._matrix[i][j] = w
        if not self._directed:
            self._matrix[j][i] = w

        # print('[add_edge]: ({},{}) was added!!!'.format(start, end))

    def contain_edge(self, start: object, end: object) -> int:
        """checks if the edge from start to end exists."""
        i, j = self._index(start), self._index(end)
        if i == -1 or j == -1:
            return None

        return self._matrix[i][j]

    def remove_edge(self, start: object, end: object) -> None:
        """removes the edge from start to end. It must
        modify its corresponding element in the matrix to 0."""
        i, j = self._index(start), self._index(end)
        if i == -1 or j == -1:
            return None

        self._matrix[i][j] = 0
        if not self._directed:
            self._matrix[j][i] = 0

    def get_adjacent_vertices(self, vertex):
        """ returns a Python list that contains the adjacent vertices
        of v1. The list only contains the vertices"""
        index = self._index(vertex)
        if index == -1:
            # v1 does not exist
            return None
        lst_adjacents = []
        for j in range(len(self._vertices)):
            if self._matrix[index][j] != 0:
                lst_adjacents.append(self._vertices[j])
        return lst_adjacents

    def get_origins(self, vertex):
        """ returns a Python list that contains those vertices that have
         and edge to v1. The list only contains the vertices"""
        index = self._index(vertex)
        if index == -1:
            # v1 does not exist
            return None
        lst_origins = []
        for j in range(len(self._vertices)):
            if self._matrix[j][index] != 0:
                lst_origins.append(self._vertices[j])
        return lst_origins

    def __str__(self) -> str:
        """returns a string containing the matrix"""
        result = ' '
        # the first row are the vertices
        for vertex in self._vertices:
            result += '  ' + str(vertex)

        result += '\n'

        for i, row in enumerate(self._matrix):
            result += str(self._vertices[i]) + ' ' + str(row) + '\n'

        return result


if __name__ == '__main__':
    # Now, we use the class to represent
    # this directed and unweighted graph:
    # <img src='https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Directed_graph%2C_cyclic.svg/900px-Directed_graph%2C_cyclic.svg.png' width='35%'/>

    vertices = ['A', 'B', 'C', 'D', 'E', 'F']

    g = GraphMatrix(vertices)

    # Now, we add the edges
    g.add_edge('A', 'B')  # A->B
    g.add_edge('B', 'C')  # B->C
    g.add_edge('C', 'E')  # C->E
    g.add_edge('D', 'B')  # D->B
    g.add_edge('E', 'D')  # E->D
    g.add_edge('E', 'F')  # E->D

    print(g)
    for c in g._vertices:
        print("adjacent vertices of {}:{}".format(c, g.get_adjacent_vertices(c)))
        print("origins for {}:{}".format(c, g.get_origins(c)))
        print()
    # We use the class to represent
    # an undirected graph without weights :
    # <img src='https://computersciencesource.files.wordpress.com/2010/05/dfs_1.png' width='35%'/>
    #

    vertices = ['A', 'B', 'C', 'D', 'E']
    g = GraphMatrix(vertices, False)
    g.add_edge('A', 'B')  # A:0, B:1
    g.add_edge('A', 'C')  # A:0, C:2
    g.add_edge('A', 'E')  # A:0, E:5
    g.add_edge('B', 'D')  # B:1, D:4
    g.add_edge('B', 'E')  # C:2, B:1
    print(g)

    for c in g._vertices:
        print("adjacent vertices of {}:{}".format(c, g.get_adjacent_vertices(c)))
        print("origins for {}:{}".format(c, g.get_origins(c)))
        print()
    print()
    # Now, we use the class to represent
    # a directed and weighted graph:
    # <img src='https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/CPT-Graphs-directed-weighted-ex1.svg/722px-CPT-Graphs-directed-weighted-ex1.svg.png' width='25%'/>

    vertices = ['A', 'B', 'C', 'D', 'E']

    g = GraphMatrix(vertices)

    # Now, we add the edges
    g.add_edge('A', 'C', 12)  # A->(12)C
    g.add_edge('A', 'D', 60)  # A->(60)D
    g.add_edge('B', 'A', 10)  # B->(10)A
    g.add_edge('C', 'B', 20)  # C->(20)B
    g.add_edge('C', 'D', 32)  # C->(32)D
    g.add_edge('E', 'A', 7)  # E->(7)A
    print(g)

    print('containEdge(C,B)', g.contain_edge('C', 'B'))
    print()
    g.remove_edge('C', 'B')
    print("after removing C->B")
    print(g)

    for c in g._vertices:
        print("adjacent vertices of {}:{}".format(c, g.get_adjacent_vertices(c)))
        print("origins for {}:{}".format(c, g.get_origins(c)))
        print()
