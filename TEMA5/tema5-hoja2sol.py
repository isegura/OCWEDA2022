from bst import BinarySearchTree
from bintree import BinaryNode
from bintree import BinaryTree

from TEMA2.slistHT import SList
import sys


class MyBST(BinarySearchTree):

    def search_ancestors(self, value: int) -> (BinaryNode, BinaryNode, BinaryNode):
        """searches the node whose element is x and returns the node, its parent and its grand-parent.
        Its complexity is O(log n)"""

        # print("searching: ", value)
        grand_parent, parent = None, None
        node = self._root

        while node:
            # print(" visiting ", node.elem)
            if node.elem == value:  # we have found the node!!!
                # print("found: ", value)
                # print("search_ancestors:", grand_parent, parent, node)
                return grand_parent, parent, node

            grand_parent, parent = parent, node
            if value < node.elem:
                node = node.left
            else:  # x > node.elem:
                node = node.right

        # There is no node with element equals to value
        return None, None, None

    def check_cousins(self, x: int, y: int) -> bool:
        """returns True if x and y are cousins, and False eoc. Problem Exam May 2020
            Complexity: O(log n)"""

        grand_parent_x, parent_x, node_x = self.search_ancestors(x)
        grand_parent_y, parent_y, node_y = self.search_ancestors(y)

        return parent_x != parent_y and grand_parent_x == grand_parent_y

    def lwc(self, a: int, b: int) -> BinaryNode:
        """returns the lowest common ancestor of a and b, June 2020.
        Complexity O(log n)"""

        # swap if a > b, to assure a < b
        if a > b:
            a, b = b, a

        _, parent_a, node_a = self.search_ancestors(a)
        _, parent_b, node_b = self.search_ancestors(b)

        if node_a is None or node_b is None:
            if node_a is None:
                print(a, ' does not exist into the tree')
            if node_b is None:
                print(b, ' does not exist into the tree')
            return None

        if a == b:  # if they are the same value, then we return its parent
            # returns the parent's element only when this parent is not None, eoc it returns None
            return parent_b.elem if parent_b else None

        # we always suppose that a < b
        return self._lwc(self._root, a, b, parent_a, parent_b)

    def _lwc(self, node: BinaryNode, a: int, b: int, parent_a: BinaryNode, parent_b: BinaryNode) -> BinaryNode:
        """returns the lowest common ancestor of a and b (a<b), searching from node.
        Complexity O(log n)"""
        if node is None:
            return None

        # print(node, a, b, parent_a, parent_b)
        # Base case 1: node.elem is a
        if a == node.elem:
            # we have to return the parent of a; we return its elements if parent_a is not None, eoc it returns None
            return parent_a.elem if parent_a else None
        # Base case 2: node.elem is b
        if b == node.elem:
            # we have to return the parent of b; we return its elements if parent_b is not None, eoc it returns None
            return parent_b.elem if parent_b else None

        # Base case 3: a< node.elem < b
        if a < node.elem < b:
            return node.elem

        # Recursive cases
        # if a, b < node.elem we have to continue the searching on its node.left
        if a < node.elem and b < node.elem:
            return self._lwc(node.left, a, b, parent_a, parent_b)

        # if a, b > node.elem we have to continue the searching on its node.right
        if a > node.elem and b > node.elem:
            return self._lwc(node.right, a, b, parent_a, parent_b)

    def is_zig_zag(self) -> bool:
        """returns True if the tree is a ziz-zag-shaped tree, False eoc.
        Worst case: The tree is zig-zag, we have to visit all nodes, O(n)
        Best case: the tree is empty or the root has two children"""

        if self._root is None or self.size() <= 2:
            return False

        return self._is_zig_zag(self._root, None)

    def _num_children(self, node):
        """returns the number of children of node.
        O(1)"""
        count = 0
        if node:
            if node.left:
                count += 1
            if node.right:
                count += 1
        return count

    def _is_zig_zag(self, node: BinaryNode, origin: str) -> bool:
        """returns True if the node has a zig-zag-shape, False eoc"""
        # print(node, origin)
        if self._num_children(node) == 0:
            return True

        if self._num_children(node) == 2:
            return False

        # node only has left or right
        if node.left:
            return self._is_zig_zag(node.left, "left") if origin != "left" else False

        # then, node has a right child
        return self._is_zig_zag(node.right, "right") if origin != "right" else False

    def is_same_shape(self, other_tree: "MyBST") -> bool:
        """returns True if both trees have the same shape, False e.o.c.
        Worst case: both trees have the same shape, we have to visit all nodes, O(n)
        Best case: other_tree is None, O(1) """
        if other_tree is None:
            return False

        return self._is_same_shape(self._root, other_tree._root)

    def _is_same_shape(self, node_1: BinaryNode, node_2: BinaryNode) -> bool:
        """returns True if both nodes have the same shape, False e.o.c"""
        if node_1 is None and node_2 is None:
            return True

        # if node_1 is not None and node_2 is not None:
        if node_1 and node_2:
            # we have to compare left children and right children, separately
            return self._is_same_shape(node_1.left, node_2.left) and self._is_same_shape(node_1.right, node_2.right)

        # any other case will be always False
        return False

    def is_left_odd_right_even(self) -> bool:
        """checks that all nodes (non-leaves) have a left child with an odd value and a right child with an even value.
        Wort case, the tree is left-odd-right-even, you have to visit all nodes, O(n)
        Best case, the tree is empty or has just a child, O(1)"""
        if self._num_children(self._root) <= 1:
            return False

        return self._is_left_odd_right_even(self._root)

    def _is_left_odd_right_even(self, node: BinaryNode) -> bool:
        """checks that all nodes (non-leaves) have a left child with an odd value and a right child with an even value"""
        if self._num_children(node) == 0:  # If the node is a leaf, we return True
            return True
        if self._num_children(node) == 1:  # If the node is a leaf, we return False
            return False
        # node has two children

        # the left elem is even or the right elem is odd
        if node.left.elem % 2 == 0 or node.right.elem % 2 != 0:
            return False
        # eoc, we have to check node.left and node.right
        return self._is_left_odd_right_even(node.left) and self._is_left_odd_right_even(node.right)

    def closest(self, value: int) -> int:
        """returns the closest element to value.
         Worst Case: value exists and it is a leaf in the largest branch. O(log n)
         Best Case: root is None or root.elem is value, O(1)
         """
        return self._closest(self._root, value)

    def _closest(self, node: BinaryNode, value: int) -> int:
        """returns the closest element to value.
         value could not exist into the tree.
         """

        if node is None:  # when the root is none
            return None

        if node.elem == value:  # base case: node.elem is value
            return value

        if value < node.elem:  # we have to search in the left child
            if node.left:
                closest_child = self._closest(node.left, value)
            else:  # as there is no left child, the closest value will be node.elem
                return node.elem
        else:
            if node.right:
                closest_child = self._closest(node.right, value)
            else:
                return node.elem

        # we have to compare both distances
        if abs(value - node.elem) < abs(value - closest_child):
            return node.elem
        elif abs(value - node.elem) > abs(value - closest_child):
            return closest_child
        else:
            # if the distance is the same, we return the greatest element.
            return max(closest_child, node.elem)

    def is_bst(self) -> bool:
        """checks if the tree is bst.
        Worst case: we have to visit all nodes, O(n)
        Best case: tree is empty"""
        return self._is_bst(self._root, -sys.maxsize, sys.maxsize)

    def _is_bst(self, node: BinaryNode, min_value: int, max_value: int) -> bool:
        if node is None:
            return True

        if node.elem < min_value or node.elem > max_value:
            return False

        return self._is_bst(node.left, min_value, node.elem - 1) and self._is_bst(node.right, node.elem + 1, max_value)

    def update_adding_left_child(self):
        """change the value in each node to sum of all the values in the nodes in the left subtree including its own.
        Complexity: O(n) """
        self._update_adding_left_child(self._root)

    def _update_adding_left_child(self, node):
        # Base cases
        if node is None:
            return 0

        # print("changing: ", node.elem)

        if node.left is None and node.right is None:
            return node.elem

        # Update left and right subtrees
        left_sum = self._update_adding_left_child(node.left)
        right_sum = self._update_adding_left_child(node.right)

        # Add right_sum to current node
        node.elem += left_sum

        # Return sum of values under root
        return node.elem + right_sum

    def get_non_leaves(self) -> list:
        """returns a list with the elements of the nodes that are not leaves.
        Complexity O(n).
        The list has to be sorted in ascending order."""
        result = []
        self._get_non_leaves(self._root, result)
        return result

    def _get_non_leaves(self, node: BinaryNode, lst_nodes: list) -> None:
        """ Complexity: O(n) """
        if node:
            self._get_non_leaves(node.right, lst_nodes)
            if node.left or node.right:
                lst_nodes.append(node.elem)
            self._get_non_leaves(node.left, lst_nodes)


def array2bst(lst_values: list) -> BinarySearchTree:
    """ gets a sorted list and creates a balanced bst"""
    tree = BinarySearchTree()
    if lst_values and len(lst_values) >= 1:
        # lst_values.sort()
        _array2bst(lst_values, 0, len(lst_values) - 1, tree)
    return tree


def _array2bst(lst_values: list, start: int, end: int, tree: BinarySearchTree) -> None:
    if start <= end:
        middle = (start + end) // 2
        tree.insert(lst_values[middle])
        _array2bst(lst_values, start, middle - 1, tree)
        _array2bst(lst_values, middle + 1, end, tree)


def mirror(obj_tree: BinaryTree) -> None:
    """ Complexity: O(n). We have to visit all nodes"""
    _mirror(obj_tree._root)


def _mirror(node: BinaryNode) -> None:
    if node:
        # we transform the left child
        _mirror(node.left)
        # we transform the right child
        _mirror(node.right)
        # swap the children
        node.left, node.right = node.right, node.left


if __name__ == "__main__":
    # tree = MyBST()
    # values = [25, 20, 36, 10, 22, 30, 40, 5, 12, 28, 38, 48]
    # tree = MyBST()
    # for x in values:
    #    tree.insert(x)
    # tree.draw()

    # # test check_cousins
    # print('5 and 15 are cousins?, False:', tree.check_cousins(5, 15))  # False, 15 does not exist
    # print('5 and 22 are cousins?, False:', tree.check_cousins(5, 22))  # False, have different levels
    # print('5 and 22 are cousins?, False:', tree.check_cousins(5, 22))  # False, have different levels
    # print('36 and 48 are cousins?, False:', tree.check_cousins(36, 48))  # False, have different levels
    # print('5 and 12 are cousins?:, False', tree.check_cousins(5, 12))  # False, are siblings
    # print('20 and 36 are cousins?:, False', tree.check_cousins(20, 36))  # False, are siblings
    # print('10 and 22 are cousins?:, False', tree.check_cousins(10, 22))  # False, are siblings
    # print('5 and 28 are cousins?:, False', tree.check_cousins(5, 28))  # False, same level, their parents are not siblings
    # print('12 and 28 are cousins?:, False', tree.check_cousins(12, 28))  # False, same level, their parents are not siblings
    # print('10 and 30 are cousins?:, True', tree.check_cousins(10, 30))  # True, are cousins
    # print('10 and 40 are cousins?:, True', tree.check_cousins(10, 30))  # True, are cousins
    # print('22 and 30 are cousins?:, True', tree.check_cousins(22, 30))  # True, are cousins
    # print('22 and 40 are cousins?:, True', tree.check_cousins(22, 40))  # True, are cousins
    # print('28 and 38 are cousins?:, True', tree.check_cousins(28, 38))  # True, are cousins
    # print('28 and 48 are cousins?:, True', tree.check_cousins(28, 48))  # True, are cousins

    # test lwc lowest common ancestor
    # a, b = 48, 38
    # print("tree.lwc({}, {})={}".format(a, b, tree.lwc(a, b)), 40)
    # a, b = 48, 28
    # print("tree.lwc({}, {})={}".format(a, b, tree.lwc(a, b)), 36)
    # a, b = 48, 30
    # print("tree.lwc({}, {})={}".format(a, b, tree.lwc(a, b)), 36)
    # a, b = 40, 30
    # print("tree.lwc({}, {})={}".format(a, b, tree.lwc(a, b)), 36)
    # a, b = 28, 22
    # print("tree.lwc({}, {})={}".format(a, b, tree.lwc(a, b)), 50)
    # a, b = 22, 5
    # print("tree.lwc({}, {})={}".format(a, b, tree.lwc(a, b)), 20)
    # a, b = 25, 5
    # print("tree.lwc({}, {})={}".format(a, b, tree.lwc(a, b)), None)
    # a, b = 25, 48
    # print("tree.lwc({}, {})={}".format(a, b, tree.lwc(a, b)), None)
    # a, b = 10, 48
    # print("tree.lwc({}, {})={}".format(a, b, tree.lwc(a, b)), 25)
    # a, b = 25, 38
    # print("tree.lwc({}, {})={}".format(a, b, tree.lwc(a, b)), None)
    # a, b = 25, 25
    # print("tree.lwc({}, {})={}".format(a, b, tree.lwc(a, b)), None)
    # a, b = 36, 38
    # print("tree.lwc({}, {})={}".format(a, b, tree.lwc(a, b)), 25)
    # a, b = 30, 36
    # print("tree.lwc({}, {})={}".format(a, b, tree.lwc(a, b)), 25)
    # a, b = 20, 22
    # print("tree.lwc({}, {})={}".format(a, b, tree.lwc(a, b)), 25)
    # a, b = 20, 20
    # print("tree.lwc({}, {})={}".format(a, b, tree.lwc(a, b)), 25)
    # a, b = 5, 5
    # print("tree.lwc({}, {})={}".format(a, b, tree.lwc(a, b)), 10)
    # a, b = 5, 28
    # print("tree.lwc({}, {})={}".format(a, b, tree.lwc(a, b)), 25)
    # a, b = 5, 22
    # print("tree.lwc({}, {})={}".format(a, b, tree.lwc(a, b)), 20)
    # a, b = 5, 12
    # print("tree.lwc({}, {})={}".format(a, b, tree.lwc(a, b)), 10)
    # a, b = 4, 12
    # print("tree.lwc({}, {})={}".format(a, b, tree.lwc(a, b)), None)
    # a, b = 5, 33
    # print("tree.lwc({}, {})={}".format(a, b, tree.lwc(a, b)), None)
    # a, b = 4, 33
    # print("tree.lwc({}, {})={}".format(a, b, tree.lwc(a, b)), None)

    # test closest
    # v = 48  # 25, 12
    # print("closest({})={}".format(v, tree.closest(v)), v)
    #
    # v = 13
    # print("closest({})={}".format(v, tree.closest(v)), 12)
    #
    # v = 29
    # print("closest({})={}".format(v, tree.closest(v)), 30)
    #
    # v = 45
    # print("closest({})={}".format(v, tree.closest(v)), 48)
    #
    # v = 21
    # print("closest({})={}".format(v, tree.closest(v)), 22)
    #
    # v = 33
    # print("closest({})={}".format(v, tree.closest(v)), 36)

    # values = [50]
    # tree = MyBST()
    # for x in values:
    #     tree.insert(x)
    # tree.draw()
    # print('is_zig_zag:', tree.is_zig_zag())
    # print()
    #
    # tree.insert(40)
    # tree.draw()
    # print('is_zig_zag:', tree.is_zig_zag())
    # print()
    #
    # tree.insert(60)
    # tree.draw()
    # print('is_zig_zag:', tree.is_zig_zag())
    # print()
    #
    # tree.remove(60)
    # tree.insert(45)
    # tree.draw()
    # print('is_zig_zag:', tree.is_zig_zag())
    # print()
    #
    # tree.insert(42)
    # tree.draw()
    # print('is_zig_zag:', tree.is_zig_zag())
    # print()
    #
    # tree.insert(69)
    # tree.draw()
    # print('is_zig_zag:', tree.is_zig_zag())
    # print()
    #
    # values = [50,60]
    # tree = MyBST()
    # for x in values:
    #     tree.insert(x)
    # tree.draw()
    #
    # print('is_zig_zag:', tree.is_zig_zag())
    # print()
    #
    # tree.insert(69)
    # tree.draw()
    # print('is_zig_zag:', tree.is_zig_zag())
    # print()
    #
    # tree.remove(69)
    # tree.insert(55)
    # tree.draw()
    # print('is_zig_zag:', tree.is_zig_zag())
    # print()
    #
    # tree.insert(58)
    # tree.draw()
    # print('is_zig_zag:', tree.is_zig_zag())
    # print()
    #
    # tree.insert(15)
    # tree.draw()
    # print('is_zig_zag:', tree.is_zig_zag())
    # print()

    # test: is_same_shape()

    # tree1 = MyBST()
    # print(tree1.is_same_shape(None))
    # tree2 = MyBST()
    # tree1.draw()
    # tree2.draw()
    # print(tree1.is_same_shape(tree2))
    # print()
    #
    # tree1.insert(50)
    # tree1.draw()
    # tree2.draw()
    # print(tree1.is_same_shape(tree2))
    # print()
    #
    # tree2.insert(70)
    # tree1.draw()
    # tree2.draw()
    # print(tree1.is_same_shape(tree2))
    # print()
    #
    # tree1.insert(40)
    # tree1.draw()
    # tree2.draw()
    # print(tree1.is_same_shape(tree2))
    # print()
    #
    # tree2.insert(30)
    # tree1.draw()
    # tree2.draw()
    # print(tree1.is_same_shape(tree2))
    # print()
    #
    # tree1.insert(80)
    # tree1.draw()
    # tree2.draw()
    # print(tree1.is_same_shape(tree2))
    # print()
    #
    # tree2.insert(90)
    # tree1.draw()
    # tree2.draw()
    # print(tree1.is_same_shape(tree2))
    # print()
    #
    # tree1.insert(90)
    # tree1.draw()
    # tree2.draw()
    # print(tree1.is_same_shape(tree2))
    # print()
    #
    # tree2.insert(95)
    # tree1.draw()
    # tree2.draw()
    # print(tree1.is_same_shape(tree2))
    # print()
    #
    # tree1.insert(30)
    # tree1.draw()
    # tree2.draw()
    # print(tree1.is_same_shape(tree2))
    # print()
    #
    # tree2.insert(25)
    # tree1.draw()
    # tree2.draw()
    # print(tree1.is_same_shape(tree2))
    # print()

    # test is_left_odd_right_even

    # tree = MyBST()
    # tree.insert(50)
    # tree.draw()
    # print("is_left_odd_right_even:", tree.is_left_odd_right_even())
    # print()
    #
    # tree.insert(60)
    # tree.draw()
    # print("is_left_odd_right_even:", tree.is_left_odd_right_even())
    # print()
    #
    # tree.insert(41)
    # tree.draw()
    # print("is_left_odd_right_even:", tree.is_left_odd_right_even())
    # print()
    #
    # tree.insert(66)
    # tree.draw()
    # print("is_left_odd_right_even:", tree.is_left_odd_right_even())
    # print()
    #
    # tree.insert(54)
    # tree.draw()
    # print("is_left_odd_right_even:", tree.is_left_odd_right_even())
    # print()
    #
    # tree.remove(54)
    # tree.insert(53)
    # tree.draw()
    # print("is_left_odd_right_even:", tree.is_left_odd_right_even())
    # print()
    #
    # tree.insert(39)
    # tree.draw()
    # print("is_left_odd_right_even:", tree.is_left_odd_right_even())
    # print()
    #
    # tree.insert(45)
    # tree.draw()
    # print("is_left_odd_right_even:", tree.is_left_odd_right_even())
    # print()
    #
    # tree.remove(45)
    # tree.insert(46)
    # tree.draw()
    # print("is_left_odd_right_even:", tree.is_left_odd_right_even())
    # print()

    # tree3 = MyBST()
    # values = [10, 5, 20, 15, 30, 45, 2]
    # for x in values:
    #     tree3.insert(x)
    # tree3.draw()
    # print("is_bst:", tree3.is_bst())
    # print("get_non_leaves: ", tree3.get_non_leaves())
    # print()
    #
    # tree3.update_adding_left_child()
    # tree3.draw()
    #
    # print("is_bst:", tree3.is_bst())
    #
    # print("get_non_leaves: ", tree3.get_non_leaves())

    # Test array2bst
    l_values = [1, 2, 3, 4, 5, 6, 7]
    tree = array2bst(l_values)
    tree.draw()

    # Test mirror
    print('mirror:')
    mirror(tree)
    tree.draw()
