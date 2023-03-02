# -*- coding: utf-8 -*-

from dlist import DList

import unittest


class Test(unittest.TestCase):

    def setUp(self):
        """This function is executed for each of the test functions"""
        self.lEmpty = DList()

        self.l1 = DList()
        self.l1.add_first('a')

        self.l4 = DList()
        self.l4.add_first('r')
        self.l4.add_first('a')
        self.l4.add_first('z')
        self.l4.add_first('a')

    def test1_len(self):
        print('Case 1: len in a list of length ==0')
        expected = []
        self.assertEqual(len(self.lEmpty), len(expected), "Fail: len in a length of length==0")

    def test2_len(self):
        print('Case 2: len in a list of length > 0')
        self.assertEqual(len(self.l4), 4, "Fail: len in a dequeue of length>0")

        expected = ['a', 'z', 'a', 'r']
        self.assertEqual(len(self.l4), len(expected), "Fail: len in a dequeue of length>0")
        print()

    def test3_add_last(self):
        print('Case 3: add_last in an empty list')
        self.lEmpty.add_last('i')
        expected = ['i']

        self.assertEqual(str(self.lEmpty), str(expected), "Fail: add_last in a list of length==0")

    def test4_add_last(self):
        print('Case 4: add_last in a list non-empty')
        self.l4.add_last('.')
        expected = ['a', 'z', 'a', 'r', '.']
        self.assertEqual(str(self.l4), str(expected), "Fail: add_last in a list of length>0")
        print()

    def test5_add_last(self):
        print('Case 4: add_last in a list of size 1')
        self.l1.add_last('z')
        expected = ['a', 'z']
        self.assertEqual(str(self.l1), str(expected), "Fail: add_last in a list of length==1")
        print()

    def test6_remove_first(self):
        print('Case 6: remove_first in an empty list')
        first = self.lEmpty.remove_first()

        expected = []
        self.assertEqual(first, None, "Fail: remove_first in a list of length==0")
        self.assertEqual(str(self.lEmpty), str(expected), "Fail: remove_first in a list of length == 0")

    def test7_remove_first(self):
        print('Case 7: remove_first in a dequeue of list 1')

        first = self.l1.remove_first()
        expected = []
        self.assertEqual(first, 'a', "Fail: remove_first in a list of length>1")
        self.assertEqual(str(self.l1), str(expected), "Fail: remove_first in a list of length == 1")

    def test8_remove_first(self):
        print('Case 8: remove_first in a list of length >1')
        top_expected = self.l4.remove_first()
        expected = ['z', 'a', 'r']
        self.assertEqual(top_expected, 'a', "Fail: remove_first in a list of length>1")
        self.assertEqual(str(self.l4), str(expected), "Fail: remove_first in a list of length>1")
        print()

    def test9_remove_last(self):
        print('Case 9: remove_last in an empty list')
        top_expected = self.lEmpty.remove_last()
        expected = []
        self.assertEqual(top_expected, None, "Fail: remove_first in an empty list")

        self.assertEqual(str(self.lEmpty), str(expected), "Fail: remove_last in an empty list")

    def test10_remove_last(self):
        print('Case 10: remove_last in a list of length 1')
        top_expected = self.l1.remove_last()
        expected = []
        self.assertEqual(top_expected, 'a', "Fail: remove_last in a list of length==1")
        self.assertEqual(str(self.l1), str(expected), "Fail: remove_last in a list of length == 1")

    def test_11_remove_last(self):
        print('Case 11: remove_last in a dequeue of length > 1')
        top_expected = self.l4.remove_last()
        expected = ['a', 'z', 'a']
        self.assertEqual(top_expected, 'r', "Fail: remove_last in a list of length>1")
        self.assertEqual(str(self.l4), str(expected), "Fail: remove_last in a list of length == 1")
        print()

    def test_12_getAt(self):
        print('Case 12: getAt')
        expected = ['a', 'z', 'a', 'r']
        for i in range(len(self.l4)):
            self.assertEqual(self.l4.getAt(i), expected[i], "Fail: front in a dequeue empty")

    def test_13_index(self):
        print('Case 13: index of an element that does not exist')
        self.assertEqual(self.l4.index('b'), -1, "Fail: index of an element")

    def test_14_index(self):
        print('Case 14: index of an element that does not exist')
        self.assertEqual(self.l4.index('a'), 0, "Fail: index of an element")
        self.assertEqual(self.l4.index('r'), 3, "Fail: index of an element")

    def test_15_insertAt(self):
        print('Case 15: insertAt(0,C) ')
        self.l4.insertAt(0, 'C')
        expected = ['C', 'a', 'z', 'a', 'r']
        self.assertEqual(str(self.l4), str(expected), "Fail: 15: insertAt(0,C) ")

    def test_16_insertAt(self):
        print('Case 16: insertAt(len,.) ')
        self.l4.insertAt(4, '.')
        expected = ['a', 'z', 'a', 'r', '.']
        self.assertEqual(str(self.l4), str(expected), "Fail: 16: insertAt(len(l4),.) ")

    def test_17_insertAt(self):
        print('Case 17: insertAt(2,C) ')
        self.l4.insertAt(2, 'C')
        expected = ['a', 'z', 'C', 'a', 'r']
        self.assertEqual(str(self.l4), str(expected), "Fail: 'Case 17: insertAt(2,C) ")

    def test_18_insertAt(self):
        print('Case 18: removeAt(0) ')
        self.l4.removeAt(0)
        expected = ['z', 'a', 'r']
        self.assertEqual(str(self.l4), str(expected), "Fail: 18: removeAt(0)")

    def test_19_removeAt(self):
        print('Case 19: removeAt(len), out of range')
        self.l4.removeAt(4)
        expected = ['a', 'z', 'a', 'r']
        self.assertEqual(str(self.l4), str(expected), "Case 19: removeAt(len), out of range")

    def test_20_remveAt(self):
        print('Case 20: removeAt(2) ')
        self.l4.removeAt(2)
        expected = ['a', 'z', 'r']
        self.assertEqual(str(self.l4), str(expected), "Fail: 'Case 20: removeAt(2) ")


# If you are using Spyder, please comment the following line:
# unittest.main(argv=['first-arg-is-ignored'], exit=False)

# To use Spyder, remove the following comments:
if __name__ == '__main__':
    unittest.main()
