from bst import BinarySearchTree
from bintree import BinaryNode

def get_smallest_ite(tree: BinarySearchTree) -> int:
    """returns the smallest element in input_tree. O(log n)"""
    result = None
    if tree is None:
        print("Tree is None!!!")
    else:
        node = tree.root
        if node is None:
            print("the root is None")
        else:
            while node.left:
                node = node.left
            result = node.elem
    return result


def get_greatest_ite(tree: BinarySearchTree) -> int:
    """returns the greatest element in input_tree. O(log n)"""
    result = None
    if tree is None:
        print("Tree is None!!!")
    else:
        node = tree.root
        if node is None:
            print("the root is None")
        else:
            while node.right:
                node = node.right
            result = node.elem
    return result


def get_smallest_rec(tree: BinarySearchTree) -> int:
    """returns the smallest element in input_tree"""
    result = None
    if tree is None:
        print("Tree is None!!!")
    else:
        result = _get_smallest_rec(tree.root)
    return result


def _get_smallest_rec(node: BinaryNode) -> int or None:
    result = None
    if node is not None:
        if node.left:
            result = _get_smallest_rec(node.left)
        else:
            return node.elem
    return result


def sum_elements(tree: BinarySearchTree) -> int:
    """returns the sum of the elements. O(n)"""
    result = None
    if tree is None:
        print("input_tree is None!!!")
    else:
        elements = tree.inorder_list()
        result = sum(elements)
    return result


def sum_elements_rec(tree: BinarySearchTree) -> int:
    """returns the sum of the elements. O(n)"""
    result = None
    if tree is None:
        print("input_tree is None!!!")
    else:
        result = _sum_elements_rec(tree.root)
    return result


def _sum_elements_rec(node: BinaryNode) -> int or None:
    """returns the sum of all elements in the subtree node"""
    result = 0
    if node is not None:
        result = node.elem + _sum_elements_rec(node.left) + _sum_elements_rec(node.right)
    return result

def array2bst(input_list: list) -> BinarySearchTree:
    """ gets a sorted list and creates a balanced bst"""
    result = BinarySearchTree()
    if input_list and len(input_list) >= 1:
        _array2bst(input_list, 0, len(input_list) - 1, result)
    return result


def _array2bst(input_list: list, start: int, end: int,
               tree: BinarySearchTree) -> None:
    if start <= end:
        index_mid = (start + end) // 2
        tree.insert(input_list[index_mid])
        _array2bst(input_list, start, index_mid - 1, tree)
        _array2bst(input_list, index_mid + 1, end, tree)


def _array2bst2(input_list: list, tree: BinarySearchTree) -> None:
    if len(input_list) > 0:
        index_mid = len(input_list) // 2
        tree.insert(input_list[index_mid])

        _array2bst2(input_list[:index_mid], tree)
        _array2bst2(input_list[index_mid + 1:], tree)


if __name__ == "__main__":
    input_tree = BinarySearchTree()
    values = [25, 20, 36, 10, 22, 30, 40, 5, 12, 28, 38, 48]
    for x in values:
        input_tree.insert(x)
    input_tree.draw()

    print("Smallest element: ", get_smallest_ite(input_tree))
    assert get_smallest_ite(input_tree) == min(values)

    print("Smallest element: ", get_smallest_rec(input_tree))
    tree_empty = BinarySearchTree()
    print("Smallest element: ", get_smallest_rec(tree_empty))
    assert get_smallest_rec(input_tree) == min(values)

    print("Greatest element: ", get_greatest_ite(tree_empty))
    print("Greatest element: ", get_greatest_ite(input_tree))
    assert get_greatest_ite(input_tree) == max(values)

    # Test array2bst
    l_values = [1, 2, 3, 4, 5, 6, 7]
    print(l_values)
    tree1 = array2bst(l_values)
    tree1.draw()
    data = [4, 2, 6, 1, 3, 5, 7]
    tree2 = BinarySearchTree()
    for x in data:
        tree2.insert(x)
    assert tree1 == tree2
