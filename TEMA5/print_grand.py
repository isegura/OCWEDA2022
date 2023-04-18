from bst import BinarySearchTree
from bintree import BinaryNode


class MyBST(BinarySearchTree):
    def print_grandchild_10(self) -> None:
        self._print_grandchild_10(self._root, None, None)

    def _print_grandchild_10(self, node: BinaryNode, parent: BinaryNode,
                             grand: BinaryNode) -> None:
        if node is None:
            return
        if grand and grand.elem % 10 == 0:
            print(node.elem, end=' ')
        self._print_grandchild_10(node.left, node, parent)
        self._print_grandchild_10(node.right, node, parent)


if __name__ == "__main__":
    tree = MyBST()
    for x in [50, 20, 60, 15, 55, 70, 10, 18, 75, 8, 93]:
        tree.insert(x)
    tree.draw()
    tree.print_grandchild_10()
