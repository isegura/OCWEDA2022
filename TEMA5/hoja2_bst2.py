from bst import BinarySearchTree
from bintree import BinaryNode
import bintree as bt
import bst

def check_cousins(tree: "BST2", x: int, y: int) -> bool:
    """returns True if x and y are cousins, and False eoc. Problem Exam May 2020
        Complexity: O(log n)"""

    node_x, parent_x, grand_parent_x = tree.search_ancestors(x)
    node_y, parent_y, grand_parent_y = tree.search_ancestors(y)

    return parent_x != parent_y and grand_parent_x == grand_parent_y


def lwc(tree: BinarySearchTree, a: int, b: int) -> int:
    """returns the element of the node that is the lowest common ancestor
    for a en b"""

    # First, the solution must check all possible inputs
    if not isinstance(a, int):
        print(a, ' must be an integer')
        return None
    if not isinstance(b, int):
        print(a, ' must be an integer')
        return None

    if a == b:
        print(a, b, " must be different")
        return None
    if tree is None:
        print('tree is None')
        return None

    # we search a and b in the tree, and also get their parents.
    node_a, parent_a, _ = tree.search_ancestors(a)
    if node_a is None:
        print(a, ' does not exist in the tree')
        return None

    node_b, parent_b, _ = tree.search_ancestors(tree, b)
    if node_b is None:
        print(b, ' does not exist in the tree')
        return None

    # it could be that a is a descendant of b, or b is a descendant of b
    if tree._search(node_a, b) is not None:
        # b is a descendant of a
        if parent_a:
            return parent_a.elem
        return None
    if tree._search(node_b, a) is not None:
        # a is a descendant of b
        if parent_b:
            return parent_b.elem
        return None

    return _lwc(tree.root, a, b)


def _lwc(node: BinaryNode, a: int, b: int) -> int:
    if node is None:
        return None
    if a < node.elem and b < node.elem:
        # if a and b are smaller than node.elem, I only have to search on its left child
        return _lwc(node.left, a, b)
    if a > node.elem and b > node.elem:
        # if a and b are greater than node.elem, I only have to search on its right child
        return _lwc(node.right, a, b)

    # Case: (a<=node.elem<=b) or (b<=node.elem<=a):
    return node


class BST2(BinarySearchTree):
    def __maximum_node(self, subtree: BinaryNode) -> BinaryNode:
        """gets a node (subtree) and returns the node with the biggest
        element in the subtree. O(log n)"""
        result = None
        if subtree is not None:
            biggest = subtree
            while biggest.right:
                biggest = biggest.right
            result = biggest
        return result

    def _remove(self, node: BinaryNode, elem: object) -> BinaryNode:
        """It recursively searches the node. When the node is
        found, the node has to be removed"""
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
            elif node.right is None:  # Case 2: only has a left child
                node = node.left
            else:  # Case 3: node.left!=None and node.right!=None
                # we search the biggest node from its left child
                predecessor = self.__maximum_node(node.left)
                # we replace elem with the elem of the successor
                node.elem = predecessor.elem
                # now, we have to remove successor from the right child
                node.left = self._remove(node.left, predecessor.elem)

        return node

    def _fe_size(self, node: BinaryNode) -> int:
        """returns the size balance factor of the input node"""
        if node is None:
            return 0
        return abs(self._size(node.left) - self._size(node.right))

    def is_size_balanced(self) -> bool:
        """return True if the input_tree is size balanced"""
        return self.__is_size_balanced(self.root)

    def __is_size_balanced(self, node: BinaryNode) -> bool:
        """returns True if the node is size balanced;
        a node is balanced if its size factor is <=1 and
        its two children are size balanced"""
        if node:
            return self._fe_size(node) <= 1 and self.__is_size_balanced(node.left) and \
                   self.__is_size_balanced(node.right)

        return True

    def _fe_height(self, node: BinaryNode) -> int:
        """returns the height balance factor of the input node"""
        if node is None:
            return 0
        return abs(self._height(node.left) - self._height(node.right))

    def is_height_balanced(self) -> bool:
        """return True if the input_tree is height balance, that is,
        if its root is height balanced"""
        return self.__is_height_balanced(self.root)

    def __is_height_balanced(self, node: BinaryNode) -> bool:
        """return True if the node is balanced, False e.o.c
        A node is balanced if its height balance <=1 and
        its two children are height balanced"""
        if node:
            return self._fe_height(node) <= 1 and \
                   self._is_height_balanced(node.left) and \
                   self._is_height_balanced(node.right)

        return True

    def get_non_leaves(self) -> list:
        """returns a list with the elements of the nodes that are not leaves.
        Complexity O(n).
        The list has to be sorted in ascending order."""
        result = []
        self.__get_non_leaves(self.root, result)
        return result

    def __get_non_leaves(self, node: BinaryNode, lst_nodes: list) -> None:
        """ Complexity: O(n) """
        if node:
            self.__get_non_leaves(node.right, lst_nodes)
            if node.left or node.right:
                lst_nodes.append(node.elem)
            self.__get_non_leaves(node.left, lst_nodes)

    def is_zig_zag(self) -> bool:
        """returns True if the input_tree is a ziz-zag-shaped input_tree, False eoc.
        Worst case: The input_tree is zig-zag, we have to visit all nodes, O(n)
        Best case: the input_tree is empty or the root has two children"""

        if self.root is None or self.size() <= 2:
            return False

        return self.__is_zig_zag(self.root, None)

    def __num_children(self, node: BinaryNode) -> int:
        """returns the number of children of node.
        O(1)"""
        count = 0
        if node:
            if node.left:
                count += 1
            if node.right:
                count += 1
        return count

    def __is_zig_zag(self, node: BinaryNode, origin: str) -> bool:
        """returns True if the node has a zig-zag-shape, False eoc"""
        # print(node, origin)
        if self.__num_children(node) == 0:
            return True

        if self.__num_children(node) == 2:
            return False

        # node only has left or right
        if node.left:
            return self.__is_zig_zag(node.left, "left") if origin != "left" else False

        # then, node has a right child
        return self.__is_zig_zag(node.right, "right") if origin != "right" else False

    def is_left_odd_right_even(self) -> bool:
        """checks that all nodes (non-leaves) have a left child with an odd value and a right child with an even value.
        Wort case, the input_tree is left-odd-right-even, you have to visit all nodes, O(n)
        Best case, the input_tree is empty or has just a child, O(1)"""
        if self.__num_children(self.root) <= 1:
            return False

        return self.__is_left_odd_right_even(self.root)

    def __is_left_odd_right_even(self, node: BinaryNode) -> bool:
        """checks that all nodes (non-leaves) have a left child with an odd value and a right child with an even value"""
        if self.__num_children(node) == 0:  # If the node is a leaf, we return True
            return True
        if self.__num_children(node) == 1:  # If the node is a leaf, we return False
            return False
        # node has two children
        # the left elem is even or the right elem is odd
        if node.left.elem % 2 == 0 or node.right.elem % 2 != 0:
            return False
        # eoc, we have to check node.left and node.right
        return self.__is_left_odd_right_even(node.left) and self.__is_left_odd_right_even(node.right)

    def closest(self, value: int) -> int:
        """returns the closest element to value.
        Worst Case: value exists, and it is a leaf in the largest branch. O(log n)
        Best Case: root is None or root. elem is value, O(1)
        """
        return self.__closest(self.root, value)

    def __closest(self, node: BinaryNode, value: int) -> int:
        """returns the closest element to value.
        value could not exist into the input_tree."""

        if node is None:  # when the root is none
            return None

        if node.elem == value:  # base case: node.elem is value
            return value

        if value < node.elem:  # we have to search in the left child
            if node.left:
                closest_child = self.__closest(node.left, value)
            else:  # as there is no left child, the closest value will be node.elem
                return node.elem
        else:  # value > node.elem
            if node.right:
                closest_child = self.__closest(node.right, value)
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

    def search_ancestors(self, value: int) -> (BinaryNode, BinaryNode, BinaryNode):
        """returns (node, parent, grand) of value"""
        return self.__search_ancestors(self.root, None, None, value)

    def __search_ancestors(self, node: BinaryNode,
                           parent_node: BinaryNode,
                           grand_node: BinaryNode, value: int) -> (BinaryNode, BinaryNode, BinaryNode):
        if node is None:
            return None, None, None
        if node.elem == value:
            return node, parent_node, grand_node
        if value < node.elem:
            return self.__search_ancestors(node.left, node, parent_node, value)
        else:
            return self.__search_ancestors(node.right, node, parent_node, value)


if __name__ == "__main__":
    input_tree = BST2()
    values = [25, 20, 36, 10, 22, 30, 40, 5, 12, 28, 38, 48]
    for x in values:
        input_tree.insert(x)
    input_tree.draw()
    print("get_non_leaves: ", input_tree.get_non_leaves())
    print("is_zig_zag: ", input_tree.is_zig_zag())

    """
    print("Smallest element: ", get_smallest_ite(input_tree))
    assert get_smallest_ite(input_tree) == min(values)

    print("Smallest element: ", get_smallest_rec(input_tree))
    print("Smallest element: ", get_smallest_rec(None))
    print("Smallest element: ", get_smallest_rec(BinarySearchTree()))
    assert get_smallest_rec(input_tree) == min(values)

    print("Greatest element: ", get_greatest_ite(None))
    print("Greatest element: ", get_greatest_ite(BinarySearchTree()))
    print("Greatest element: ", get_greatest_ite(input_tree))
    assert get_greatest_ite(input_tree) == max(values)

    print("sum of all elements: ", sum_elements(None))
    print("sum of all elements: ", sum_elements(BinarySearchTree()))
    print("sum of all elements: ", sum_elements(input_tree))
    assert sum_elements(input_tree) == sum(values)

    print("sum of all elements: ", sum_elements_rec(None))
    print("sum of all elements: ", sum_elements_rec(BinarySearchTree()))
    print("sum of all elements: ", sum_elements_rec(input_tree))
    assert sum_elements_rec(input_tree) == sum(values)
    """

    """
    for x in values:
        node = input_tree.search(x)
        if node is not None:
            small_n = smallest_node(node)
            print(small_n.elem, " is the smallest node in ", node.elem )
    print()
    """

    """
    input_tree = BSTRemove2()
    # input_tree = BinarySearchTree()
    for x in [5, 10, 15, 20, 23, 22, 24, 3, 7]:
        input_tree.insert(x)
    input_tree.draw()
    print("is_size_balanced:", is_size_balanced(input_tree))
    print("is_height_balanced:", is_height_balanced(input_tree))

    input_tree.remove(24)
    print("after remove 24, a leaf")
    input_tree.draw()

    print("is_size_balanced:", is_size_balanced(input_tree))
    print("is_height_balanced:", is_height_balanced(input_tree))

    input_tree.remove(23)
    print("after remove 23 (only has a left child)")
    input_tree.draw()

    print("is_size_balanced:", is_size_balanced(input_tree))
    print("is_height_balanced:", is_height_balanced(input_tree))

    input_tree.remove(20)
    print("after remove 20 (only has a right child)")
    input_tree.draw()

    print("is_size_balanced:", is_size_balanced(input_tree))
    print("is_height_balanced:", is_height_balanced(input_tree))

    input_tree.remove(22)
    print("after remove 22 (a leaf)")
    input_tree.draw()

    print("is_size_balanced:", is_size_balanced(input_tree))
    print("is_height_balanced:", is_height_balanced(input_tree))

    input_tree.remove(10)
    print("after remove 10 (two children)")
    input_tree.draw()

    print("is_size_balanced:", is_size_balanced(input_tree))
    print("is_height_balanced:", is_height_balanced(input_tree))

    input_tree.remove(5)
    print("after remove 5 (root with two children)")
    input_tree.draw()

    print("is_size_balanced:", is_size_balanced(input_tree))
    print("is_height_balanced:", is_height_balanced(input_tree))

    for x in [11, 10, 30]:
        input_tree.insert(x)
    print('after insert [11, 10, 30]')
    input_tree.draw()

    print("is_size_balanced:", is_size_balanced(input_tree))
    print("is_height_balanced:", is_height_balanced(input_tree))

    input_tree.remove(3)
    print("after remove 3 (root only right child)")
    input_tree.draw()

    print("is_size_balanced:", is_size_balanced(input_tree))
    print("is_height_balanced:", is_height_balanced(input_tree))

    input_tree.remove(7)
    print("after remove 7 (root only right child)")
    input_tree.draw()

    print("is_size_balanced:", is_size_balanced(input_tree))
    print("is_height_balanced:", is_height_balanced(input_tree))

    input_tree.remove(15)
    print("after remove 15 root, replace with 11")
    input_tree.draw()
    print("is_size_balanced:", is_size_balanced(input_tree))
    print("is_height_balanced:", is_height_balanced(input_tree))

    data = [50, 20, 60, 15, 55, 70, 10, 18, 75, 8, 93]
    data.sort()
    print(data)
    # data = [5, 10, 15, 20, 25, 30]
    input_tree = array2bst(data)
    input_tree.draw()
    print("is_size_balanced:", is_size_balanced(input_tree))
    print("is_height_balanced:", is_height_balanced(input_tree))
"""
    """
    data1 = [20, 10, 30, 8]
    tree1 = BinarySearchTree()
    for x in data1:
        tree1.insert(x)

    data2 = [80, 60, 90, 5]
    tree2 = BinarySearchTree()
    for x in data2:
        tree2.insert(x)
    tree1.draw()
    tree2.draw()
    print("same_shape:", same_shape(tree1, tree2))
    print("same_shape:",same_shape(tree1, BinarySearchTree()))
    print("same_shape:",same_shape(BinarySearchTree(), tree1))
    print("same_shape:",same_shape(None, tree1))
    tree1.draw()
    print("get_non_leaves: ", get_non_leaves(tree1))
    """
    """
    input_tree = BinarySearchTree()
    for x in [10, 20, 15, 18, 17, 19]:
        input_tree.insert(x)
        input_tree.draw()
        print("is_zig_zag:", is_zig_zag(input_tree))

    for v in [18, 16, 11, 12, 13, 22]:
        print("closest({})={}".format(v, closest(input_tree, v)))
        
    """

    """
    input_tree = BinarySearchTree()
    for x in [15, 3, 1, 5, 30, 20, 40]:
        input_tree.insert(x)
        input_tree.draw()

    update_adding_left_child(input_tree)
    input_tree.draw()
    """
    """
    input_tree = BinarySearchTree()
    for number in [15, 3, 1, 5, 30, 20, 40, 6]:
        input_tree.insert(number)
    input_tree.draw()
    """
    """    
    i, j = 15, 3
    print("lwc({},{})={}".format(i, j, lwc(input_tree, i, j)))
    i, j = 3, 30
    print("lwc({},{})={}".format(i, j, lwc(input_tree, i, j)))
    i, j = 1, 20
    print("lwc({},{})={}".format(i, j, lwc(input_tree, i, j)))
    i, j = 1, 30
    print("lwc({},{})={}".format(i, j, lwc(input_tree, i, j)))
    i, j = 20, 3
    print("lwc({},{})={}".format(i, j, lwc(input_tree, i, j)))
    i, j = 30, 40
    print("lwc({},{})={}".format(i, j, lwc(input_tree, i, j)))
    i, j = 1, 3
    print("lwc({},{})={}".format(i, j, lwc(input_tree, i, j)))
    i, j = 5, 6
    print("lwc({},{})={}".format(i, j, lwc(input_tree, i, j)))
    i, j = 3, 6
    print("lwc({},{})={}".format(i, j, lwc(input_tree, i, j)))
    """
    """
    i, j = 15, 3
    print("check_cousins({},{})={}".format(i, j, check_cousins(input_tree, i, j)))
    i, j = 3, 30
    print("check_cousins({},{})={}".format(i, j, check_cousins(input_tree, i, j)))
    i, j = 1, 20
    print("check_cousins({},{})={}".format(i, j, check_cousins(input_tree, i, j)))
    i, j = 5, 20
    print("check_cousins({},{})={}".format(i, j, check_cousins(input_tree, i, j)))
"""
