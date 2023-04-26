from bintree import BinaryTree, BinaryNode
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

    def same_shape(self, other_tree: BinaryTree) -> bool:
        result = False
        if other_tree is not None:
            result = self.__same_shape(self.root, other_tree.root)
        return result

    def __same_shape(self, node1: BinaryNode, node2: BinaryNode) -> bool:
        result = False
        if node1 is None and node2 is None:
            result = True
        elif node1 is not None and node2 is not None:
            result = self.__same_shape(node1.left, node2.left) and \
                     self.__same_shape(node1.right, node2.right)
        return result

    def update_adding_left_child(self) -> None:
        """change the value in each node to sum of all the values in the nodes in the left subtree including its own.
        Complexity: O(n) """
        self.__update_adding_left_child(self._root)

    def __update_adding_left_child(self, node: BinaryNode) -> int:
        # Base cases
        if node is None:
            return 0

        # print("changing: ", node.elem)
        if node.left is None and node.right is None:
            return node.elem

        # Update left and right subtrees
        left_sum = self.__update_adding_left_child(node.left)
        right_sum = self.__update_adding_left_child(node.right)

        # Add right_sum to current node
        node.elem += left_sum

        # Return sum of values under root
        return node.elem + right_sum


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
    input_tree.draw()
    input_tree.mirror()
    input_tree.draw()

    print("is BST?", input_tree.is_bst())

    root = BinaryNode(50)
    left = BinaryNode(25)
    right = BinaryNode(75)
    root.right = right
    root.left = left
    left.left = BinaryNode(10)
    left.right = BinaryNode(30)
    right.left = BinaryNode(60)
    right.right = BinaryNode(80)

    input_tree = MyBinaryTree()
    input_tree._root = root
    input_tree.draw()

    print("is BST?", input_tree.is_bst())
