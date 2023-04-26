from bintree import BinaryTree, BinaryNode
from bst import BinarySearchTree
import sys

class MyBinaryTree(BinaryTree):
    def mirror(self) -> None:
        """transform it to its mirror version"""
        self.__mirror(self._root)

    def __mirror(self, node: BinaryNode) -> None:
        if node:
            # we transform the left child
            self.__mirror(node.left)
            # we transform the right child
            self.__mirror(node.right)
            # swap the children
            node.left, node.right = node.right, node.left

    def is_bst(self) -> bool:
        """gets a binary input_tree and checks if the input_tree is bst.
        Worst case: we have to visit all nodes, O(n)
        Best case: input_tree is empty"""
        return self.__is_bst(self._root, -sys.maxsize, sys.maxsize)

    def __is_bst(self, node: BinaryNode, min_value: int, max_value: int) -> bool:
        if node is None:
            return True

        return (min_value <= node.elem <= max_value) and \
            self.__is_bst(node.left, min_value, node.elem - 1) \
            and self.__is_bst(node.right, node.elem + 1, max_value)

    def print_grandchild_10(self) -> None:
        self._print_grandchild_10(self._root, None, None)

    def _print_grandchild_10(self, node: BinaryNode,
                             parent: BinaryNode,
                             grand: BinaryNode) -> None:
        if node is None:
            return
        if grand and grand.elem % 10 == 0:
            print(node.elem, end=' ')
        self._print_grandchild_10(node.left, node, parent)
        self._print_grandchild_10(node.right, node, parent)


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
    input_tree = MyBinaryTree()
    input_tree._root = root

    # Test
    print("Before mirror()")
    input_tree.draw()
    input_tree.mirror()
    print("After mirror()")
    input_tree.draw()

    # Test para is_bst (False)
    print("is BST?", input_tree.is_bst())
    # Test para is_bst (True)
    aux_tree = BinarySearchTree()
    for x in [50, 25, 75, 10, 30, 60]:
        aux_tree.insert(x)
    input_tree2 = MyBinaryTree()
    input_tree2._root = aux_tree.root
    input_tree2.draw()

    print("is BST?", input_tree2.is_bst())

    """
    aux_tree = BinarySearchTree()
    for x in [50, 20, 60, 15, 55, 70, 10, 18, 75, 8, 93]:
        aux_tree.insert(x)
    aux_tree.draw()
    input_tree = MyBinaryTree()
    input_tree._root = aux_tree.root

    input_tree.print_grandchild_10()
    """
