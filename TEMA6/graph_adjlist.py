# -*- coding: utf-8 -*-

from TEMA2.dlist import DList


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
    """This class is an implementation for any type of graph,
     based on adjacency lists."""

    def __init__(self, vertices: list, directed: bool = True) -> None:
        """This constructor gets an array saving the vertices. The class has the
        following attributes:
        _vertices: is a Python list to save the vertices
        _adjacent_list: a Python list of doubly linked list.
        Given a v1 v, it has an index in _vertices, for example, i.
        Then, its list of adjacent v1 is saved into _adjacent_list[i], which is a
        doubly linked list saving objects of the AdjacentVertex class.
        """
        self._vertices = vertices
        self._adjacent_list = []
        for _ in self._vertices:
            self._adjacent_list.append(DList())

        self._directed = directed

    def add_vertex(self, v: object) -> None:
        self._vertices.append(v)
        self._adjacent_list.append(DList())

    def _index(self, v: object) -> int:
        try:
            index = self._vertices.index(v)
        except ValueError:
            index = -1
        return index

    def add_edge(self, start: object, end: object, weight: int = None) -> None:
        """This function adds the edge (start,end). First, it must check if the
        vertices exist."""
        i, j = self._index(start), self._index(end)
        if i == -1 or j == -1:
            return

        self._adjacent_list[i].add_last(AdjacentVertex(end, weight))
        if not self._directed:
            self._adjacent_list[j].add_last(AdjacentVertex(start, weight))

    def contain_edge(self,  start, end) -> int:
        """This function adds the edge (start, end). First, it must check if the
        vertices exist."""
        i, j = self._index(start), self._index(end)
        if i == -1 or j == -1:
            return

        for k in range(len(self._adjacent_list[i])):
            adj = self._adjacent_list[i].getAt(k)
            if adj.vertex == end:
                return adj.weight

        return 0

    def remove_edge(self, start, end):
        """This function adds the edge (start , end). First, it must check if the
        vertices exist."""
        i, j = self._index(start), self._index(end)
        if i == -1 or j == -1:
            return

        for k in range(len(self._adjacent_list[i])):
            adj = self._adjacent_list[i].getAt(k)
            if adj.vertex == end:
                self._adjacent_list[i].removeAt(k)
                break

        if not self._directed:
            for k in range(len(self._adjacent_list[j])):
                adj = self._adjacent_list[j].getAt(k)
                if adj.vertex == start:
                    self._adjacent_list[j].removeAt(k)
                    break

    def __str__(self) -> str:
        result = ''
        for i, v in enumerate(self._vertices):
            result += '\n'+str(v)+': '+str(self._adjacent_list[i])
        return result


if __name__ == '__main__':
    # Now, we use the implementation to represent this  undirected graph:
    # <img src='https://i.stack.imgur.com/31ml3.png' width='50%'/>
    # we use this dictionary to represent the vertices with numbers:

    labels = [0, 1, 2, 3, 4]
    g = Graph(labels, False)
    print(g)

    # Now,  we add the edges
    g.add_edge(0, 1)
    g.add_edge(0, 4)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    print(g)

    print()
    print('g.contain_edge({} , {})={}'.format(0, 1, g.contain_edge(0, 1)))
    print('g.contain_edge({}, {})={}'.format(1, 0, g.contain_edge(1, 0)))

    print('g.contain_edge({}, {})={}'.format(3, 1, g.contain_edge(3, 1)))
    print('g.contain_edge({}, {})={}'.format(0, 2, g.contain_edge(0, 2)))

    print(g)
    g.remove_edge(2, 3)
    print(g)

    # Now,  we represent this weighted graph:
    # https://hyperskill.org/learn/step/5645
    # <img src='https://ucarecdn.com/a67cb888-aa0c-424b-8c7f-847e38dd5691/' width=25%>

    labels = [0, 1, 2, 3, 4]
    g = Graph(labels, False)

    # Now,  we add the edges
    g.add_edge(0, 1, 3)
    g.add_edge(0, 3, 7)
    g.add_edge(0, 4, 8)
    g.add_edge(1, 2, 1)
    g.add_edge(1, 3, 4)
    g.add_edge(2, 3, 2)
    g.add_edge(3, 4, 3)
    print(g)
    print()
    print('g.contain_edge({}, {})={}'.format(0, 1, g.contain_edge(0, 1)))
    print('g.contain_edge({}, {})={}'.format(1, 0, g.contain_edge(1, 0)))

    print('g.contain_edge({}, {})={}'.format(3, 1, g.contain_edge(3, 1)))
    print('g.contain_edge({}, {})={}'.format(0, 2, g.contain_edge(0, 2)))

    print(g)
    print()
    print('after removing (2, 3):')
    g.remove_edge(2, 3)
    print(g)

    """Now,  we use the implementation to represent this graph: 

    <img src='https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/CPT-Graphs-directed-weighted-ex1.svg/722px-CPT-Graphs-directed-weighted-ex1.svg.png' width='25%'/>
    """

    labels = ['A', 'B', 'C', 'D', 'E']
    g = Graph(labels)

    # Now,  we add the edges
    g.add_edge('A', 'C', 12)
    g.add_edge('A', 'D', 60)
    g.add_edge('B', 'A', 10)
    g.add_edge('C', 'B', 20)
    g.add_edge('C', 'D', 32)
    g.add_edge('E', 'A', 7)

    print(g)
    print()
    print("g.contain_edge('C', 'B')",  g.contain_edge('C', 'B'))
    print(g.contain_edge('B', 'C'))

    g.remove_edge('C',  'B')
    print('after removing (C,  E)')
    print(g)
