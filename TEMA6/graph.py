# -*- coding: utf-8 -*-
from dlist import DList

class AdjacentVertex:
    def __init__(self, vertex: object, weight: int = 1) -> None:
        self.vertex = vertex
        self.weight = weight

    def __str__(self) -> str:
        """ returns the tuple (v1, weight)"""
        return '(' + str(self.vertex) + ',' + str(self.weight) + ')'


class Graph:
    def __init__(self, list_vertices: list, directed: bool = True) -> None:
        """ vertices: lista de vértices del grafo
            directed: variable booelana que indica si el grafo está dirigido  o no

            El grafo se va a representar como un diccionario _vertices.
            Cada vértice del grafo es una key del diccionario.
            Asociado a cada vértice, el diccionario almacenara una lista de AdjacentVertex.
            Un AdjacentVertex es un objeto con dos atributos: vertex y weight
            En el constructor, no añadimos ninguna arista.

            Suponemos que es un grafo simple (sin aristas loop ni paralelas)
            """

        self._directed = directed
        # La instrucción anterior obtiene el mismo resultados que al ejecutar el siguiente código:
        self._vertices = {}
        for v in list_vertices:
            self._vertices[v] = []


    def __check_vertex(self, v: object) -> bool:
        """Método que devuelve True si v es un vértice del grafo, y False eoc."""
        return v in self._vertices.keys()

    def add_vertex(self, v: object) -> None:
        """añade un nuevo vértice al grafo. Por el momento, no añadimos ninguna arista"""
        if not self.__check_vertex(v):
            self._vertices[v] = []
        else:
            print(v, " ya existe!!!")

    def add_edge(self, start: object, end: object, weight: int = 1) -> None:
        """Método que añade una arista de start a end con peso weight.
        Recuerda que es un grafo simple (sin aristas loop ni aristas paralelas)"""
        if not self.__check_vertex(start):
            print(start, " no es un vértice")
            return
        if not self.__check_vertex(end):
            print(end, " no es un vértice")
            return

        if start == end:
            print("No permitimos añadir loops")
            return

        for adj in self._vertices[start]:
            if adj.vertex == end:
                print("Ya existe un arista de ", start , " a ", end, ". No permitimos aristas paralelas")
                return

        #Si el bucle for termina, significa que la arista start -> end no existe
        # La añadimos
        self._vertices[start].append(AdjacentVertex(end,weight))
        if not self._directed:
            self._vertices[end].append(AdjacentVertex(start,weight))

    def contain_edge(self, start: object, end: object) -> int:
        """ Método que comprueba si existe un arista de start a end.
        Si la arista existe devuelve su peso.
        Si no existe devuelve 0. """
        if not self.__check_vertex(start):
            print(start, " no es un vértice")
            return 0
        if not self.__check_vertex(end):
            print(end, " no es un vértice")
            return 0
        for adj in self._vertices[start]:
            if adj.vertex == end:
                # existe la arista start->end, devolvemos su peso
                return adj.weight
        # si el bucle termina, significa que no se ha encontrado la arista
        return 0

    def remove_edge(self, start: object, end: object):
        """ Método que comprueba si existe un arista de start a end.
                Si la arista existe devuelve su peso.
                Si no existe devuelve 0. """
        if not self.__check_vertex(start):
            print(start, " no es un vértice")
            return
        if not self.__check_vertex(end):
            print(end, " no es un vértice")
            return
        for adj in self._vertices[start]:
            if adj.vertex == end:
                self._vertices[start].remove(adj)
                break

        if not self._directed:
            for adj in self._vertices[end]:
                if adj.vertex == start:
                    self._vertices[end].remove(adj)
                    break

    def get_adjacent_vertices(self, start: object) -> list:
        """ Método que devuelve la lista de vértices vecinos o adyacentes a start.
        La lista sólo contiene vertices (no los pesos)"""
        if not self.__check_vertex(start):
            print(start, " no es un vértice")
            return []

        result = [] # lista vcon los vecinos de start
        for adj in self._vertices[start]:
            result.append(adj.vertex)
        return result


    def get_origins(self, end: object) -> list:
        """ devuelve una lista de vértices que tienen alguna arista a end"""
        if not self.__check_vertex(end):
            print(end, " no es un vértice")
            return []

        result = []  # lista con los vértices origenes a end
        for v in self._vertices.keys():
            for adj in self._vertices[v]:
                if adj.vertex == end:
                    result.append(v)
                    break   # salimos el bucle for adj

        return result

    def __str__(self) -> str:
        """ devuelve una string con los vertices y aristas del grafo"""
        result = ''
        for vertex in self._vertices.keys():
            result += str(vertex) + ': '
            for obj_adj in self._vertices[vertex]:
                result += str(obj_adj) + ' '
            result += '\n'

        return result

    def bfs_iter(self, start: object) -> list:
        """método iterativo que devuelve el recorrido en amplitud del grafo desde el vértice start"""
        if not self.__check_vertex(start):
            print(start, " no es un vértice")
            return []

        result = []     # lista para el recorrido en amplitud desde start
        queue = DList() # lista como cola
        # diccionario para marcar los vértices que ya se han visitado
        visited = dict.fromkeys(self._vertices.keys(), False)
        # añadimos start a la cola, y lo marcamos como visitados
        queue.add_last(start)
        visited[start] = True
        while len(queue) > 0:
            # sacamos el primer vértice de la cola
            v = queue.remove_first()
            # lo añadimos al recorrido
            result.append(v)
            # recuperamos sus adyacentes
            for u in self.get_adjacent_vertices(v):
                # si el vértice vecino u no ha sido visitado
                if not visited[u]:
                    # lo encolamos y lo marcamos como visitado
                    queue.add_last(u)
                    visited[u] = True
        return result

    def dfs_rec(self, start:object) -> list:
        if not self.__check_vertex(start):
            print(start, " no es un vértice!!!")
            return []
        result = []
        visited = dict.fromkeys(self._vertices.keys(), False)
        self._dfs_rec(start, result, visited)
        return result

    def _dfs_rec(self, start: object, result: list, visited: dict):
        result.append(start)
        visited[start] = True
        for v in self.get_adjacent_vertices(start):
            if not visited[v]:
                self._dfs_rec(v, result, visited)

    def dfs_iter(self, start: object) -> list:
        """método iterativo que devuelve el recorrido en profundidad del grafo desde el vértice start"""
        if not self.__check_vertex(start):
            print(start, " no es un vértice")
            return []

        result = []     # lista para el recorrido dfs desde start
        # diccionario para marcar los vértices que ya se han visitado
        visited = dict.fromkeys(self._vertices.keys(), False)
        stack = []  # lista como pila
        # añadimos start a la pila, y lo marcamos como visitados
        stack = [start]
        visited[start] = True
        while len(stack) > 0:
            # desapilamos: el último que entroen la pila
            v = stack.pop()
            # lo añadimos al recorrido
            result.append(v)
            # recuperamos sus adyacentes
            for u in reversed(self.get_adjacent_vertices(v)):
                # si el vértice vecino u no ha sido visitado
                if not visited[u]:
                    # lo encolamos y lo marcamos como visitado
                    stack.add_last(u)
                    visited[u] = True
        return result

if __name__ == '__main__':
    # Ejercicio 1: We use the class to represent an undirected graph without weights :
    # <img src='https://computersciencesource.files.wordpress.com/2010/05/dfs_1.png' width='35%'/>
    list_vertices = ['A', 'B', 'C', 'D']
    mygraph = Graph(list_vertices, False)
    print("Mostramos el grafo después del constructor (sin vértice E):")
    print(mygraph)
    print("Mostramos el grafo después de añadir E: ")
    mygraph.add_vertex('E')
    print(mygraph)
    list_vertices.append('E')

    mygraph.add_edge('A','B')
    mygraph.add_edge('A','E')
    mygraph.add_edge('A','C')

    mygraph.add_edge('B','D')
    mygraph.add_edge('B','E')
    print(mygraph)

    for v in list_vertices:
        print("Vecinos de ", v, ":", mygraph.get_adjacent_vertices(v))
        print("Orígenes de ", v, ":", mygraph.get_origins(v))
        print("bfs desde ", v, ":", mygraph.bfs_iter(v))
        print("dfs desde ", v, ":", mygraph.dfs_rec(v))
        print("dfs desde ", v, ":", mygraph.dfs_iter(v))

        print()

    # Ejercicio 2: Now,  we use the implementation to represent this graph:
    # <img src='https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/CPT-Graphs-directed-weighted-ex1.svg/722px-CPT-Graphs-directed-weighted-ex1.svg.png' width='25%'/>
    mygraph2=Graph(list_vertices)
    mygraph2.add_edge('A','C',12)
    mygraph2.add_edge('A','D',60)
    mygraph2.add_edge('B','A',10)
    mygraph2.add_edge('C','B',20)
    mygraph2.add_edge('C','D',32)
    mygraph2.add_edge('E','A',7)

    for v in list_vertices:
        print("Vecinos de ", v, ":", mygraph2.get_adjacent_vertices(v))
        print("Orígenes de ", v, ":", mygraph2.get_origins(v))
        print("bfs desde ", v, ":", mygraph2.bfs_iter(v))
        print("dfs desde ", v, ":", mygraph2.dfs_rec(v))
        print("dfs desde ", v, ":", mygraph2.dfs_iter(v))

        print()
