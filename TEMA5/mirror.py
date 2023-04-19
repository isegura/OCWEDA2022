from bintree import BinaryNode
from bintree import BinaryTree


def mirror(tree_input: BinaryTree) -> None:
    _mirror(tree_input._root)


def _mirror(node: BinaryNode) -> None:
    if node:
        # we transform the left child
        _mirror(node.left)
        # we transform the right child
        _mirror(node.right)
        # swap the children
        node.left, node.right = node.right, node.left


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
    tree = BinaryTree()
    tree._root = root
    tree.draw()
    mirror(tree)
    tree.draw()
