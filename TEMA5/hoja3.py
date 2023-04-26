from bst import BinarySearchTree
from bintree import BinaryNode

class BST2(BinarySearchTree):
    def __maximum_node(self, subtree: BinaryNode) -> BinaryNode:
        """gets a node (subtree) and returns the node with the biggest
        element in the subtree. O(log n)"""
        maximum = None
        if subtree is not None:
            maximum = subtree
            while maximum.right:
                maximum = maximum.right
        return maximum

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
                   self.__is_height_balanced(node.left) and \
                   self.__is_height_balanced(node.right)

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

    def same_shape(self, other_tree: BinarySearchTree) -> bool:
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

    def is_zig_zag(self) -> bool:
        """returns True if the input_tree is a ziz-zag-shaped input_tree, False eoc.
        Worst case: The input_tree is zig-zag, we have to visit all nodes, O(n)
        Best case: the input_tree is empty or the root has two children"""

        if self.root is None or self.size() <= 2:
            return False

        # return self.__is_zig_zag(self.root, None)
        return self.__is_zig_zag2(self.root, None)

    def __is_zig_zag(self, node: BinaryNode, origin: str) -> bool:
        """returns True if the node has a zig-zag-shape, False eoc"""
        # print(node, origin)
        if node.left is None and node.right is None:
            return True

        if node.left and node.right:
            return False

        # node only has left or right
        if node.left:
            return self.__is_zig_zag(node.left, "left") if origin != "left" else False

        # then, node has a right child
        return self.__is_zig_zag2(node.right, "right") if origin != "right" else False

    def __is_zig_zag2(self, node: BinaryNode, parent: BinaryNode) -> bool:
        """returns True if the node has a zig-zag-shape, False eoc"""
        # print(node, origin)
        if node.left is None and node.right is None:
            return True

        if node.left and node.right:
            return False

        # node only has left or right
        if node.left:
            if parent and node == parent.left:
                return False
            return self.__is_zig_zag2(node.left, node)

        # then, node has a right child
        if parent and node == parent.right:
            return False
        return self.__is_zig_zag2(node.right, node)

    def is_left_odd_right_even(self) -> bool:
        """checks that all nodes (non-leaves) have a left child with an odd value and a right child with an even value.
        Wort case, the input_tree is left-odd-right-even, you have to visit all nodes, O(n)
        Best case, the input_tree is empty or has just a child, O(1)"""
        return self.__is_left_odd_right_even(self.root)

    def __is_left_odd_right_even(self, node: BinaryNode) -> bool:
        """checks that all nodes (non-leaves) have a left child with an odd value and a right child with an even value"""
        if node is None or (node.left is None and node.right is None):
            return True

        if node.left is not None and node.right is None:
            return False
        if node.right is not None and node.left is None:
            return False

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

    def check_cousins(self, x: int, y: int) -> bool:
        """returns True if m and y are cousins, and False eoc. Problem Exam May 2020
            Complexity: O(log n)"""

        node_x, parent_x, grand_parent_x = self._search_ancestors(x)
        node_y, parent_y, grand_parent_y = self._search_ancestors(y)

        return parent_x != parent_y and grand_parent_x == grand_parent_y

    def _search_ancestors(self, value: int) -> (BinaryNode, BinaryNode, BinaryNode):
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

    def lwc(self, a: int, b: int) -> int:
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

        # we search a and b in the tree1, and also get their parents.
        node_a, parent_a, _ = self._search_ancestors(a)
        if node_a is None:
            print(a, ' does not exist in the tree1')
            return None

        node_b, parent_b, _ = self._search_ancestors(b)
        if node_b is None:
            print(b, ' does not exist in the tree1')
            return None

        # it could be that a is a descendant of b, or b is a descendant of b
        if self._search(node_a, b) is not None:
            # b is a descendant of a
            if parent_a:
                return parent_a.elem
            return None
        if self._search(node_b, a) is not None:
            # a is a descendant of b
            if parent_b:
                return parent_b.elem
            return None

        return self._lwc(self.root, a, b)

    def _lwc(self, node: BinaryNode, a: int, b: int) -> int:
        if node is None:
            return None
        if a < node.elem and b < node.elem:
            # if a and b are smaller than node.elem, I only have to search on its left child
            return self._lwc(node.left, a, b)
        if a > node.elem and b > node.elem:
            # if a and b are greater than node.elem, I only have to search on its right child
            return self._lwc(node.right, a, b)

        # Case: (a<=node.elem<=b) or (b<=node.elem<=a):
        return node

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

    """
    # Test para _remove() con maximum_node
    input_tree = BST2()
    # input_tree = BinarySearchTree()
    for m in [5, 10, 15, 20, 23, 22, 24, 3, 7, 9, 8]:
        input_tree.insert(m)
    input_tree.draw()
    print("borrar una hoja:", 24)
    input_tree.remove(24)
    input_tree.draw()
    print("borrar un nodo con 1 nodo:", 23)
    input_tree.remove(23)
    input_tree.draw()
    print("borrar un nodo con 2 nodos:", 10)
    input_tree.remove(10)
    input_tree.draw()
    print("borrar root que tiene 2 nodos:", 5)
    input_tree.remove(5)
    input_tree.draw()
    print("borrar root con  1 nodo:", 3)
    input_tree.remove(3)
    input_tree.draw()
    print("borrar root con  2 nodos:", 9)
    input_tree.remove(9)
    input_tree.draw()
    """
    """
    # Test para probar is_size_balanced, is_height_balanced y get_non_leaves
    input_tree2 = BST2()
    # input_tree = BinarySearchTree()
    for m in [15, 10, 5, 20]:
        input_tree2.insert(m)
    input_tree2.draw()
    print("is_size_balanced:", input_tree2.is_size_balanced())
    print("is_height_balanced:", input_tree2.is_height_balanced())
    print("get_non_leaves:", input_tree2.get_non_leaves())

    input_tree2.insert(12)
    print("Después de insertar 12")
    input_tree2.draw()
    print("is_size_balanced:", input_tree2.is_size_balanced())
    print("is_height_balanced:", input_tree2.is_height_balanced())

    # Test para same_shape
    input_tree3 = BinarySearchTree()
    for m in [50, 55, 20, 25]:
        input_tree3.insert(m)
    input_tree3.draw()
    print("same_shape:", input_tree2.same_shape(input_tree3))
    input_tree3.insert(15)
    input_tree3.draw()
    print("same_shape:", input_tree2.same_shape(input_tree3))
    """
    """
    # Test para probar is_zig_zag
    input_tree = BST2()
    for m in [50, 90, 70, 80, 75]:
        input_tree.insert(m)
    input_tree.draw()
    print("is_zig_zag: ", input_tree.is_zig_zag())
    input_tree.insert(30)
    input_tree.draw()
    print("is_zig_zag: ", input_tree.is_zig_zag())
    print("is_left_odd_right_even: ", input_tree.is_left_odd_right_even())
    """

    """
    # Test para probar is_left_odd_right_even
    input_tree = BST2()
    for m in [50, 31, 70, 55, 25, 36, 80]:
        input_tree.insert(m)
        input_tree.draw()
        print("is_left_odd_right_even: ", input_tree.is_left_odd_right_even())
    """

    """
    # Test para closest:
    input_tree = BST2()
    for m in [10, 20, 6, 15, 18, 17, 19]:
        input_tree.insert(m)
    input_tree.draw()

    for v in [8, 7, 18, 16, 11, 12, 13, 22]:
        print("closest({})={}".format(v, input_tree.closest(v)))
    """
    """
    input_tree = BST2()
    for number in [15, 3, 1, 5, 30, 20, 40, 6]:
        input_tree.insert(number)
    input_tree.draw()
    i, j = 15, 3
    print("check_cousins({},{})={}".format(i, j, input_tree.check_cousins(i, j)))
    i, j = 3, 30
    print("check_cousins({},{})={}".format(i, j, input_tree.check_cousins(i, j)))
    i, j = 1, 20
    print("check_cousins({},{})={}".format(i, j, input_tree.check_cousins(i, j)))
    i, j = 5, 20
    print("check_cousins({},{})={}".format(i, j, input_tree.check_cousins(i, j)))

    i, j = 15, 3
    print("lwc({},{})={}".format(i, j, input_tree.lwc(i, j)))
    i, j = 3, 30
    print("lwc({},{})={}".format(i, j, input_tree.lwc(i, j)))
    i, j = 1, 20
    print("lwc({},{})={}".format(i, j, input_tree.lwc(i, j)))
    i, j = 1, 30
    print("lwc({},{})={}".format(i, j, input_tree.lwc(i, j)))
    i, j = 20, 3
    print("lwc({},{})={}".format(i, j, input_tree.lwc(i, j)))
    i, j = 30, 40
    print("lwc({},{})={}".format(i, j, input_tree.lwc(i, j)))
    i, j = 1, 3
    print("lwc({},{})={}".format(i, j, input_tree.lwc(i, j)))
    i, j = 5, 6
    print("lwc({},{})={}".format(i, j, input_tree.lwc(i, j)))
    i, j = 3, 6
    print("lwc({},{})={}".format(i, j, input_tree.lwc(i, j)))
    """

    #
    input_tree = BST2()
    for m in [15, 3, 1, 5, 30, 20, 40]:
        input_tree.insert(m)
    input_tree.draw()
    # Lo pasamos a MyBinaryTree
    print(input_tree.level_order_list())
    print('Antes de update_adding_left_child:')
    input_tree.draw()
    input_tree.update_adding_left_child()
    print('Después de update_adding_left_child:')
    input_tree.draw()
    print(input_tree.level_order_list())
