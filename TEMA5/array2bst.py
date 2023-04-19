from bst import BinarySearchTree
from bintree import BinaryNode


def array2bst(input_list: list) -> BinarySearchTree:
    """ gets a sorted list and creates a balanced bst"""
    result = BinarySearchTree()
    if input_list and len(input_list) >= 1:
        _array2bst(input_list, 0, len(input_list)-1, result)
    return result

def _array2bst(input_list: list, start: int, end: int,
               tree: BinarySearchTree) -> None:
    if start <= end:
        index_mid = (start + end) // 2
        tree.insert(input_list[index_mid])
        _array2bst(input_list, start, index_mid-1, tree)
        _array2bst(input_list, index_mid+1, end, tree)


def _array2bst2(input_list: list, tree: BinarySearchTree) -> None:
    if len(input_list) > 0:
        index_mid = len(input_list) // 2
        tree.insert(input_list[index_mid])

        _array2bst2(input_list[:index_mid], tree)
        _array2bst2(input_list[index_mid+1:], tree)



if __name__ == "__main__":
    data = [50, 20, 60, 15, 55, 70, 10, 18, 75, 8, 93]
    data.sort()
    print(data)
    # data = [5, 10, 15, 20, 25, 30]
    tree = array2bst(data)
    tree.draw()
