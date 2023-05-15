# -*- coding: utf-8 -*-

from graph import Graph


class Graph2(Graph):
    """ Graph2 is a Graph's subclass. In this class,
    we will implement the breadth-first and depth-first traversals
    """

    def bfs_full(self) -> list:
        """This method returns a list containing all vertices of
        the graph by BFS traversal"""

        # Mark all the vertices as not visited
        visited_vertex = {}
        for v in self._vertices.keys():
            visited_vertex[v] = False
        # the list that will save the BFS traversal of the whole graph
        result = []
        # This for forces to traverse all vertices in the graph
        for v in self._vertices.keys():
            if not visited_vertex[v]:
                self.bfs(v, visited_vertex, result)
        return result

    def bfs(self, vertex: object, visited_vertex: dict, list_traversal: list) -> None:
        """This method saves the BFS traversal from v1 in the list
         list_traversal."""
        
        # It will save the indices of vertices to visit
        queue = []
        # mark the source v1 as visited
        visited_vertex[vertex] = True
        # and enqueue it 
        queue.append(vertex)
        
        while queue: 
            # gets the first element
            s = queue.pop(0) 
            # we print the v1, so we need to get its label
            # print(s, end=" ")
            list_traversal.append(s)
            # Get all adjacent vertices of s
            # If an adjacent v1 has not been visited,
            # then mark it visited and enqueue it 
            for adj in self._vertices[s]:
                u = adj.vertex
                if not visited_vertex[u]:
                    queue.append(u)
                    visited_vertex[u] = True

    def dfs_full(self, strategy: str = 'recursive') -> list:
        """This method return a list with all vertices of the graph
        by the DFS traversal."""

        print('dfs traversal:')
        # Mark all the vertices as not visited
        visited_vertex = {}
        for vertex in self._vertices.keys():
            visited_vertex[vertex] = False

        # the list that will save the DFS traversal
        result = []
        for vertex in self._vertices.keys():
            if not visited_vertex[vertex]:
                if strategy == 'recursive':
                    self.dfs(vertex, visited_vertex, result)
                else:
                    self.dfs_iterative(vertex, visited_vertex, result)

        return result

    def dfs(self, vertex: object, visited_vertex: dict, list_traversal: list) -> None:
        """This method saves the DFS traversal
        from the v1 into list_traversal"""
        # Mark the current node as visited and print it
        visited_vertex[vertex] = True
        # print(v1, end=' ')
        list_traversal.append(vertex)

        # Recur for all the vertices  adjacent to this v1
        for adj in self._vertices[vertex]:
            u = adj.vertex
            if not visited_vertex[u]:
                self.dfs(u, visited_vertex, list_traversal)

    def dfs_iterative(self, vertex: object, visited_vertex: dict, list_traversal: list) -> None:
        """This method saves the DFS traversal from v1 into list_traversal"""

        # we use a list as a stack. We add and remove always from the end (peak) of the list.
        stack = [vertex]
        # mark the source v1 as visited
        visited_vertex[vertex] = True

        while len(stack) > 0:
            # remove the last added
            s = stack.pop()
            # print (s, end = " ")
            list_traversal.append(s)

            # Get all adjacent vertices of the dequeued index.
            # If an adjacent v1 has not been visited,
            # then mark it visited and enqueue it
            for adj in reversed(self._vertices[s]):
                # print(adj)
                u = adj.vertex
                if not visited_vertex[u]:
                    # we add at the end (peak) of the stack
                    stack.append(u)
                    visited_vertex[u] = True


if __name__ == '__main__':
    # Now, we use the implementation to represent and traverse this graph:
    # <img src='https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/CPT-Graphs-directed-weighted-ex1.svg/722px-CPT-Graphs-directed-weighted-ex1.svg.png' width='25%'/>

    labels = ['A', 'B', 'C', 'D', 'E']

    g = Graph2(labels)

    # Now, we add the edges
    g.add_edge('A', 'C', 12)  # A->(12)C
    g.add_edge('A', 'D', 60)  # A->(60)D
    g.add_edge('B', 'A', 10)  # B->(10)A
    g.add_edge('C', 'B', 20)  # C->(20)B
    g.add_edge('C', 'D', 32)  # C->(32)D
    g.add_edge('E', 'A', 7)   # E->(7)A

    print(g)
    print("BFS traversal:", g.bfs_full())
    print("DFS traversal:", g.dfs_full())

    for v1 in labels:

        result_bfs = []
        visited = dict.fromkeys(labels, False)

        g.bfs(v1, visited, result_bfs)
        print("BFS traversal from {}: {}".format(v1, result_bfs))

        visited = dict.fromkeys(labels, False)
        result_dfs_rec = []
        g.dfs(v1, visited, result_dfs_rec)
        print("BFS traversal from {}: {}".format(v1, result_dfs_rec))

        visited = dict.fromkeys(labels, False)
        result_dfs_it = []
        g.dfs_iterative(v1, visited, result_dfs_it)
        print("BFS traversal from {}: {}".format(v1, result_dfs_it))

        print()
    # We use the implementation to represent an undirected graph without weights :
    # <img src='https://computersciencesource.files.wordpress.com/2010/05/dfs_1.png' width='35%'/>

    labels = ['A', 'B', 'C', 'D', 'E']
    g = Graph2(labels, False)
    g.add_edge('A', 'B')  # A:0, B:1
    g.add_edge('A', 'C')  # A:0, C:2
    g.add_edge('A', 'E')  # A:0, E:5
    g.add_edge('B', 'D')  # B:1, D:4
    g.add_edge('B', 'E')  # C:2, B:1
    # g.add_edge('A','H',8)

    print(g)

    # we use this dictionary to represent the vertices with numbers:
    labels = ['A', 'B', 'C', 'D', 'E']
    g = Graph2(labels)

    # Now, we add the edges
    g.add_edge('A', 'C', 12)  # A->(12)C
    g.add_edge('A', 'D', 60)  # A->(60)D
    g.add_edge('B', 'A', 10)  # B->(10)A
    g.add_edge('C', 'B', 20)  # C->(20)B
    g.add_edge('C', 'D', 32)  # C->(32)D
    g.add_edge('E', 'A', 7)  # E->(7)A

    print(g)

