from bintree import BinaryTree, BinaryNode
import sys

def mirror(tree_input: BinaryTree) -> None:
    """gets a binary input_tree and transform it to its
    mirror version"""
    _mirror(tree_input.root)

def _mirror(node: BinaryNode) -> None:
    if node:
        # we transform the left child
        _mirror(node.left)
        # we transform the right child
        _mirror(node.right)
        # swap the children
        node.left, node.right = node.right, node.left


def is_bst(tree: BinaryTree) -> bool:
    """gets a binary input_tree and checks if the input_tree is bst.
    Worst case: we have to visit all nodes, O(n)
    Best case: input_tree is empty"""
    return _is_bst(tree.root, -sys.maxsize, sys.maxsize)


def _is_bst(node: BinaryNode, min_value: int, max_value: int) -> bool:
    if node is None:
        return True

    return min_value <= node.elem <= max_value and \
        _is_bst(node.left, min_value, node.elem - 1) \
        and _is_bst(node.right, node.elem + 1, max_value)


if __name__ == "__main__":

    root = BinaryNode(1)
    left = BinaryNode(2)
    right = BinaryNode(3)
    root.left = left
    root.right = right
    left.left = BinaryNode(4)
    left.right = BinaryNode(5)
    right.left = BinaryNode(6)
    right.right = BinaryNode(7)
    input_tree = BinaryTree()
    input_tree._root = root
    input_tree.draw()
    mirror(input_tree)
    input_tree.draw()

    print("is BST?", is_bst(input_tree))

    root = BinaryNode(50)
    left = BinaryNode(25)
    right = BinaryNode(75)
    root.right = right
    root.left = left
    left.left = BinaryNode(10)
    left.right = BinaryNode(30)
    right.left = BinaryNode(60)
    right.right = BinaryNode(80)

    input_tree = BinaryTree()
    input_tree._root = root
    input_tree.draw()

    print("is BST?", is_bst(input_tree))
