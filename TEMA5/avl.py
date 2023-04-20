from bst import BinarySearchTree
from bintree import BinaryNode
import bintree as bin
import bst

def balance_factor(node: BinaryNode) -> int:
    """returns the balance factor of node.
    It is the height of its right subtree minus
    the height of its left subtree"""
    if node is None:
        return 0

    return bin._height(node.right) - bin._height(node.left)

def _insert(node: BinaryNode, elem: object) -> BinaryNode:
    node = bst._insert(node, elem)
    node = rebalance(node)
    return node

def _remove(node: BinaryNode, elem: object) -> BinaryNode:
    node = bst._remove(node, elem)
    node = rebalance(node)
    return node

def rebalance(node: BinaryNode) -> BinaryNode:
    # O(logn)
    if abs(balance_factor(node)) <= 1:
        return node  # the node is already balanced, we do nothing

    print('balancing ', node.elem)

    height_left = bin._height(node.left)
    height_right = bin._height(node.right)

    # the left branch is larger than the right branch
    # so we have to do a right rotation
    if height_left > height_right:  # right rotate
        # as it is greater, node.left cannot be None,
        height_left_left = bin._height(node.left.left)
        height_left_right = bin._height(node.left.right)
        if height_left_left < height_left_right:
            # print(' double first left rotation on: ', node.elem)
            node.left = left_rotate(node.left)
            # print('right rotation on ', node.elem)
        node = right_rotate(node)
    else:  # left rotate
        height_right_left = bin._height(node.right.left)
        height_right_right = bin._height(node.right.right)
        if height_right_right < height_right_left:  # double rotation (right - left)
            # print(' double first right rotation on: ', node.elem)
            node.right = right_rotate(node.right)
            # print('left rotation on ', node.elem)
        node = left_rotate(node)
    return node

def right_rotate(node: BinaryNode) -> BinaryNode:
    """balance node by right rotation """
    # its child left becomes the new root (and we will return it)
    new_root = node.left  # it will be the new root
    # we save the right child of new_root (because it will become the left childe of node)
    subtree = new_root.right
    # node becomes the right child of new_root
    new_root.right = node
    # the (old) right child of new_root has to be the left child of node
    node.left = subtree
    # print(new_root.left.elem,new_root.elem,new_root.right.elem)
    return new_root

def left_rotate(node: BinaryNode) -> BinaryNode:
    """balance node applying left rotation"""
    # print("left rotation on ", node.key)
    # its right child becomes the new root of the subtree
    # Also, the function will return new_root
    new_root = node.right
    # we save the left child of new_root, because
    # it becomes the right child of node
    subtree = new_root.left

    # we have to update the parent for newRoot
    new_root.left = node
    # now, the old left child of new_root has to be
    # the right child of node
    node.right = subtree

    return new_root


class AVLTree(BinarySearchTree):

    # Override insert method from base class to keep it as AVL
    def insert(self, elem: object) -> None:
        """inserts a new node, with key and element elem"""
        self._root = _insert(self._root, elem)

    # Override remove method from base class to keep it as AVL
    def remove(self, elem: object) -> None:
        self._root = _remove(self._root, elem)


if __name__ == "__main__":
    tree = AVLTree()
    """
    for x in [10, 20, 30, 5]:
        print('insert ', x)
        tree.insert(x)
        tree.draw()
    print('remove 30')
    tree.remove(30)
    tree.draw()
    print('insert 8')
    tree.insert(8)
    tree.draw()
    print('remove 20')
    tree.remove(20)
    tree.draw()

    print('insert 9')
    tree.insert(9)
    tree.draw()
    print('remove 5')
    tree.remove(5)
    tree.draw()
    """
    # rotation simple left
    print("inserting 30")
    tree.insert(30)
    tree.draw()
    print("inserting 50")
    tree.insert(50)
    tree.draw()
    print("inserting 60")
    tree.insert(60)
    tree.draw()
    print("inserting 25")
    tree.insert(25)
    tree.draw()
    # If we insert 15, 30 and 50 will be unbalanced.
    # We apply simple rotation right on 30.
    print("inserting 15")
    tree.insert(15)
    tree.draw()
    # If we insert 35, 50 will be unbalanced.
    # We must apply double rotation left-right on 50.ç
    print("inserting 35")
    tree.insert(35)
    tree.draw()
    print("inserting 55")
    tree.insert(55)
    tree.draw()
    print("inserting 65")
    tree.insert(65)
    tree.draw()
    # If we insert 52, 50 will be unbalanced with the
    # longest branch from 50-60-55.
    # We must apply double rotation right-left
    print("inserting 52")
    tree.insert(52)
    tree.draw()
