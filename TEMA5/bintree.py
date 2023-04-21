# -*- coding: utf-8 -*-
# Implementation of Binary Tree
# A node only saves the references to its children

from TEMA2.slistHT import SList


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


"""Auxiliary functions"""
def _size(node: BinaryNode) -> int:
    """return the size of the subtree from node"""
    if node is None:
        return 0
    return 1 + _size(node.left) + _size(node.right)

def _height(node: BinaryNode) -> int:
    """returns the height of node"""
    if node is None:
        return -1

    return 1 + max(_height(node.left), _height(node.right))

def _preorder(node: BinaryNode) -> None:
    """prints the preorder (root, left, right) traversal of the subtree
    than hangs from node"""
    if node is not None:
        print(node.elem, end=' ')  # end=' ' avoid new line
        _preorder(node.left)
        _preorder(node.right)

def _preorder_list(node: BinaryNode, pre_list: list) -> None:
    """populates pre_list with the preorder traversal of the subtree node"""
    if node is not None:
        pre_list.append(node.elem)
        _preorder_list(node.left, pre_list)
        _preorder_list(node.right, pre_list)

def _postorder(node: BinaryNode) -> None:
    """prints the postorder (left, right, root) traversal of the subtree
    than hangs from node"""
    if node is not None:
        _postorder(node.left)
        _postorder(node.right)
        print(node.elem, end=' ')  # end=' ' avoid new line

def _postorder_list(node: BinaryNode, post_list: list) -> None:
    """populates post_list with the postorder traversal of the subtree node"""
    if node is not None:
        _postorder_list(node.left, post_list)
        _postorder_list(node.right, post_list)
        post_list.append(node.elem)

def _inorder(node: BinaryNode) -> None:
    """prints the inorder (left, root, right) traversal of the subtree
    than hangs from node"""
    if node is not None:
        _inorder(node.left)
        print(node.elem, end=' ')  # end=' ' avoid new line
        _inorder(node.right)

def _inorder_list(node: BinaryNode, in_list: list) -> None:
    """populates in_list with the inorder traversal of the subtree node"""
    if node is not None:
        _inorder_list(node.left, in_list)
        in_list.append(node.elem)
        _inorder_list(node.right, in_list)

class BinaryTree:
    def __init__(self) -> None:
        """creates an empty binary input_tree
        I only has an attribute: _root"""
        self._root = None

    def __eq__(self, other_tree: 'BinaryTree') -> bool:
        """checks if two binary trees are equal o not"""
        return other_tree is not None and self._root == other_tree._root

    def size(self) -> int:
        """Returns the number of nodes"""
        return _size(self._root)

    def height(self) -> int:
        """Returns the height of the input_tree"""
        return _height(self._root)

    def preorder(self) -> None:
        """prints the preorder (root, left, right) traversal of the input_tree"""
        # self.draw()
        print('Preorder traversal: ', end=' ')  # end=' ' avoid the newline
        _preorder(self._root)
        print()

    def preorder_list(self) -> list:
        """returns a list with the preorder traversal"""
        # self.draw()
        result = []
        _preorder_list(self._root, result)
        return result

    def postorder(self) -> None:
        """prints the postorder (left, right, root)  traversal of the input_tree"""
        # self.draw()
        print('Postorder traversal: ', end=' ')  # end=' ' avoid the newline
        _postorder(self._root)
        print()

    def postorder_list(self) -> list:
        """returns a list with the postorder traversal of the input_tree"""
        # self.draw()
        result = []
        _postorder_list(self._root, result)
        return result

    def inorder(self) -> None:
        """prints the inorder (left, root, right)  traversal of the input_tree"""
        # self.draw()
        print('Inorder traversal: ', end=' ')  # end=' ' avoid the newline
        _inorder(self._root)
        print()

    def inorder_list(self) -> list:
        """returns a list with the inorder traversal of the input_tree"""
        # self.draw()
        result = []
        _inorder_list(self._root, result)
        return result

    def level_order(self) -> None:
        """prints the level order of the input_tree. O(n)"""
        if self._root is None:
            print('input_tree is empty')
        else:
            print("Level order: ", end=' ')  # avoid the new line

            # we can use SList with tail and head
            list_nodes = SList()
            list_nodes.add_last(self._root)
            while len(list_nodes) > 0:  # loop will be executed the size of input_tree: n
                current = list_nodes.remove_first()
                print(current.elem, end=' ')
                if current.left is not None:
                    list_nodes.add_last(current.left)  # O(1)
                if current.right is not None:
                    list_nodes.add_last(current.right)  # O(1)

            print()

    def level_order_list(self) -> list:
        """prints the level order of the input_tree. O(n)"""
        result = []
        if self._root is not None:
            # we can use SList with tail and head
            list_nodes = SList()
            list_nodes.add_last(self._root)

            while len(list_nodes) > 0:  # loop will be executed the size of input_tree: n
                current = list_nodes.remove_first()  # O(1)
                result.append(current.elem)
                if current.left is not None:
                    list_nodes.add_last(current.left)  # O(1)
                if current.right is not None:
                    list_nodes.add_last(current.right)  # O(1)

        return result


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


    def depth(self, node: BinaryNode) -> int:
        """ returns the depth of the node; this is the length from
        the root to the node"""

        if self._root is None:
            print('Error: the input_tree is empty')
            return None

        # we can use SList with tail and head
        depth_level = 0

        list_nodes = SList()
        list_nodes.add_last(self._root)

        while len(list_nodes) > 0:  # loop will be executed the size of input_tree: n
            current = list_nodes.remove_first()  # O(1)
            if current == node:
                return depth_level
            if current.left and node.elem < current.elem:
                list_nodes.add_last(current.left)  # O(1)
            if current.right and node.elem > current.elem:
                list_nodes.add_last(current.right)  # O(1)
            depth_level += 1

        print('Not found ', node.elem)
        return None

    @property
    def root(self):
        return self._root


# function to obta





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
    print('root of the input_tree:', _height(root))
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

    # depth of some nodes
    print('depth of root:', tree.depth(root))
    print('depth of root.left:', tree.depth(left))
    print('depth of root.right:', tree.depth(right))
    print('depth of root.right.left:', tree.depth(right.left))
    print('depth of root.right.right.right:', tree.depth(rrNode.right), rrNode.right.elem)
