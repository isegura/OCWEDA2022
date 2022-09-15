import unittest
from bst import BinarySearchTree
from bst import BinaryNode


class Test(unittest.TestCase):
    def setUp(self):
        self.empty = BinarySearchTree()
        self.tree = BinarySearchTree()
        self.data = [50, 55, 54, 20, 60, 15, 18, 5, 25, 24, 75, 80]
        for x in self.data:
            self.tree.insert(x)
            self.tree.draw()
        self.data1 = [55, 54, 60, 75, 80]
        self.tree1 = BinarySearchTree()
        for x in self.data1:
            self.tree1.insert(x)

        self.data2 = [20, 25, 24, 15, 18, 5]
        self.tree2 = BinarySearchTree()
        for x in self.data2:
            self.tree2.insert(x)

        self.data3 = [25, 24]
        self.tree3 = BinarySearchTree()
        for x in self.data3:
            self.tree3.insert(x)

        self.data4 = [60, 75, 80]
        self.tree4 = BinarySearchTree()
        for x in self.data4:
            self.tree4.insert(x)

        self.treeL = BinarySearchTree()
        self.dataL = [50, 20, 15, 18, 5]
        for x in self.dataL:
            self.treeL.insert(x)
        # self.treeL.draw()

        self.treeR = BinarySearchTree()
        self.dataR = [50, 60, 55, 75, 80]
        for x in self.dataR:
            self.treeR.insert(x)
        # self.treeL.draw()

    def testSize(self):
        self.assertEqual(self.empty.size(), 0)
        self.empty.insert(5)
        self.assertEqual(self.empty.size(), 1)
        self.empty.insert(6)
        self.assertEqual(self.empty.size(), 2)
        self.assertEqual(self.tree.size(), 12)

    def testHeight(self):
        self.assertEqual(self.empty.height(), -1)
        self.empty.insert(5)
        self.assertEqual(self.empty.height(), 0)
        self.empty.insert(6)
        self.assertEqual(self.empty.height(), 1)
        self.assertEqual(self.tree.height(), 4)

    def testSearch(self):
        self.assertIsNone(self.empty.search(0))
        self.assertEqual(self.tree.search(50), self.tree._root)
        self.assertEqual(self.tree.search(55), self.tree1._root)
        self.assertEqual(self.tree.search(20), self.tree2._root)
        self.assertEqual(self.tree.search(18), BinaryNode(18))
        self.assertEqual(self.tree.search(25), self.tree3._root)
        self.assertEqual(self.tree.search(60), self.tree4._root)

    def testRemove(self):
        expected = BinarySearchTree()
        for x in self.data:
            expected.insert(x)
        self.tree.remove(0)
        self.assertEqual(self.tree, expected)

    def testRemove1(self):
        # leaf: right child
        expected = BinarySearchTree()
        for x in [50, 55, 54, 20, 60, 15, 18, 5, 25, 24, 75]:
            expected.insert(x)
        # expected.draw()
        self.tree.remove(80)
        # self.tree.draw()
        self.assertEqual(self.tree, expected)

    def testRemove2(self):
        # left child is a leaf
        expected = BinarySearchTree()
        for x in [50, 55, 54, 20, 60, 15, 18, 25, 24, 75, 80]:
            expected.insert(x)
        self.tree.remove(5)
        self.assertEqual(self.tree, expected)

    def testRemove3(self):
        # left child is a leaf
        expected = BinarySearchTree()
        for x in [50, 55, 54, 20, 60, 15, 5, 25, 24, 75, 80]:
            expected.insert(x)
        self.tree.remove(18)
        self.assertEqual(self.tree, expected)

    def testRemove4(self):
        # node with a right child
        expected = BinarySearchTree()
        for x in [50, 55, 54, 20, 15, 18, 5, 25, 24, 75, 80]:
            expected.insert(x)
        self.tree.remove(60)
        self.assertEqual(self.tree, expected)

    def testRemove5(self):
        # node with a left child
        expected = BinarySearchTree()
        for x in [50, 55, 54, 20, 60, 15, 18, 5, 24, 75, 80]:
            expected.insert(x)
        self.tree.remove(25)
        self.assertEqual(self.tree, expected)

    def testRemove6(self):
        # node with two children
        expected = BinarySearchTree()
        for x in [50, 55, 54, 20, 60, 18, 5, 25, 24, 75, 80]:
            expected.insert(x)
        # expected.draw()
        self.tree.remove(15)
        # self.tree.draw()

        self.assertEqual(self.tree, expected)

    def testRemove7(self):
        # two children
        expected = BinarySearchTree()
        for x in [50, 55, 54, 60, 24, 15, 18, 5, 25, 75, 80]:
            expected.insert(x)
        # expected.draw()

        self.tree.remove(20)
        # self.tree.draw()

        self.assertTrue(self.tree == expected)

    def testRemove9(self):
        # remove the root
        expected = BinarySearchTree()
        for x in [54, 55, 20, 60, 15, 18, 5, 25, 24, 75, 80]:
            expected.insert(x)
        # expected.draw()

        self.tree.remove(50)
        # self.tree.draw()

        self.assertTrue(self.tree == expected)

    def testRemove10(self):
        # remove the root
        self.tree.remove(54)

        expected = BinarySearchTree()
        for x in [55, 20, 60, 15, 18, 5, 25, 24, 75, 80]:
            expected.insert(x)
        # expected.draw()

        self.tree.remove(50)
        # self.tree.draw()

        self.assertTrue(self.tree == expected)

    def test_remove11(self):
        expected = BinarySearchTree()
        for x in [50, 55, 54, 20, 60, 15, 18, 5, 25, 24, 80]:
            expected.insert(x)
        # print(self.data)
        # expected.draw()
        self.tree.remove(75)
        self.assertTrue(self.tree == expected)

    def test_remove12(self):
        x = 24
        expected = BinarySearchTree()
        for e in [50, 20, 55, 15, 5, 25, 18, 54, 60, 75, 80]:
            expected.insert(e)
        # expected.draw()
        self.tree.remove(x)
        # self.tree.draw()

        self.assertTrue(self.tree == expected)
        print('\n\ttest_remove12 was OK!!!')

    def test_remove13(self):
        x = 50
        self.dataL.remove(x)
        print('\n\test_remove13: remove the root with only left children ({})'.format(x))

        expected = BinarySearchTree()
        for e in self.dataL:
            expected.insert(e)
        # expected.draw()

        self.treeL.remove(x)
        # self.treeL.draw()
        self.assertEqual(self.treeL, expected)
        print('\n\test_remove13 was OK!!!')

    def test_remove14(self):
        x = 50
        self.dataR.remove(x)
        print('\n\test_remove14: remove the root with only left children ({})'.format(x))

        # print(self.data)

        expected = BinarySearchTree()
        for e in self.dataR:
            expected.insert(e)
        # self.treeR.draw()

        self.treeR.remove(x)

        self.assertEqual(self.treeR, expected)
        print('\n\test_remove14 was OK!!!')

    def test_remove15(self):
        print('\n\test_remove15 the root without children!!!')
        tree = BinarySearchTree()
        tree.insert(5)
        tree.remove(5)
        self.assertIsNone(tree._root)
        print('\n\test9_remove was OK!!!')

    def test_remove16(self):
        """removing a node cause an unbalanced node
        that has to be balanced applying a right rotation"""
        data = [12, 8, 18, 6, 20, 14, 4, 2]
        tree = BinarySearchTree()
        for n in data:
            tree.insert(n)
        # tree.draw()

        print("after remove 8")
        tree.remove(8)
        # tree.draw()

        expected = BinarySearchTree()
        for e in [12, 18, 6, 20, 14, 4, 2]:
            expected.insert(e)
        # expected.draw()
        self.assertEqual(tree, expected)
