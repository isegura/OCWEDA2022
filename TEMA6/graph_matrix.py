# -*- coding: utf-8 -*-

class Graph:
    """This is an implementation for an unweighted and undirected graph
    based on an adjacency matrix"""
    def __init__(self,  list_vertices: list) -> None:
        """This constructor gets a Python list of vertices and creates an empty adjacency matrix  """
        # labels is the set of vertices,  for example,  A,  B,  C,  D...
        self._vertices = list_vertices

        n = len(vertices)
        # we initialize the matrix with 0s
        self._matrix = [[0 for _ in range(n)] for _ in range(n)]

    def _index(self,  v):
        """gets a v1 and returns its index. If v does not exist,
        it shows an error message and returns -1"""
        try:
            index = self._vertices.index(v)
        except ValueError:
            print(v,  ' is not a v1!!!')
            index = -1
        return index

    def add_edge(self,  start: object,   end: object) -> None:
        """gets two vertices and adds an edge from start to end."""
        # first,   we get their indexes
        i,  j = self._index(start),   self._index(end)
        if i == -1 or j == -1:
            return

        # now,   we modify its element in the matrix
        self._matrix[i][j] = 1
        print('[add_edge]: ({},  {}) was added!!!'.format(start,  end))

    def contain_edge(self,  start: object,  end: object) -> int:
        """checks if the edge from start to end exists. If
        the edge exists, then it returns its weight"""
        i,  j = self._index(start),   self._index(end)
        if i == -1 or j == -1:
            return None

        return self._matrix[i][j]

    def remove_edge(self, start: object,  end: object) -> None:
        """removes the edge from start to end. It must
        modify its corresponding element in the matrix to 0."""
        i,  j = self._index(start),   self._index(end)
        if i == -1 or j == -1:
            return

        self._matrix[i][j] = 0

    def __str__(self) -> str:
        """returns the matrix"""
        result = ' '
        # the first row are the vertices
        for v in self._vertices:
            result += '  ' + v

        result += '\n'

        for i, row in enumerate(self._matrix):
            result += self._vertices[i]+' ' + str(row)+'\n'

        return result


if __name__ == '__main__':

    # Now,  we use the implementation to represent this directed and unweighted graph:
    # <img src='https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Directed_graph%2C_cyclic.svg/900px-Directed_graph%2C_cyclic.svg.png' width='35%'/>
    
    vertices = ['A', 'B', 'C', 'D', 'E', 'F']

    g = Graph(vertices)

    # Now,  we add the edges
    g.add_edge('P', 'B')  # A->B
    g.add_edge('A', 'B')  # A->B
    g.add_edge('B', 'C')  # B->C
    g.add_edge('C', 'E')  # C->E
    g.add_edge('D', 'B')  # D->B
    g.add_edge('E', 'D')  # E->D
    g.add_edge('E', 'F')  # E->D
    print('contain_edge(A, E) = ', g.contain_edge('A', 'E'))
    print('contain_edge(D, B) = ', g.contain_edge('D', 'B'))

    print(g)

    g.remove_edge('E', 'D')
    print(g)


