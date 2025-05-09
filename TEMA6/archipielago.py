from dlist import DList

class AdjacentIsland:
    def __init__(self, name_island: str, d: int, h: int):
       self.island = name_island
       self.distance = d
       self.height = h

    def __str__(self) -> str:
       return "("+ self.island +", " + str(self.distance) + ", " + str(self.height) + ")"

class Archipielago:
    def __init__(self, islands: list) -> None:
        self._islands = DList()
        self._adjacent_islands = DList()

        for island in islands:
            self._islands.add_last(island)
            self._adjacent_islands.add_last(DList())

    def __str__(self) -> str:
        result = ""
        for i in range(len(self._islands)):
            result += str(self._islands.getAt(i))
            result += ":  " + str(self._adjacent_islands.getAt(i)) + '\n'
        return result

    def get_index_island(self, island: str) -> int:
        return self._islands.index(island)

    def add_bridge(self, island1: str, island2: str, d: int, h: int) -> None:
        index1 = self.get_index_island(island1)
        index2 = self.get_index_island(island2)
        if index1 == -1:
            print(island1, " no existe en el archipielago")
            return None
        if index2 == -1:
            print(island2, " no existe en el archipielago")
            return None
        if island1 == island2:
            print("No se permiten puentes que van de la misma isla a la misma isla")
            return
        # recuperamos la lista DList de AdjacentIslands para index1
        adj_islands = self._adjacent_islands.getAt(index1)
        for i in range(len(adj_islands)):
            adj = adj_islands.getAt(i)
            if adj.island == island2:
                print("Ya existe un puente de ", island1, " a ", island2)
                return

        self._adjacent_islands.getAt(index1).add_last(AdjacentIsland(island2, d, h))
        self._adjacent_islands.getAt(index2).add_last(AdjacentIsland(island1, d, h))

    def get_adjacent_islands(self, island: str) -> DList:
        index = self.get_index_island(island)
        if index == -1:
            print(island, " no existe en el archipielago")
            return None
        neighbors = DList()
        adj_islands = self._adjacent_islands.getAt(index)
        for i in range(len(adj_islands)):
            adj = adj_islands.getAt(i)
            neighbors.add_last(adj.island)
        return neighbors

    def get_nonaccesible_islands(self) -> DList:
        start = self._islands.getAt(0)
        queue = DList()
        visited = {}
        for i in range(len(self._islands)):
            island = self._islands.getAt(i)
            visited[island] = False

        queue.add_last(start)
        visited[start] = True

        while len(queue) > 0:
            v = queue.remove_first()
            index_v = self.get_index_island(v)
            neighbors_adj = self._adjacent_islands.getAt(index_v)
            for i in range(len(neighbors_adj)):
                adj_island = neighbors_adj.getAt(i)
                if not visited[adj_island.island]:
                    queue.add_last(adj_island.island)
                    visited[adj_island.island] = True

        result = DList()
        for v in visited.keys():
            if not visited[v]:
                result.add_last(v)
        return result

    def get_nonaccesible_islands_tide(self, tide: int) -> DList:
        start = self._islands.getAt(0)
        queue = DList()
        visited = {}
        for i in range(len(self._islands)):
            island = self._islands.getAt(i)
            visited[island] = False

        queue.add_last(start)
        visited[start] = True

        while len(queue) > 0:
            v = queue.remove_first()
            index_v = self.get_index_island(v)
            neighbors_adj = self._adjacent_islands.getAt(index_v)
            for i in range(len(neighbors_adj)):
                adj_island = neighbors_adj.getAt(i)
                if not visited[adj_island.island] and adj_island.height >= tide:
                    queue.add_last(adj_island.island)
                    visited[adj_island.island] = True

        result = DList()
        for v in visited.keys():
            if not visited[v]:
                result.add_last(v)
        return result




if __name__ == '__main__':
    islas=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

    my_archi = Archipielago(islas)
    print(my_archi)

    my_archi.add_bridge('A', 'B', 2, 1)
    my_archi.add_bridge('A', 'D', 1, 5)
    my_archi.add_bridge('A', 'E', 5, 10)

    my_archi.add_bridge('B', 'C', 2, 0)

    my_archi.add_bridge('C', 'F', 8, 0)

    my_archi.add_bridge('D', 'F', 3, 2)

    my_archi.add_bridge('E', 'F', 4, 1)

    my_archi.add_bridge('A', 'A', 10, 5)
    my_archi.add_bridge('A', 'B', 15, 10)

    print(my_archi)

    for i in islas:
        print("Islas vecinas de ", i, ": ", my_archi.get_adjacent_islands(i))

    print("Islas que no son accesibles: ", my_archi.get_nonaccesible_islands())
    print("Islas que no son accesibles: ", my_archi.get_nonaccesible_islands_tide(5))
