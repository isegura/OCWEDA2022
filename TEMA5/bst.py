# -*- coding: utf-8 -*-

from bintree import BinaryNode
from bintree import BinaryTree


class BinarySearchTree(BinaryTree):

    def search(self, elem: object) -> BinaryNode:
        """Returns the node whose elem is elem"""
        return self._search(self._root, elem)

    def _search(self, node: BinaryNode, elem: object) -> BinaryNode:
        """Recursive function"""
        
        if node is None or node.elem == elem:
            return node
        elif elem < node.elem:
            return self._search(node.left, elem)
        elif elem > node.elem:
            return self._search(node.right, elem)

    def searchit(self, elem: object) -> BinaryNode:
        """iterative function to search an elem in a BST. It
        returns the node that contains this elem."""
        node = self._root
        while node:
            if node.elem == elem:
                # we have found it!!! we can return it and leave the function
                return node

            if elem < node.elem:
                node = node.left
            else:
                node = node.right
        return node

    def insert(self, elem: object) -> None:
        """insert a new node containing this element"""
        self._root = self._insert(self._root, elem)

    def _insert(self, node: BinaryNode, elem: object) -> BinaryNode:
        if node is None:
            return BinaryNode(elem)

        if node.elem == elem:
            print('Error: elem already exist ', elem)
            return node

        if elem < node.elem:
            node.left = self._insert(node.left, elem)
        else:
            # elem>node.elem
            node.right = self._insert(node.right, elem)
        return node

    def insert_iterative(self, elem: object) -> None:
        """iterative version of insert"""
        if self._root is None:
            self._root = BinaryNode(elem)  # if tree is empty, new node will be the root
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

    def _minimum_node(self, node: BinaryNode) -> BinaryNode:
        """returns the  node with the smallest elem in the subtree node.
        This is the node that is furthest to the left"""
        min_node = node
        while min_node.left is not None:
            min_node = min_node.left
        return min_node

    def remove(self, elem: object) -> None:
        # update the root with the new subtree after remove elem
        self._root = self._remove(self._root, elem)

    def _remove(self, node: BinaryNode, elem: object) -> BinaryNode:
        """It recursively searches the node. When the node is
        found, the node has to be removed"""
        if node is None:
            print(elem, ' not found')
            return node

        if elem < node.elem:
            node.left = self._remove(node.left, elem)
        elif elem > node.elem:
            node.right = self._remove(node.right, elem)
        else:
            # node.elem == elem, node is the node to remove!!!
            if node.left is None and node.right is None:
                # Case 1: node is a leave
                return None

            # Case 2: node only has a child, so the function has to return it
            if node.left is None:
                # It only has the right child
                return node.right

            elif node.right is None:
                # It only has the left child
                return node.left
            else:
                # Case 3: node.left!=None and node.right!=None
                # we search the smallest node from its right child
                successor = self._minimum_node(node.right)
                # we replace elem with the elem of the successor
                node.elem = successor.elem
                # now, we have to remove successor from the right child
                node.right = self._remove(node.right, successor.elem)

        return node


if __name__ == "__main__":
    tree1 = BinarySearchTree()
    input_list = [50, 55, 54, 20, 60, 15, 18, 5, 25, 24, 75, 80]
    for x in input_list:
        tree1.insert(x)
        # you can see the tree after each insertion
        # print('after insert: ', x)
        # tree1.draw()

    # show the resulting tree
    tree1.draw()

    # Test insert_iterative
    tree2 = BinarySearchTree()
    for x in input_list:
        tree2.insert_iterative(x)
        # you can see the tree after each insertion
        # print('after insert: ', x)
        # tree2.draw()

    # show the resulting tree
    tree2.draw()

    # both trees should be equal
    assert(tree1 == tree2)

    # Test remove
    print("after remove 80 (a leaf)")
    tree1.remove(80)
    tree1.draw()
    print()

    tree = BinarySearchTree()
    for x in [18, 11, 23, 5, 15, 20, 24, 9, 15, 22, 21, 6, 8, 7]:
        tree.insert(x)
    tree.draw()
    print('size:', tree.size())
    print('height:', tree.height())

    tree.remove(18)
    print("after remove 18 (root), replaced with its successor 20")
    tree.draw()

    tree.remove(7)
    print("after remove 7 (a leaf)")
    tree.draw()

    tree.remove(8)
    print("after remove 8 (a leaf)")
    tree.draw()

    tree.remove(5)
    print("after remove 5 (only a child), replaced with its child: 9")
    tree.draw()

    tree.remove(9)
    print("after remove 9 (only a child), replaced with its left child: 6")
    tree.draw()

    tree.remove(11)
    print("after remove 11 (two children), replaced with its successor: 15")
    tree.draw()

    tree.remove(20)
    print("after remove 20 (root), two children, replaced with its successor: 21")
    tree.draw()

    tree.remove(15)
    print("after remove 15 (only left child) -> 6")
    tree.draw()

    tree.remove(6)
    print("after remove 6 (a leaf)")
    tree.draw()

    tree.remove(8)
    print("after remove 8 (does not exist)")
    tree.draw()

    tree.remove(24)
    print("after remove 24 (a leaf)")
    tree.draw()
    print()

    for x in [5, 10, 15, 20]:
        tree.insert(x)
    print("after insert 5,10,15,20")
    tree.draw()

    tree.remove(23)
    print("after remove 23, only a left child -> 22")
    tree.draw()

    # remove a root, with only the left child
    tree.remove(22)
    print("after remove 22 (a leaf)")
    tree.draw()
    # remove a root, with only the right child
    print("after remove 5 (only a right child) ->10")
    tree.remove(5)
    tree.draw()

    print("after remove 21 (root with only a left child) -> 10")
    tree.remove(21)
    tree.draw()
