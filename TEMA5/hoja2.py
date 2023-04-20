from bst import BinarySearchTree
from bintree import BinaryNode
import bintree as bin


def get_smallest_ite(tree: BinarySearchTree) -> int:
    """returns the smallest element in input_tree. O(log n)"""
    result = None
    if tree is None:
        print("Tree is None!!!")
    else:
        node = tree.root
        if node is None:
            print("the root is None")
        else:
            while node.left:
                node = node.left
            result = node.elem
    return result


def get_greatest_ite(tree: BinarySearchTree) -> int:
    """returns the greatest element in input_tree. O(log n)"""
    result = None
    if tree is None:
        print("Tree is None!!!")
    else:
        node = tree.root
        if node is None:
            print("the root is None")
        else:
            while node.right:
                node = node.right
            result = node.elem
    return result


def get_smallest_rec(tree: BinarySearchTree) -> int:
    """returns the smallest element in input_tree"""
    result = None
    if tree is None:
        print("Tree is None!!!")
    else:
        result = _get_smallest_rec(tree.root)
    return result


def _get_smallest_rec(node: BinaryNode) -> int:
    result = None
    if node is not None:
        if node.left:
            result = _get_smallest_rec(node.left)
        else:
            return node.elem
    return result

def sum_elements(tree: BinarySearchTree) -> int:
    """returns the sum of the elements. O(n)"""
    result = None
    if tree is None:
        print("input_tree is None!!!")
    else:
        elements = tree.inorder_list()
        result = sum(elements)
    return result

def sum_elements_rec(tree: BinarySearchTree) -> int:
    """returns the sum of the elements. O(n)"""
    result = None
    if tree is None:
        print("input_tree is None!!!")
    else:
        result = _sum_elements_rec(tree.root)
    return result

def _sum_elements_rec(node: BinaryNode) -> int:
    """returns the sum of all elements in the subtree node"""
    result = 0
    if node is not None:
        result = node.elem + _sum_elements_rec(node.left) + _sum_elements_rec(node.right)
    return result


def _maximum_node(subtree: BinaryNode) -> BinaryNode:
    """gets a node (subtree) and returns the node with the biggest
    element in the subtree. O(log n)"""
    result = None
    if subtree is not None:
        biggest = subtree
        while biggest.right:
            biggest = biggest.right
        result = biggest
    return result


def _remove(node: BinaryNode, elem: object) -> BinaryNode:
    """It recursively searches the node. When the node is
    found, the node has to be removed"""
    if node is None:
        print(elem, ' not found')
    elif elem < node.elem:
        node.left = _remove(node.left, elem)
    elif elem > node.elem:
        node.right = _remove(node.right, elem)
    else:  # node.elem == elem, node is the node to remove!!!
        if node.left is None and node.right is None:
            # Case 1: node is a leave
            node = None
        elif node.left is None:  # Case 2: only has a right child
            node = node.right
        elif node.right is None:    # Case 2: only has a left child
            node = node.left
        else:  # Case 3: node.left!=None and node.right!=None
            # we search the biggest node from its left child
            predecessor = _maximum_node(node.left)
            # we replace elem with the elem of the successor
            node.elem = predecessor.elem
            # now, we have to remove successor from the right child
            node.left = _remove(node.left, predecessor.elem)

    return node

def _fe_size(node: BinaryNode) -> int:
    """returns the size balance factor of the input node"""
    if node is None:
        return 0
    return abs(bin._size(node.left) - bin._size(node.right))

def is_size_balanced(tree: BinarySearchTree) -> bool:
    """return True if the input_tree is size balanced"""
    return _is_size_balanced(tree.root)

def _is_size_balanced(node: BinaryNode) -> bool:
    """returns True if the node is size balanced;
    a node is balanced if its size factor is <=1 and
    its two children are size balanced"""
    if node:
        return _fe_size(node) <= 1 and _is_size_balanced(node.left) and \
               _is_size_balanced(node.right)

    return True

def _fe_height(node: BinaryNode) -> int:
    """returns the height balance factor of the input node"""
    if node is None:
        return 0
    return abs(bin._height(node.left) - bin._height(node.right))

def is_height_balanced(tree) -> bool:
    """return True if the input_tree is height balance, that is,
    if its root is height balanced"""
    return _is_height_balanced(tree.root)

def _is_height_balanced(node: BinaryNode) -> bool:
    """return True if the node is balanced, False e.o.c
    A node is balanced if its height balance <=1 and
    its two children are height balanced"""
    if node:
        return _fe_height(node) <= 1 and \
            _is_height_balanced(node.left) and \
            _is_height_balanced(node.right)

    return True


def same_shape(tree1: BinarySearchTree, tree2: BinarySearchTree) -> bool:
    result = False
    if tree1 is not None and tree2 is not None:
        result = _same_shape(tree1.root, tree2.root)
    return result

def _same_shape(node1: BinaryNode, node2: BinaryNode) -> bool:
    result = False
    if node1 is None and node2 is None:
        result = True
    elif node1 is not None and node2 is not None:
        result = _same_shape(node1.left, node2.left) and \
                 _same_shape(node1.right, node2.right)
    return result

def get_non_leaves(tree) -> list:
    """returns a list with the elements of the nodes that are not leaves.
    Complexity O(n).
    The list has to be sorted in ascending order."""
    result = []
    _get_non_leaves(tree.root, result)
    return result

def _get_non_leaves(node: BinaryNode, lst_nodes: list) -> None:
    """ Complexity: O(n) """
    if node:
        _get_non_leaves(node.right, lst_nodes)
        if node.left or node.right:
            lst_nodes.append(node.elem)
        _get_non_leaves(node.left, lst_nodes)

def is_zig_zag(tree: BinarySearchTree) -> bool:
    """returns True if the input_tree is a ziz-zag-shaped input_tree, False eoc.
    Worst case: The input_tree is zig-zag, we have to visit all nodes, O(n)
    Best case: the input_tree is empty or the root has two children"""

    if tree.root is None or tree.size() <= 2:
        return False

    return _is_zig_zag(tree.root, None)

def _num_children(node: BinaryNode) -> int:
    """returns the number of children of node.
    O(1)"""
    count = 0
    if node:
        if node.left:
            count += 1
        if node.right:
            count += 1
    return count

def _is_zig_zag(node: BinaryNode, origin: str) -> bool:
    """returns True if the node has a zig-zag-shape, False eoc"""
    # print(node, origin)
    if _num_children(node) == 0:
        return True

    if _num_children(node) == 2:
        return False

    # node only has left or right
    if node.left:
        return _is_zig_zag(node.left, "left") if origin != "left" else False

    # then, node has a right child
    return _is_zig_zag(node.right, "right") if origin != "right" else False

def is_left_odd_right_even(tree: BinarySearchTree) -> bool:
    """checks that all nodes (non-leaves) have a left child with an odd value and a right child with an even value.
    Wort case, the input_tree is left-odd-right-even, you have to visit all nodes, O(n)
    Best case, the input_tree is empty or has just a child, O(1)"""
    if _num_children(tree.root) <= 1:
        return False

    return _is_left_odd_right_even(tree.root)

def _is_left_odd_right_even(node: BinaryNode) -> bool:
    """checks that all nodes (non-leaves) have a left child with an odd value and a right child with an even value"""
    if _num_children(node) == 0:  # If the node is a leaf, we return True
        return True
    if _num_children(node) == 1:  # If the node is a leaf, we return False
        return False
    # node has two children
    # the left elem is even or the right elem is odd
    if node.left.elem % 2 == 0 or node.right.elem % 2 != 0:
        return False
    # eoc, we have to check node.left and node.right
    return _is_left_odd_right_even(node.left) and _is_left_odd_right_even(node.right)


def array2bst(input_list: list) -> BinarySearchTree:
    """ gets a sorted list and creates a balanced bst"""
    result = BinarySearchTree()
    if input_list and len(input_list) >= 1:
        _array2bst(input_list, 0, len(input_list)-1, result)
    return result

def _array2bst(input_list: list, start: int, end: int,
               tree: BinarySearchTree) -> None:
    if start <= end:
        index_mid = (start + end) // 2
        tree.insert(input_list[index_mid])
        _array2bst(input_list, start, index_mid-1, tree)
        _array2bst(input_list, index_mid+1, end, tree)


def _array2bst2(input_list: list, tree: BinarySearchTree) -> None:
    if len(input_list) > 0:
        index_mid = len(input_list) // 2
        tree.insert(input_list[index_mid])

        _array2bst2(input_list[:index_mid], tree)
        _array2bst2(input_list[index_mid+1:], tree)



class BSTRemove2(BinarySearchTree):
    def remove(self, elem: object) -> None:
        # update the root with the new subtree after remove elem
        self._root = _remove(self._root, elem)


if __name__ == "__main__":

    input_tree = BinarySearchTree()
    values = [25, 20, 36, 10, 22, 30, 40, 5, 12, 28, 38, 48]
    for x in values:
        input_tree.insert(x)
    input_tree.draw()
    print("get_non_leaves: ", get_non_leaves(input_tree))
    print("is_zig_zag: ", is_zig_zag(input_tree))

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
    input_tree = BinarySearchTree()
    for x in [10, 20, 15, 18, 17, 19]:
        input_tree.insert(x)
        input_tree.draw()
        print("is_zig_zag:", is_zig_zag(input_tree))

