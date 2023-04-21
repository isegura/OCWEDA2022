from bst import BinarySearchTree
from bintree import BinaryTree, BinaryNode


def inorder(tree: BinarySearchTree) -> list:
    """returns the in-order traverse of tree into a Python list"""
    if tree is None:
        return []
    result_lst = []
    _inorder(tree.root, result_lst)
    return result_lst


def _inorder(node: BinaryNode, lst: list) -> None:
    """saves the elements in the subtree node in order list"""
    if node:
        _inorder(node.left, lst)
        lst.append(node.elem)
        _inorder(node.right, lst)


def sum_k_smallest(tree: BinarySearchTree, k: int) -> int:
    """returns the sum of the k smallest elements of tree. If
    k > size(tree), returns the sum of all elements"""

    if not isinstance(k, int) or k < 0:
        print(k, " must be an integer >= 0")
        return 0
    if tree is None:
        return 0

    elements = inorder(tree)
    result = 0
    min_size = min(k, len(elements))
    for i in range(min_size):
        result += elements[i]
    # result = sum(elements[:min_size])

    return result


def check_inorder(tree: BinarySearchTree, lst: list) -> bool:
    lst_inorder = inorder(tree)
    return lst == lst_inorder


def check_inorder2(tree: BinarySearchTree, lst: list) -> bool:
    if tree is None:
        return (lst is None or len(lst) == 0)

    aux_list = lst.copy()
    _check_inorder(tree.root, aux_list)
    return len(lst) == 0


def _check_inorder(node: BinaryNode, lst: list) -> None:
    if node:
        _check_inorder(node.left, lst)
        lst.pop(0)
        _check_inorder(node.right, lst)


def create_tree_preorder(lst: list) -> BinaryTree:
    if lst is None or len(lst) == 0:
        return BinaryTree()

    root = _create_tree_preorder(lst, 0)
    tree = BinaryTree()
    tree.root = root

def _create_tree_preorder(lst: list, start: int) -> BinaryNode:

    root = BinaryNode(lst[start])
    index = -1
    for i in range(start, len(lst)):
        if lst[i] > lst[start]:
            index = i
            break
    if index > start + 1:
        root.left = BinaryNode(lst[start + 1])
    root.right = BinaryNode(lst[index])

if __name__ == "__main__":
    """
    input_tree = BinarySearchTree()
    # input_tree = BinarySearchTree()
    for x in [5, 10, 15, 20, 23, 22, 24, 3, 7]:
        input_tree.insert(x)
    input_tree.draw()

    for k in range(-1, 12):
        print("sum_k_smallest(,{})={}".format(k, sum_k_smallest(input_tree, k)))
    """

    input_tree = BinarySearchTree()
    # input_tree = BinarySearchTree()
    data = [50, 60, 30, 15, 20]
    for x in data:
        input_tree.insert(x)
    input_tree.draw()

    input_list = sorted(data)
    # input_list = data.copy()
    # print("check_postorder(,{}) = {}".format(data, check_inorder(input_tree, input_list)))
    print("check_postorder(,{}) = {}".format(data, check_inorder2(input_tree, input_list)))
