from bst import BinarySearchTree
from bintree import BinaryNode

"""Problema 1: Implementa una función (iterativa o recursiva) 
que reciba un árbol binario de búsqueda (de elementos de tipo entero) 
y devuelva el elemento más pequeño del árbol. ¿Cuál es su complejidad temporal?
"""


def get_smallest_ite(tree: BinarySearchTree) -> int:
    """returns the smallest element in tree. O(log n)"""
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
    """returns the greatest element in tree. O(log n)"""
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
    """returns the smallest element in tree"""
    result = None
    if tree is None:
        print("Tree is None!!!")
    else:
        result = _get_smallest_rec(tree.root)
    return result


def _get_smallest_rec(node: BinaryNode) -> int:
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
        print("tree is None!!!")
    else:
        elements = tree.inorder_list()
        result = sum(elements)
    return result


def sum_elements_rec(tree: BinarySearchTree) -> int:
    """returns the sum of the elements. O(n)"""
    result = None
    if tree is None:
        print("tree is None!!!")
    else:
        result = _sum_elements_rec(tree.root)
    return result


def _sum_elements_rec(node: BinaryNode) -> int:
    """returns the sum of all elements in the subtree node"""
    result = 0
    if node is not None:
        result = node.elem + _sum_elements_rec(node.left) + _sum_elements_rec(node.right)
    return result


def _maximum_node(subtree: BinaryNode) -> BinaryNode:
    """gets a node (subtree) and returns the node with the biggest
    element in the subtree. O(log n)"""
    result = None
    if subtree is not None:
        biggest = subtree
        while biggest.right:
            biggest = biggest.right
        result = biggest
    return result


def _remove(node: BinaryNode, elem: object) -> BinaryNode:
    """It recursively searches the node. When the node is
    found, the node has to be removed"""
    if node is None:
        print(elem, ' not found')
    elif elem < node.elem:
        node.left = _remove(node.left, elem)
    elif elem > node.elem:
        node.right = _remove(node.right, elem)
    else:  # node.elem == elem, node is the node to remove!!!
        if node.left is None and node.right is None:
            # Case 1: node is a leave
            node = None
        elif node.left is None:  # Case 2: only has a right child
            node = node.right
        elif node.right is None:    # Case 2: only has a left child
            node = node.left
        else:  # Case 3: node.left!=None and node.right!=None
            # we search the biggest node from its left child
            predecessor = _maximum_node(node.left)
            # we replace elem with the elem of the successor
            node.elem = predecessor.elem
            # now, we have to remove successor from the right child
            node.left = _remove(node.left, predecessor.elem)

        return node


class BSTRemove2(BinarySearchTree):
    def remove(self, elem: object) -> None:
        # update the root with the new subtree after remove elem
        self._root = _remove(self._root, elem)

if __name__ == "__main__":

    input_tree = BinarySearchTree()
    values = [25, 20, 36, 10, 22, 30, 40, 5, 12, 28, 38, 48]
    for x in values:
        input_tree.insert(x)
    input_tree.draw()

    """
    print("Smallest element: ", get_smallest_ite(input_tree))
    assert get_smallest_ite(input_tree) == min(values)

    print("Smallest element: ", get_smallest_rec(input_tree))
    print("Smallest element: ", get_smallest_rec(None))
    print("Smallest element: ", get_smallest_rec(BinarySearchTree()))
    assert get_smallest_rec(input_tree) == min(values)

    print("Greatest element: ", get_greatest_ite(None))
    print("Greatest element: ", get_greatest_ite(BinarySearchTree()))
    print("Greatest element: ", get_greatest_ite(input_tree))
    assert get_greatest_ite(input_tree) == max(values)

    print("sum of all elements: ", sum_elements(None))
    print("sum of all elements: ", sum_elements(BinarySearchTree()))
    print("sum of all elements: ", sum_elements(input_tree))
    assert sum_elements(input_tree) == sum(values)

    print("sum of all elements: ", sum_elements_rec(None))
    print("sum of all elements: ", sum_elements_rec(BinarySearchTree()))
    print("sum of all elements: ", sum_elements_rec(input_tree))
    assert sum_elements_rec(input_tree) == sum(values)
    """

    """
    for x in values:
        node = input_tree.search(x)
        if node is not None:
            small_n = smallest_node(node)
            print(small_n.elem, " is the smallest node in ", node.elem )
    print()
    """

    input_tree2 = BSTRemove2()
    values = [25, 20, 36, 10, 22, 30, 40, 5, 12, 28, 38, 48]
    for x in values:
        input_tree2.insert(x)
    input_tree2.draw()
    input_tree2.remove(25)
    input_tree2.draw()

    input_tree.remove(25)
    input_tree.draw()
