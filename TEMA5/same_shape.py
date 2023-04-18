from bst import BinarySearchTree
from bintree import BinaryNode


def same_shape(tree1: BinarySearchTree, tree2: BinarySearchTree) -> bool:
    result = False
    if tree1 is not None and tree2 is not None:
        result = _same_shape(tree1._root, tree2._root)
    return result


def _same_shape(node1: BinaryNode, node2: BinaryNode) -> bool:
    result = False
    if node1 is None and node2 is None:
        result = True
    elif node1 is not None and node2 is not None:
        result = _same_shape(node1.left, node2.left) and \
                 _same_shape(node1.right, node2.right)
    return result


if __name__ == "__main__":
    data1 = [20, 10, 30, 8]
    tree1 = BinarySearchTree()
    for x in data1:
        tree1.insert(x)

    data2 = [80, 60, 90, 5]
    tree2 = BinarySearchTree()
    for x in data2:
        tree2.insert(x)

    print(same_shape(tree1, tree2))
    print(same_shape(tree1, BinarySearchTree()))
    print(same_shape(BinarySearchTree(), tree1))
    print(same_shape(None, tree1))
