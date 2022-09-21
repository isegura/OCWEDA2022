# -*- coding: utf-8 -*-

import sys
from graph import Graph
import math
class Graph3(Graph):
    """ Algorithms for shortest path """

    def min_distance(self, distances: dict, visited: dict) -> int:
        """returns the vertex (index) whose associated value in
        the dictionary distances is the smallest value. We
        only consider the set of vertices that have not been visited"""
        # Initialize minimum distance for next node
        min_distance = math.inf
        min_vertex = None

        # returns the vertex with minimum distance from the non-visited vertices
        for vertex in self._vertices.keys():
            if distances[vertex] <= min_distance and not visited[vertex]:
                min_distance = distances[vertex]  # update the new smallest
                min_vertex = vertex      # update the index of the smallest

        return min_vertex

    def dijkstra(self, origin: object) -> None:
        visited = {}    # for each vertex (key), the value is a boolean indicating if the vertex has been visited
        previous = {}   # for each vertex (key), the value is the previous node in the minimum path from origin
        distances = {}  # for each vertex (key), the value is minimum distance in the minimum path from origin

        # initialize dictionaries
        for v in self._vertices.keys():
            visited[v] = False
            previous[v] = None
            distances[v] = math.inf

        # The distance from origin to itself is 0
        distances[origin] = 0

        for _ in range(len(self._vertices)):
            # pick the non-visited vertex with minimum distance
            u = self.min_distance(distances, visited)
            visited[u] = True
            # get the adjacent vertices of u
            for adj in self._vertices[u]:
                i = adj.vertex
                w = adj.weight
                # for non-visited vertex, we have to check if its distance is greater than the distance from u
                if not visited[i] and distances[i] > distances[u]+w:
                    # we must update because its distance is greater than the new distance
                    distances[i] = distances[u]+w
                    previous[i] = u

        # Finally, we print the minimum path from origin to the other vertices
        self.print_solution(distances, previous, origin)

        return distances, previous

    def print_solution(self, distances: dict, previous: dict, origin: object):
        print("Minimum path from ", origin)

        for i in self._vertices.keys():
            if distances[i] == sys.maxsize:
                print("There is not path from ", origin, ' to ', i)
            else:
                # minimum_path is the list which contains the minimum path from origin to i
                minimum_path = []
                prev = previous[i]
                # this loop helps us to build the path
                while prev is not None:
                    minimum_path.insert(0, prev)
                    prev = previous[prev]

                # we append the last vertex, which is i
                minimum_path.append(i)

                # we print the path from v to i and the distance
                print(origin, '->', i, ":", minimum_path, distances[i])

    def bellmanford(self, origin: object) -> None:
        """Bellman-Ford algorithm for minimum path"""
        previous = {}
        distances = {}
        for v in self._vertices.keys():
            previous[v] = None
            distances[v] = math.inf
        distances[origin] = 0

        for _ in range(len(self._vertices)-1):
            for u in self._vertices.keys():
                # get all adjacent vertices of u
                for adj in self._vertices[u]:
                    v = adj.vertex
                    w = adj.weight
                    if distances[v] > distances[u] + w:
                        distances[v] = distances[u] + w
                        previous[v] = u

        for u in self._vertices.keys():
            for adj in self._vertices[u]:
                v = adj.vertex
                w = adj.weight
                if distances[v] > distances[u] + w:
                    print('There is no solution ', origin)
                    return False

        self.print_solution(distances, previous, origin)

    def minimum_path(self, start: object, end: object) -> list:
        """ returns a list containing the path from star to end.
        It also returns the distance of the path. If the path
        does not exist, it returns an empty list and infinitum"""
        if start not in self._vertices.keys():
            print(start, ' does not exist!!!')
            return None, None
        if end not in self._vertices.keys():
            print(end, ' does not exist!!!')
            return None, None

        distances, previous = self.dijkstra(start)
        if distances[end] == math.inf:
            return [], math.inf

        result = [end]
        prev = previous[end]
        while prev is not None:
            result.insert(0, prev)
            prev = previous[prev]

        return result, distances[end]

if __name__ == '__main__':
    # Now, we use the implementation to represent this graph:
    #  <img src='https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/CPT-Graphs-directed-weighted-ex1.svg/722px-CPT-Graphs-directed-weighted-ex1.svg.png' width='25%'/>
    labels = ['A', 'B', 'C', 'D', 'E']
    g = Graph3(labels)
    # Now, we add the edges
    g.add_edge('A', 'C')  # A->(12)C
    g.add_edge('A', 'D')  # A->(60)D
    g.add_edge('B', 'A')  # B->(10)A
    g.add_edge('C', 'B')  # C->(20)B
    g.add_edge('C', 'D')  # C->(32)D
    g.add_edge('E', 'A')  # E->(7)A

    print(g)

    # g.dijkstra('A')
    print('minimum path from {} to {}: {}'.format('A', 'B', g.minimum_path('A', 'B')))
    print('minimum path from {} to {}: {}'.format('A', 'E', g.minimum_path('A', 'E')))
    print('minimum path from {} to {}: {}'.format('J', 'E', g.minimum_path('J', 'E')))

    labels = ['A', 'B', 'C', 'D', 'E']
    g = Graph3(labels)

    g.add_edge('A', 'C', 12)  # A->(12)C
    g.add_edge('A', 'D', 60)  # A->(60)D
    g.add_edge('B', 'A', 10)  # B->(10)A
    g.add_edge('C', 'B', 20)  # C->(20)B
    g.add_edge('C', 'D', 32)  # C->(32)D
    g.add_edge('E', 'A', 7)  # E->(7)A
    # Now, we add the edges

    print(g)
    print('minimum path from {} to {}: {}'.format('A', 'B', g.minimum_path('A', 'B')))
    print('minimum path from {} to {}: {}'.format('A', 'E', g.minimum_path('A', 'E')))
    print('minimum path from {} to {}: {}'.format('J', 'E', g.minimum_path('J', 'E')))


    g.bellmanford('A')
    #
    labels = ['A', 'B', 'C']
    g = Graph3(labels)
    g.add_edge('A', 'B', -1)
    g.add_edge('B', 'C', -1)
    g.add_edge('C', 'A', -1)
    print(g)
    for c in g._vertices.keys():
         g.bellmanford(c)

    # Exercise: Calculate the minimum path from
    # 'a' to the rest of the vertices in this graph:
    # <img src='https://www.bogotobogo.com/python/images/Dijkstra/graph_diagram.png' src='25%'/>
    #
    labels = ['a', 'b', 'c', 'd', 'e', 'f']
    g = Graph3(labels, False)
    #
    # # Now, we add the edges
    g.add_edge('a', 'b', 7)
    g.add_edge('a', 'c', 9)
    g.add_edge('a', 'f', 14)
    g.add_edge('b', 'c', 10)
    g.add_edge('b', 'd', 15)
    g.add_edge('c', 'd', 11)
    g.add_edge('c', 'f', 2)
    g.add_edge('d', 'e', 6)
    g.add_edge('e', 'f', 9)
    print(g)

    for c in g._vertices.keys():
        print('dijkstra:')
        g.dijkstra(c)
        print('bellmanford:')
        g.bellmanford(c)
        print()


    # # # Exercise: Use the previous implementation to obtain the minimum path from X to Y in this graph:
    # # #  <img src='http://benalexkeen.com/wp-content/uploads/2017/01/Dijkstra.png'>

