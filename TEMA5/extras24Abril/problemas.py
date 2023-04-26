# -*- coding: utf-8 -*-
from bst import BinarySearchTree
from bintree import BinaryTree, BinaryNode


def sum_k_smallest(tree: BinarySearchTree, k: int) -> int:
    """returns the sum of the k smallest elements of tree1. If
    k > size(tree1), returns the sum of all elements.
    This is the least efficient in terms of spacial complexity
    because it uses a python list to save the in-order list"""

    if not isinstance(k, int) or k < 0:
        print(k, " must be an integer >= 0")
        return 0
    if tree is None:
        return 0

    elements = tree.inorder_list()
    result = 0
    min_size = min(k, len(elements))
    for i in range(min_size):
        result += elements[i]
    # result = sum(elements[:min_size])

    return result


def sum_k_smallest2(tree: BinarySearchTree, k: int) -> int:
    """This version is more efficient than the previous because
    it does not use a Python list to save the in-order traverse"""
    if not isinstance(k, int) or k < 0:
        print(k, " must be an integer >= 0")
        return 0
    if tree is None:
        return 0

    """returns the sum of the k smallest elements of tree1. If
    k > size(tree1), returns the sum of all elements"""
    k_sum = 0 # saves the sum for the previous nodes
    _, k_sum = __sum_k_smallest(tree.root, k, k_sum)
    return k_sum


def __sum_k_smallest(node: BinaryNode, k: int, sum_so_far: int) -> (int, int):
    if node is not None and k != 0:
        k, sum_so_far = __sum_k_smallest(node.left, k, sum_so_far)
        if k > 0:
            k -= 1
            sum_so_far += node.elem
        k, sum_so_far = __sum_k_smallest(node.right, k, sum_so_far)
    return k, sum_so_far


def create_tree_preorder(lst: list) -> BinaryTree:
    """takes a list that is the pre-order traverse of a binary search tree1.
    The function returns this tree1. You cannot use the BinarySearchTree class
    to create it.
    This version is the most efficient in terms of spacial complexity because
    it does not create new sub-lists"""
    if lst is None or len(lst) == 0:
        return BinaryTree()

    tree = BinaryTree()
    tree._root = _create_tree_preorder(lst, 0, len(lst)-1)
    return tree


def _create_tree_preorder(lst: list, start: int, end: int) -> BinaryNode:
    """returns the node (subtree) whose preorder traverse is equal to lst[start:end+1].
    This version is the most efficient in terms of spacial complexity because
    it does not use new sub-lists. """
    if start > end:
        # The sublist is empty
        return None
    if start <= end:
        # elem_root
        elem_root = lst[start]
        node = BinaryNode(elem_root)
        index = start
        for i in range(start+1, end+1):
            if lst[i] > elem_root:
                index = i
                break
        if index == start:
            # it does not have right child
            node.left = _create_tree_preorder(lst, start + 1, end)
            node.right = None
        else:
            node.left = _create_tree_preorder(lst, start + 1, index - 1)
            node.right = _create_tree_preorder(lst, index, end)

        return node


def create_tree_preorder2(lst: list) -> BinaryTree:
    """takes a list that is the pre-order traverse of a binary search tree1.
    The function returns this tree1. You cannot use the BinarySearchTree class
    to create it. This version is less efficient because it creates new sub-lists"""
    if lst is None or len(lst) == 0:
        return BinaryTree()

    tree = BinaryTree()
    tree._root = _create_tree_preorder2(lst)
    return tree


def _create_tree_preorder2(lst) -> BinaryNode:
    """creates a node (subtree) whose preorder traverse is equal to lst.
    This version is less efficient in terms of spacial complexity"""
    if len(lst) == 0:
        return None

    node = BinaryNode(lst[0])
    if len(lst) > 1:
        index = 0
        for i in range(1, len(lst)):
            if lst[i] > lst[0]:
                index = i
                break
        if index == 0:
            # it does not have right child
            node.right = None
            node.left = _create_tree_preorder2(lst[1:])
        else:
            node.right = _create_tree_preorder2(lst[index:])
            node.left = _create_tree_preorder2(lst[1:index])

    return node


def create_tree_level(lst: list) -> BinaryTree:
    """returns a BinaryTree (which must  be a binary search tree1) whose
    level order is lst"""
    if lst is None or len(lst) == 0:
        return BinaryTree()
    root = None
    for elem in lst:
        root = _create_tree_level(root, elem)
    tree = BinaryTree()
    tree._root = root
    return tree


def _create_tree_level(node: BinaryNode, elem: int) -> BinaryNode:
    if node is None:
        return BinaryNode(elem)
    if elem <= node.elem:
        node.left = _create_tree_level(node.left, elem)
    else:
        node.right = _create_tree_level(node.right, elem)
    return node


def distance(tree: BinarySearchTree, a: int, b: int) -> int:
    if tree is None:
        print('tree1 is empty')
        return -1
    node_a = tree.search(a)
    node_b = tree.search(b)
    if node_a is None:
        print(a, 'does not exist in the tree1')
        return -1
    if node_b is None:
        print(b, 'does not exist in the tree1')
        return -1
    return _distance(tree.root, a, b)


def _distance(node: BinaryNode, a: int, b: int) -> int:
    if node is None:
        return 0
    if a < node.elem and b < node.elem:
        return _distance(node.left, a, b)
    elif a > node.elem and b > node.elem:
        return _distance(node.right, a, b)
    else:
        # a <= node.elem <= b or b <= node.elem <= a:
        # distance node
        return _distance_from_ancestor(node, a) + _distance_from_ancestor(node, b)


def _distance_from_ancestor(node: BinaryNode, a: int) -> int:
    """node is always ancestor of a """
    if node is None:
        return 0
    if node.elem == a:
        return 0
    if a < node.elem:
        return 1 + _distance_from_ancestor(node.left, a)
    return 1 + _distance_from_ancestor(node.right, a)


if __name__ == "__main__":


    # test problema 1, sum_k_smallest
    input_tree = BinarySearchTree()
    for x in [25, 10, 15, 30, 25]:
        input_tree.insert(x)
    input_tree.draw()

    for j in range(-1, input_tree.size() + 3):
        print("sum_k_smallest(,{})={}".format(j, sum_k_smallest(input_tree, j)))

        print("sum_k_smallest(,{})={}".format(j, sum_k_smallest2(input_tree, j)))


    """ 
    # test para el problema 2
    input_list = [50, 30, 15, 45, 80, 65, 70, 90, 100]
    input_tree = create_tree_preorder(input_list)
    input_tree.draw()
    #  we could check it automatically comparing with its preorder traverse
    lst_pre = input_tree.preorder_list()
    assert lst_pre == input_list

    input_tree = create_tree_preorder2(input_list)
    input_tree.draw()
    assert lst_pre == input_list
    """
    """
    # test para problema 3
    input_list = [50, 15, 60, 5, 20, 65, 70]
    result_tree = create_tree_level(input_list)
    result_tree.draw()

    level_order = result_tree.level_order_list()
    assert input_list == level_order
    """

    """
    # test para problema 4
    input_list = [50, 30, 15, 45, 80, 65, 70, 90, 100]
    input_tree = BinarySearchTree()
    for m in input_list:
        input_tree.insert(m)

    input_tree.draw()
    a, b = 80, 100
    print("distance({},{})={}".format(a, b, distance(input_tree, a, b)))
    a, b = 70, 100
    print("distance({},{})={}".format(a, b, distance(input_tree, a, b)))
    a, b = 90, 70
    print("distance({},{})={}".format(a, b, distance(input_tree, a, b)))
    a, b = 45, 100
    print("distance({},{})={}".format(a, b, distance(input_tree, a, b)))
    a, b = 45, 15
    print("distance({},{})={}".format(a, b, distance(input_tree, a, b)))
    a, b = 50, 15
    print("distance({},{})={}".format(a, b, distance(input_tree, a, b)))
    """
