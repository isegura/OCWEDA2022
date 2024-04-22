# -*- coding: utf-8 -*-
# Implementation of Binary Tree
# A node only saves the references to its children

from queue import Queue


class BinaryNode:
    def __init__(self, elem: object,
                 node_left: 'BinaryNode' = None,
                 node_right: 'BinaryNode' = None) -> None:
        self.elem = elem
        self.left = node_left
        self.right = node_right

    def __eq__(self, other: 'BinaryNode') -> bool:
        """checks if two nodes (subtrees) are equal o not"""
        return other is not None and self.elem == other.elem and \
            self.left == other.left and self.right == other.right

    def __str__(self) -> str:
        return str(self.elem)


class BinaryTree:
    def __init__(self) -> None:
        """creates an empty binary input_tree
        I only has an attribute: _root"""
        self._root = None

    @property
    def root(self):
        return self._root

    def __eq__(self, other_tree: 'BinaryTree') -> bool:
        """checks if two binary trees are equal o not"""
        return other_tree is not None and self._root == other_tree._root

    def size(self) -> int:
        """Returns the number of nodes"""
        return self._size(self._root)

    def _size(self, node: BinaryNode) -> int:
        """return the size of the subtree from node."""
        if node is None:
            return 0
        return 1 + self._size(node.left) + self._size(node.right)

    def height(self) -> int:
        """Returns the height of the input_tree"""
        return self._height(self._root)

    def _height(self, node: BinaryNode) -> int:
        """returns the height of node. It's protected because
        this method will be used in AVL"""
        if node is None:
            return -1

        return 1 + max(self._height(node.left), self._height(node.right))

    def preorder(self) -> None:
        """prints the preorder (root, left, right) traversal of the input_tree"""
        print('Preorder traversal: ', end=' ')  # end=' ' avoid the newline
        self.__preorder(self._root)
        print()

    def __preorder(self, node: BinaryNode) -> None:
        """prints the preorder (root, left, right) traversal of the subtree
        than hangs from node"""
        if node is not None:
            print(node.elem, end=' ')  # end=' ' avoid new line
            self.__preorder(node.left)
            self.__preorder(node.right)

    def preorder_list(self) -> list:
        """returns a list with the preorder traversal"""
        # self.draw()
        result = []
        self.__preorder_list(self._root, result)
        return result

    def __preorder_list(self, node: BinaryNode, pre_list: list) -> None:
        """populates pre_list with the preorder traversal of the subtree node"""
        if node is not None:
            pre_list.append(node.elem)
            self.__preorder_list(node.left, pre_list)
            self.__preorder_list(node.right, pre_list)

    def postorder(self) -> None:
        """prints the postorder (left, right, root)  traversal of the input_tree"""
        # self.draw()
        print('Postorder traversal: ', end=' ')  # end=' ' avoid the newline
        self.__postorder(self._root)
        print()

    def __postorder(self, node: BinaryNode) -> None:
        """prints the postorder (left, right, root) traversal of the subtree
        than hangs from node"""
        if node is not None:
            self.__postorder(node.left)
            self.__postorder(node.right)
            print(node.elem, end=' ')  # end=' ' avoid new line

    def postorder_list(self) -> list:
        """returns a list with the postorder traversal of the input_tree"""
        # self.draw()
        result = []
        self.__postorder_list(self._root, result)
        return result

    def __postorder_list(self, node: BinaryNode, post_list: list) -> None:
        """populates post_list with the postorder traversal of the subtree node"""
        if node is not None:
            self.__postorder_list(node.left, post_list)
            self.__postorder_list(node.right, post_list)
            post_list.append(node.elem)

    def inorder(self) -> None:
        """prints the inorder (left, root, right)  traversal of the input_tree"""
        # self.draw()
        print('Inorder traversal: ', end=' ')  # end=' ' avoid the newline
        self.__inorder(self._root)
        print()

    def inorder_list(self) -> list:
        """returns a list with the inorder traversal of the input_tree"""
        # self.draw()
        result = []
        self.__inorder_list(self._root, result)
        return result

    def __inorder(self, node: BinaryNode) -> None:
        """prints the inorder (left, root, right) traversal of the subtree
        than hangs from node"""
        if node is not None:
            self.__inorder(node.left)
            print(node.elem, end=' ')  # end=' ' avoid new line
            self.__inorder(node.right)

    def __inorder_list(self, node: BinaryNode, in_list: list) -> None:
        """populates in_list with the inorder traversal of the subtree node"""
        if node is not None:
            self.__inorder_list(node.left, in_list)
            in_list.append(node.elem)
            self.__inorder_list(node.right, in_list)

    def level_order(self) -> None:
        """prints the level order of the input_tree. O(n)"""
        if self._root is None:
            print('input_tree is empty')
        else:
            print("Level order: ", end=' ')  # avoid the new line

            # we can use SList with tail and head
            queue_nodes = Queue()
            queue_nodes.put(self._root)
            while queue_nodes.qsize() > 0:  # loop will be executed the size of input_tree: n
                current = queue_nodes.get()
                print(current.elem, end=' ')
                if current.left is not None:
                    queue_nodes.put(current.left)  # O(1)
                if current.right is not None:
                    queue_nodes.put(current.right)  # O(1)
            print()

    def level_order_list(self) -> list:
        """prints the level order of the input_tree. O(n)"""
        result = []
        if self._root is not None:
            # we can use SList with tail and head
            queue_nodes = Queue()
            queue_nodes.put(self._root)

            while queue_nodes.qsize() > 0:  # loop will be executed the size of input_tree: n
                current = queue_nodes.get()  # O(1)
                result.append(current.elem)
                if current.left is not None:
                    queue_nodes.put(current.left)  # O(1)
                if current.right is not None:
                    queue_nodes.put(current.right)  # O(1)

        return result

    def get_depth(self, elem: int) -> int:
        """gets elem, and returns the level of its nodes.
         If elem does not exist in the tree, it returns -1.
         Time complexity: O(n), best case: root empty or elem == root.elem, O(1)
         worst case: elem does not exist into the list, because we have to traverse all nodes: O(1)
         Space complexity: n (tree) + n (queue_nodes) = 2n """
        if self._root is not None:
            # we can use SList with tail and head
            queue_nodes = Queue()
            # save the root and its level
            queue_nodes.put((self._root, 0))

            while queue_nodes.qsize() > 0:  # loop will be executed the size of input_tree: n
                current_tuple = queue_nodes.get()  # O(1)

                current = current_tuple[0]  # the first element of the tuple is the node
                level = current_tuple[1]    # the second element of the tuple is the level

                if current.elem == elem:
                    return level

                if current.left is not None:
                    queue_nodes.put((current.left, level+1))  # O(1)
                if current.right is not None:
                    queue_nodes.put((current.right, level+1))  # O(1)

        return -1

    def get_depth_rec(self, elem: int) -> int:
        """recursive method to get the depth of an element.
        If elem does not exist, it returns -1
        """
        return self._get_depth_rec(elem, self._root, 0)

    def _get_depth_rec(self, elem: int, node: BinaryNode, level: int) -> (int or None):
        if node is None:
            return None
        if node.elem == elem:
            return level
        left_level = self._get_depth_rec(elem, node.left, level+1)
        if left_level != -1:
            # we have found it in its left subtree
            return left_level
        # As the element was not found in the left subtree,
        # we also have to search it in the right subtree
        return self._get_depth_rec(elem, node.right, level+1)

    def draw(self) -> None:
        """function to draw an input_tree. """
        if self._root:
            self._draw('', self._root, False)
        else:
            print('input_tree is empty')
        print('\n\n')

    def _draw(self, prefix: str, node: BinaryNode, is_left: bool) -> None:
        if node is not None:
            self._draw(prefix + "     ", node.right, False)
            print(prefix + "|-- " + str(node.elem))
            self._draw(prefix + "     ", node.left, True)


if __name__ == '__main__':
    tree = BinaryTree()
    newNode = BinaryNode(2)
    left = BinaryNode(3, newNode, None)
    right = BinaryNode(9)
    right.left = BinaryNode(8)
    right.right = BinaryNode(20)
    rrNode = right.right
    rrNode.right = BinaryNode(30)

    root = BinaryNode(5, left, right)
    tree._root = root
    # Show the input_tree
    tree.draw()

    # size, height
    print('Size of the input_tree:', tree.size())
    print('Height of the input_tree:', tree.height())
    print()

    # traversals
    tree.preorder()
    tree.postorder()
    tree.inorder()
    # save into a list
    print("Preorder: ", tree.preorder_list())
    print("Postorder: ", tree.postorder_list())
    print("Inorder: ", tree.inorder_list())
    tree.level_order()
    # save into a list
    print("Level order:", tree.level_order_list())
    print()

