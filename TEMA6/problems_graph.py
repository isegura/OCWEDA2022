# -*- coding: utf-8 -*-
from graph import Graph


class Graph4(Graph):
    # delete this method, if it already exists in graph.py
    def add_vertex(self, vertex: str) -> None:
        if vertex in self._vertices.keys():
            print(vertex, ' already exists!')
            return
        self._vertices[vertex] = []

    def _dfs(self, vertex: str, visited: dict) -> None:
        visited[vertex] = True
        for adj in self._vertices[vertex]:
            # adj is an object of AdjacentVertex
            adj_vertex = adj.v1
            if not visited[adj_vertex]:
                self._dfs(adj_vertex, visited)

    def _bfs(self, vertex: str, visited: dict) -> None:
        queue = [vertex]
        visited[vertex] = True
        while len(queue) > 0:
            u = queue.pop(0)
            for adj in self._vertices[u]:
                # remember that adj is an AdjacentVertex
                if not visited[adj.v1]:
                    queue.append(adj.v1)
                    visited[adj.v1] = True

    def non_accessible(self, vertex: str) -> list:
        """gets a v1 and returns the list of vertices
        that cannot be reached from v1, that is, there is no path
        from v1 to these vertices"""
        # First, we need to obtain all vertices that can be
        # reached from v1. To do this, we can apply
        # the algorithms of dfs or bfs
        visited = {}
        for v1 in self._vertices:
            visited[v1] = False
        self._dfs(vertex, visited)
        # The function _dfs will visit all vertices reachable
        # from v1. Therefore, the non-visited vertices
        # will form the list of non-accessible vertices from v1
        result = []  # list with the non-accessible vertices
        for v1 in self._vertices:
            if not visited[v1]:
                result.append(v1)

        return result

    def get_reachable(self, vertex: str, alg: str = '_dfs') -> list:
        """gets a v1 and returns the list of vertices
        that can be reached from v1, that is, there is a path
        from v1 to these vertices"""
        # First, we need to obtain all vertices that can be
        # reached from v1. To do this, we can apply
        # the algorithms of dfs or bfs
        visited = {}
        for v1 in self._vertices:
            visited[v1] = False
        if alg == '_dfs':
            self._dfs(vertex, visited)
        else:
            self._bfs(vertex, visited)

        # The function _dfs will visit all vertices reachable
        # from v1. Therefore, the visited vertices
        # will form the list of accessible vertices from v1
        result = []  # list with the accessible vertices
        for v1 in self._vertices:
            if visited[v1]:
                result.append(v1)

        return result

    def _check_bipartite(self, source: str, color: dict) -> bool:

        # Assign first color to source
        queue = [source]
        color[source] = 1
        # similar to bfs
        while len(queue):
            u = queue.pop(0)
            for adj in self._vertices[u]:
                adj_vertex = adj.v1
                if color[adj_vertex] is None:
                    color[adj_vertex] = 1 - color[u]
                    queue.append(adj_vertex)
                elif color[adj_vertex] == color[u]:
                    return False

        # If we reach here, then all adjacent
        # vertices can be colored with alternate
        # color
        return True

    def check_bipartite(self) -> bool:
        """ returns True if the graph is bipartite and False eoc
        A graph is bipartite is a graph whose vertices can be divided
        into two independent sets, U and V
        such that every edge (u, v) either connects a v1
        from U to V or a v1 from V to U.
        In other words, for every edge (u, v), either u belongs to U and v to V,
         or u belongs to V and v to U. We can also say that there is no edge
         that connects vertices of same set. """
        color = {}
        # We use a dictionary color to save the color
        # assigned to each v1: 1 means first color (origins)
        # , 0 means second color (target)
        for v1 in self._vertices:
            color[v1] = None

        for v1 in self._vertices:
            if color[v1] is None:
                if not self._check_bipartite(v1, color):
                    return False

        return True

    def _has_cycles_bfs(self, vertex: str, visited: dict) -> bool:
        """This is function is based on bfs to detect if there is
        some cycle in the breadth traversal from v1. It uses the dictionary
        visited and the parent of the vertices to detect
        cycle in subgraph reachable from v1 v."""

        # Mark the current v1 as visited
        queue = [vertex]
        parents = {}
        for v1 in self._vertices:
            parents[v1] = None

        while len(queue) > 0:
            s = queue.pop(0)
            visited[s] = True
            for adj in self._vertices[s]:
                adj_vertex = adj.v1
                if not visited[adj_vertex]:
                    visited[adj_vertex] = True
                    queue.append(adj_vertex)
                    parents[adj_vertex] = s
                elif parents[s] != adj_vertex:
                    # if the ajd_vertex has been already visited,
                    # and it is not the parent of current v1,
                    # then there is a cycle
                    return True
        return False

    def _has_cycles_dfs(self, vertex: str, visited: dict, parent: str) -> bool:
        """This is recursive function that uses the dictionary
        visited and the parent of the vertices to detect
        cycle in subgraph reachable from v1 v."""

        # Mark the current v1 as visited
        visited[vertex] = True
        # Recur for all the vertices
        # adjacent to this v1
        for adj in self._vertices[vertex]:
            adj_vertex = adj.v1
            # If the node is not visited then recurse on it
            if not visited[adj_vertex]:
                if self._has_cycles_dfs(adj_vertex, visited, vertex):
                    return True
            elif parent != adj_vertex:
                # if the ajd_vertex has been already visited,
                # and it is not the parent of current v1,
                # then there is a cycle
                return True
        print()
        return False

    def _has_cycles_directed(self, vertex: str, visited: dict, rec_stack: dict) -> bool:
        """detects a cycle in a directed graph using the
        dfs alg. Moreover, visited and rec_stack allow us
        to detect if a v1 has been previously visited."""

        # Mark the current v1 as visited
        visited[vertex] = True
        rec_stack[vertex] = True
        # Recur for all the vertices
        # adjacent to this v1
        for adj in self._vertices[vertex]:
            adj_vertex = adj.v1
            # If the node is not visited then recurse on it
            if not visited[adj_vertex]:
                if self._has_cycles_directed(adj_vertex, visited, rec_stack):
                    return True
            elif rec_stack[adj_vertex]:
                return True
        # The node needs to be popped from
        # recursion stack before function ends
        rec_stack[vertex] = False
        return False

    def has_cycles(self, alg: str = 'dfs') -> bool:
        """returns True if the graph contains a cycle, False eoc"""
        print(self._directed)
        visited = {}
        recursion_stack = {}

        for v1 in self._vertices:
            visited[v1] = False
            # we will only use it for directed graphs
            recursion_stack[v1] = False

        # Call the recursive helper
        # function to detect cycle in different
        # DFS trees
        for v1 in self._vertices:
            if not visited[v1]:
                if self._directed:
                    result = self._has_cycles_directed(v1, visited, recursion_stack)
                else:
                    if alg == 'dfs':
                        result = self._has_cycles_dfs(v1, visited, None)
                    else:
                        result = self._has_cycles_bfs(v1, visited)

                if result:
                    return True

        return False


if __name__ == '__main__':
    # We use the class to represent an undirected graph without weights :
    # <img src='https://computersciencesource.files.wordpress.com/2010/05/dfs_1.png' width='35%'/>

    labels = ['A', 'B', 'C', 'D', 'E']
    g = Graph4(labels, False)
    g.add_edge('A', 'B')  # A:0,  B:1
    g.add_edge('A', 'C')  # A:0,  C:2
    g.add_edge('A', 'E')  # A:0,  E:5
    g.add_edge('B', 'D')  # B:1,  D:4
    g.add_edge('B', 'E')  # C:2,  B:1
    print(g)
    # Please, draw the graph. This is a connected graph, that is,
    # for any pair of vertices, there is a path between them
    for v in g._vertices:
        list_non_accessible = g.non_accessible(v)
        print("non-accessible from {}:{} ".format(v, list_non_accessible))
        # all list should be empty
        assert list_non_accessible == []

        list_reachable = g.get_reachable(v)
        print("reachable from {}: {} ".format(v, list_reachable))
        assert list_reachable == list(g._vertices.keys())
        # we now use the _bfs alg
        list_reachable = g.get_reachable(v, '_bfs')
        print("reachable (using _bfs) from {}: {} ".format(v, list_reachable))
        assert list_reachable == list(g._vertices.keys())
        print()
    algorithm = 'bfs'
    print("has cycles? ", g.has_cycles(algorithm))
    assert g.has_cycles(algorithm)

    # we add more vertices to the graph (please, download
    # graph.py if you don't have the method add_vertex
    g.add_vertex("F")
    g.add_vertex("G")
    g.add_vertex("H")
    # Now, we add edges to connect these nodes between them,
    # but not with the other vertices. In this way, we will have
    # a subgraph
    g.add_edge("F", "G")
    g.add_edge("F", "H")
    g.add_edge("G", "H")
    print(g)

    # now, we show the non-accessible vertices for each v1 in the graph
    for v in g._vertices:
        list_non_accessible = g.non_accessible(v)
        print("non-accessible from {}:{} ".format(v, list_non_accessible))
        list_reachable = g.get_reachable(v)
        print("reachable from {}:{} ".format(v, list_reachable))
        list_reachable = g.get_reachable(v, '_bfs')
        print("reachable (using _bfs) from {}: {} ".format(v, list_reachable))

        print()
        # checks if our methods are correct (similar to unitest)
        if v in ['A', 'B', 'C', 'D', 'E']:
            assert sorted(list_non_accessible) == ['F', 'G', 'H']
            assert sorted(list_reachable) == ['A', 'B', 'C', 'D', 'E']
        elif v in ['F', 'G', 'H']:
            assert sorted(list_non_accessible) == ['A', 'B', 'C', 'D', 'E']
            assert sorted(list_reachable) == ['F', 'G', 'H']

    print("has cycles? ", g.has_cycles(algorithm))
    assert g.has_cycles(algorithm)

    # We create an undirected graph without cycles
    labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    g = Graph4(labels, False)
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'D')
    g.add_edge('B', 'E')
    g.add_edge('C', 'F')
    g.add_edge('C', 'G')
    g.add_edge('E', 'H')
    g.add_edge('F', 'I')
    print(g)
    print("has_cycles: {}".format(g.has_cycles()))
    assert not g.has_cycles()

    # Now,  we use the implementation to represent this graph:
    # <img src='https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/CPT-Graphs-directed-weighted-ex1.svg/722px-CPT-Graphs-directed-weighted-ex1.svg.png' width='25%'/>

    labels = ['A', 'B', 'C', 'D', 'E']
    g = Graph4(labels)

    # Now, we add the edges
    g.add_edge('A', 'C', 12)  # A->(12)C
    g.add_edge('A', 'D', 60)  # A->(60)D
    g.add_edge('B', 'A', 10)  # B->(10)A
    g.add_edge('C', 'B', 20)  # C->(20)B
    g.add_edge('C', 'D', 32)  # C->(32)D
    g.add_edge('E', 'A', 7)   # E->(7)A

    print(g)
    print("has cycles? ", g.has_cycles(algorithm))
    assert g.has_cycles(algorithm)

    for v in g._vertices:
        list_non_accessible = g.non_accessible(v)
        print("non-accessible from {}:{} ".format(v, list_non_accessible))
        list_reachable = g.get_reachable(v)
        print("reachable from {}:{} ".format(v, list_reachable))
        list_reachable = g.get_reachable(v, '_bfs')
        print("reachable (using _bfs) from {}: {} ".format(v, list_reachable))

        print()
        # checks if our method is correct (similar to unitest)
        if v in ['A', 'B', 'C']:
            assert sorted(list_non_accessible) == ['E']
            assert sorted(list_reachable) == ['A', 'B', 'C', 'D']
        elif v == 'D':
            assert sorted(list_non_accessible) == ['A', 'B', 'C', 'E']
            assert sorted(list_reachable) == ['D']
        elif v == 'E':
            assert sorted(list_non_accessible) == []
            assert sorted(list_reachable) == ['A', 'B', 'C', 'D', 'E']

    # Let us remove the edge from B to A, the graph does not have any cycle
    g.remove_edge('B', 'A')
    print(g)
    print("has cycles? ", g.has_cycles(algorithm))
    assert not g.has_cycles(algorithm)

    labels = ['A', 'B', 'C']
    g = Graph4(labels)
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'C')
    print(g)
    print("has cycles? ", g.has_cycles(algorithm))
    assert not g.has_cycles(algorithm)

    # remove A -> C
    g.remove_edge('A', 'C')
    print("has cycles? ", g.has_cycles(algorithm))
    assert not g.has_cycles(algorithm)

    # add C -> A, now, the graph is cyclic!!!
    g.add_edge('C', 'A')
    print("has cycles? ", g.has_cycles(algorithm))
    assert g.has_cycles(algorithm)

    print('check_bipartite ', g.check_bipartite())
    # assert not g.check_bipartite()

    # now, the graph is bipartite
    g.remove_edge('C', 'A')
    g.remove_edge('A', 'B')
    g.add_edge('A', 'C')
    print(g)
    print('check_bipartite ', g.check_bipartite())
    assert g.check_bipartite()

    # we create a bipartite graph
    labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    g = Graph4(labels, False)
    g.add_edge('A', 'E')
    g.add_edge('A', 'F')
    g.add_edge('B', 'G')
    g.add_edge('C', 'F')
    g.add_edge('D', 'H')
    print(g)
    print('check_bipartite ', g.check_bipartite())
    assert g.check_bipartite()
    g.add_edge('H', 'A')
    print(g)
    print('check_bipartite ', g.check_bipartite())
    assert g.check_bipartite()
