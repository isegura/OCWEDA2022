# -*- coding: utf-8 -*-

from bst import BinarySearchTree
from bintree import BinaryNode


class BST2(BinarySearchTree):
    def minimum(self) -> object:
        """returns the smallest key of the tree. What is its temporal complexity?"""
        # Complexity: O(log n)
        if self._root is None:
            print('tree is empty')
            return None

        node = self._root
        while node.left:
            node = node.left

        return node.elem

    def minimum_rec(self) -> object:
        """recursive function to return the smallest elem"""
        return self._minimum_rec(self._root)

    def _minimum_rec(self, node: BinaryNode) -> object:
        if node is None:
            return None  # base case
        elif node.left is None:
            return node.elem  # base case
        else:
            return self._minimum_rec(node.left)  # recursive case

    def maximum(self) -> object:
        """returns the greatest elem of the tree. What is its temporal complexity?"""
        # Complexity: O(log n)
        if self._root is None:
            print('tree is empty')
            return None

        node = self._root
        while node.right:
            node = node.right

        return node.elem

    def maximum_rec(self) -> object:
        """recursive function that returns the largest object"""
        return self._maximum_rec(self._root)

    def _maximum_rec(self, node: BinaryNode) -> object:
        if node is None:
            return None  # base case
        elif node.right is None:
            return node.elem  # base case
        else:
            return self._maximum_rec(node.right)  # base recursive

    def sum_elements(self) -> object:
        """ returns the sum of all its elements. What is its temporal complexity?"""
        # Complexity: O(n), where n is the size of the tree.
        # The function has to visit all the nodes of the tree.
        return self._sum_elements(self._root)

    def _sum_elements(self, node: BinaryNode) -> object:
        if node:
            return node.elem + self._sum_elements(node.left) + self._sum_elements(node.right)
        else:
            return 0

    def prints10(self) -> None:
        """prints the elements of those nodes whose grandparents' elements are multiply of 10
        What is its temporal complexity"""
        # Complexity: O(n), where n is the size of the tree.
        # The function has to visit all the nodes of the tree.
        self._prints10(self._root, None, None)

    def _prints10(self, node: BinaryNode, parent: BinaryNode, grand: BinaryNode) -> None:
        if node:
            self._prints10(node.left, node, parent)
            if grand and grand.elem % 10 == 0:
                print(node.elem, end=' ')
            self._prints10(node.right, node, parent)

    def _maximum_node(self, node: BinaryNode) -> BinaryNode:
        """returns the node with the maximum elem in the subtree node.
        This is the node that is furthest to the right
        """
        max_node = node
        while max_node.right is not None:
            max_node = max_node.right
        return max_node

    def _remove(self, node: BinaryNode, elem: object) -> BinaryNode:
        if node is None:
            return None

        if elem < node.elem:
            node.left = self._remove(node.left, elem)
        elif elem > node.elem:
            node.right = self._remove(node.right, elem)
        else:
            # elem == node.elem
            if node.left is None and node.right is None:
                # node is a leave
                node = None
            elif node.left is None:  # only has the right child
                return node.right
            elif node.right is None:  # only has the left child
                return node.left
            else:  # elem == node.elem
                predecessor = self._maximum_node(node.left)
                print('predecessor: ', predecessor.elem)
                node.elem = predecessor.elem
                node.left = self._remove(node.left, predecessor.elem)

        return node

    def fe_size(self, elem: object) -> int:
        """gives an elem, and returns the size balance factor of
        its node """
        node = self.search(elem)
        return self._fe_size(node)

    def _fe_size(self, node: BinaryNode) -> int:
        """returns the size balance factor of the input node"""
        if node is None:
            return 0
        else:
            return abs(self._size(node.left) - self._size(node.right))

    def is_size_balanced(self) -> bool:
        """return True if the tree is size balanced"""
        return self._is_size_balanced(self._root)

    def _is_size_balanced(self, node: BinaryNode) -> bool:
        """returns True if the node is size balanced;
        a node is balanced if its size factor is <=1 and
        its two children are size balanced"""
        if node:
            return self._fe_size(node) <= 1 and \
                   self._is_size_balanced(node.left) and \
                   self._is_size_balanced(node.right)
        else:
            return True

    def fe_height(self, elem: object) -> int:
        """gives an elem, and returns the height balance factor of
        its node """
        node = self.search(elem)
        return self._fe_height(node)

    def _fe_height(self, node: BinaryNode) -> int:
        """returns the height balance factor of the input node"""
        if node is None:
            return 0
        else:
            return abs(self._height(node.left) - self._height(node.right))

    def is_height_balanced(self) -> bool:
        """return True if the tree is height balance, that is,
        if its root is height balanced"""
        return self._is_height_balanced(self._root)

    def _is_height_balanced(self, node: BinaryNode) -> bool:
        """return True if the node is balanced, False e.o.c
        A node is balanced if its height balance <=1 and
        its two children are height balanced"""
        if node:
            return self._fe_height(node) <= 1 and \
                   self._is_height_balanced(node.left) and \
                   self._is_height_balanced(node.right)
        else:
            return True


if __name__ == "__main__":
    tree = BST2()
    for x in [50, 60, 30, 20, 24, 70, 66, 65, 10, 80, 21, 15, 35, 45, 22]:
        tree.insert(x)

    print('input tree:')
    tree.draw()
    print()
    print('Minimum elem of the tree:', tree.minimum())
    print('Maximum elem of the tree:', tree.maximum())
    print('sum of all its elements:', tree.sum_elements())
    print("elements whose grandparents' elements are multiply of 10")
    tree.prints10()
    print()

    tree.remove(50)
    # 50 should have been replaced by 45 as root
    print('after remove 50')
    tree.draw()

    tree.remove(70)
    print('after remove 70')
    # 70 should have been replaced by 66 as root
    tree.draw()

    tree.remove(20)
    # 20 should have been replaced by 15 as root
    print('after remove 20')
    tree.draw()

    tree.insert(55)
    tree.insert(36)
    tree.insert(50)
    tree.insert(32)
    tree.insert(56)
    print('after insert 55,36,50,32,56')
    tree.draw()
    print()
    for x in [45, 60, 30, 15, 35, 10, 24, 21, 66, 80, 63, 55, 36, 50, 32, 56]:
        print('size-balanced factor of  {} is {}'.format(x, tree.fe_size(x)))
        print('height-balanced factor of  {} is {}'.format(x, tree.fe_height(x)))
        print()
