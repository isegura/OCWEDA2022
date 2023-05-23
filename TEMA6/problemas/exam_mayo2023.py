class MyGraph:

    def __init__(self, list_vertices: list) -> None:
        self._vertices = {}
        for v in list_vertices:
            self._vertices[v]= []

    def add_edge(self, i: int, j: int) -> None:
        if i not in self._vertices.keys():
            return
        if j not in self._vertices.keys():
            return
        self._vertices[i].append(j)

    def have_path_to_odd(self, k: int) -> list:
        result = []

        if not isinstance(k, int) or k <= 1:
            print(k, " must be an integer greater than 1")
            return result

        for origin in self._vertices.keys():
            visited = dict.fromkeys(self._vertices.keys(), False)
            if self.__has_path_to_odd(origin, origin, k, visited):
                result.append(origin)
        return result

    def __has_path_to_odd(self, origin: int, v: int, k: int, visited: dict) -> bool:
        if k == 0:
            return False
        if origin != v and v % 2 != 0:
            return True

        visited[v] = True
        for neighbour in self._vertices[v]:
            if not visited[neighbour]:
                if self.__has_path_to_odd(origin, neighbour, k - 1, visited):
                    return True

        return False


if __name__ == '__main__':
    vertices = [2, 4, 6, 8, 10, 12, 14, 16, 17, 20, 22, 24, 25]
    g = MyGraph(vertices)

    g.add_edge(2, 4)
    g.add_edge(2, 10)

    g.add_edge(4, 6)

    g.add_edge(6, 12)
    g.add_edge(6, 14)

    g.add_edge(8, 6)
    g.add_edge(8, 10)
    g.add_edge(8, 12)

    g.add_edge(10, 16)

    g.add_edge(14, 22)

    g.add_edge(16, 12)
    g.add_edge(16, 20)

    g.add_edge(17, 14)
    g.add_edge(17, 22)

    g.add_edge(20, 12)
    g.add_edge(20, 17)
    g.add_edge(20, 25)

    g.add_edge(22, 24)

    g.add_edge(24, 17)

    g.add_edge(25, 24)

    for distance in range(1, 12):
        result_k = g.have_path_to_odd(distance)
        print("distance less than ", distance, ":",  result_k)
