# -*- coding: utf-8 -*-

from bintree import BinaryNode
from bintree import BinaryTree


class BinarySearchTree(BinaryTree):

    def search(self, elem: object) -> BinaryNode:
        """Returns the node whose elem is elem"""
        return self._search(self._root, elem)

    def _search(self, node: BinaryNode, elem: object) -> BinaryNode:
        """recursive function to search elem in the subtree node.
        Returns the node if elem exists, None eoc"""
        result = None
        if node is None or node.elem == elem:
            result = node
        elif elem < node.elem:
            result = self._search(node.left, elem)
        elif elem > node.elem:
            result = self._search(node.right, elem)
        return result

    def insert(self, elem: object) -> None:
        """insert a new node containing this element"""
        self._root = self._insert(self._root, elem)

    def _insert(self, node: BinaryNode, elem: object) -> BinaryNode:
        """recursive function to insert a new node in the subtree node.
        Returns the new node.
        This method is protected because it will be used in AVL"""
        if node is None:
            node = BinaryNode(elem)
        elif node.elem == elem:
            print('Error: elem already exist ', elem)
        elif elem < node.elem:
            node.left = self._insert(node.left, elem)
        else:  # elem>node.elem
            node.right = self._insert(node.right, elem)
        return node

    def remove(self, elem: object) -> None:
        # update the root with the new subtree after remove elem
        self._root = self._remove(self._root, elem)

    @staticmethod
    def __minimum_node(node: BinaryNode) -> BinaryNode or None:
        """returns the  node with the smallest elem in the subtree node.
        This is the node that is furthest to the left.
        This is a static method because it will not modify the instance"""
        if node is None:
            return None

        min_node = node
        while min_node.left is not None:
            min_node = min_node.left
        return min_node

    def _remove(self, node: BinaryNode, elem: object) -> BinaryNode:
        """It recursively searches the node. When the node is
        found, the node has to be removed.
        Returns node after removing elem.
        This method is protected because it will be used in AVL
        """
        if node is None:
            print(elem, ' not found')
        elif elem < node.elem:
            node.left = self._remove(node.left, elem)
        elif elem > node.elem:
            node.right = self._remove(node.right, elem)
        else:  # node.elem == elem, node is the node to remove!!!
            if node.left is None and node.right is None:
                # Case 1: node is a leave
                node = None
            elif node.left is None:  # Case 2: only has a right child
                node = node.right
            elif node.right is None:    # Case 2: only has a left child
                node = node.left
            else:  # Case 3: node.left!=None and node.right!=None
                # we search the smallest node from its right child
                successor = self.__minimum_node(node.right)
                # we replace elem with the elem of the successor
                node.elem = successor.elem
                # now, we have to remove successor from the right child
                node.right = self._remove(node.right, successor.elem)

        return node

    def searchit(self, elem: object) -> BinaryNode:
        """iterative function to search an elem in a BST. It
        returns the node that contains this elem."""
        node = self._root
        result = None
        found = False
        while not found and node:
            if node.elem == elem:
                result = node
                found = True
            elif elem < node.elem:
                node = node.left
            else:
                node = node.right
        return result

    def insert_it(self, elem: object) -> None:
        """iterative version of insert"""
        if self._root is None:
            self._root = BinaryNode(elem)  # if input_tree is empty, new node will be the root
            return  # we can leave!!!

        node = self._root  # to search the place
        not_exist = True
        while not_exist and node:
            if elem < node.elem:
                if node.left is None:  # this is the place to insert it
                    node.left = BinaryNode(elem)
                    not_exist = False
                else:
                    node = node.left

            elif elem > node.elem:
                if node.right is None:  # this is the place to insert it
                    node.right = BinaryNode(elem)
                    not_exist = False
                else:
                    node = node.right

            else:  # elem == node.elem
                print('duplicate elements not allowed!!')
                not_exist = False


if __name__ == "__main__":
    """
    tree1 = BinarySearchTree()
    input_list = [50, 55, 54, 20, 60, 15, 18, 5, 25, 24, 75, 80]
    for m in input_list:
        tree1.insert(m)
        # you can see the input_tree after each insertion
        # print('after insert: ', m)
        # tree1.draw()

    # show the resulting input_tree
    tree1.draw()
    
    # Test insert_iterative
    tree2 = BinarySearchTree()
    for m in input_list:
        tree2.insert_it(m)
        # you can see the input_tree after each insertion
        # print('after insert: ', m)
        # tree2.draw()

    # show the resulting input_tree
    tree2.draw()

    # both trees should be equal
    assert(tree1 == tree2)
"""
    """
    input_tree = BinarySearchTree()
    for m in [18, 11, 23, 5, 15, 20, 24, 9, 22, 21, 6, 8, 7]:
        input_tree.insert(m)
    input_tree.draw()
    print('size:', input_tree.size())
    print('height:', input_tree.height())

    input_tree.remove(18)
    print("after remove 18 (root), replaced with its successor 20")
    input_tree.draw()

    input_tree.remove(7)
    print("after remove 7 (a leaf)")
    input_tree.draw()

    input_tree.remove(8)
    print("after remove 8 (a leaf)")
    input_tree.draw()

    input_tree.remove(5)
    print("after remove 5 (only a child), replaced with its child: 9")
    input_tree.draw()

    input_tree.remove(9)
    print("after remove 9 (only a child), replaced with its left child: 6")
    input_tree.draw()

    input_tree.remove(11)
    print("after remove 11 (two children), replaced with its successor: 15")
    input_tree.draw()

    input_tree.remove(20)
    print("after remove 20 (root), two children, replaced with its successor: 21")
    input_tree.draw()

    input_tree.remove(15)
    print("after remove 15 (only left child) -> 6")
    input_tree.draw()

    input_tree.remove(6)
    print("after remove 6 (a leaf)")
    input_tree.draw()

    input_tree.remove(8)
    print("after remove 8 (does not exist)")
    input_tree.draw()

    input_tree.remove(24)
    print("after remove 24 (a leaf)")
    input_tree.draw()
    print()
    """
    input_tree = BinarySearchTree()
    for x in [5, 10, 15, 20, 23, 22, 24, 3, 7]:
        input_tree.insert(x)
    input_tree.draw()

    input_tree.remove(24)
    print("after remove 24, a leaf")
    input_tree.draw()

    input_tree.remove(23)
    print("after remove 23 (only has a left child)")
    input_tree.draw()

    input_tree.remove(20)
    print("after remove 20 (only has a right child)")
    input_tree.draw()

    input_tree.remove(22)
    print("after remove 22 (a leaf)")
    input_tree.draw()

    input_tree.remove(10)
    print("after remove 10 (two children)")
    input_tree.draw()

    input_tree.remove(5)
    print("after remove 5 (root with two children)")
    input_tree.draw()

    for x in [11, 10, 30]:
        input_tree.insert(x)
    print('after insert [11, 10, 30]')
    input_tree.draw()

    input_tree.remove(3)
    print("after remove 3 (leaf)")
    input_tree.draw()

    input_tree.remove(7)
    print("after remove 7 root with only right child")
    input_tree.draw()

    input_tree.remove(30)
    print("after remove 30, a leaf")
    input_tree.draw()

    input_tree.remove(15)
    print("after remove 15 root with only left child")
    input_tree.draw()
