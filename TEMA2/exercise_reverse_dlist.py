# -*- coding: utf-8 -*-
from dlist import DList
import random


class DList2(DList):

    def reverse1(self) -> None:
        """reverse the list by swapping the elements"""
        left = self._head
        right = self._tail
        m = len(self)//2
        i = 0
        while i < m:  # just need to iterate len(self)//2 iterations, the half of the list
            # swap the elements
            left.elem, right.elem = right.elem, left.elem
            left = left.next
            right = right.prev
            i += 1

    def reverse2(self):
        """ reverse the list by swapping the references of the nodes"""
        node = self._head
        while node:
            # for each node, we swap its references
            node.next, node.prev = node.prev, node.next
            # we have to move forward to the tail (so we have to move to prev, which was next previously)
            node = node.prev

        # finally, we have to swap head and  tail
        self._head, self._tail = self._tail, self._head
                

if __name__ == '__main__':
    my_list = DList2()
    # we randomly create the size of the list
    size_list = random.randint(0, 5)
    for _ in range(size_list):
        # we add random numbers to the list
        my_list.add_last(random.randint(-10, 10))

    print(' before to reverse:', my_list)
    # Please, uncomment just one of the two calls: reverse1 or reverse2
    # my_list.reverse1()
    my_list.reverse2()
    print(' after to reverse:', my_list)
