# -*- coding: utf-8 -*-
from slistHT import SList
import random


class SList2(SList):
    def remove_byindex(self, e: object) -> None:
        """remove the first occurrence of e in the list. If e does not exist, it prints a message. 
        This solution is based on the methods index and remove"""
        index = self.index(e)
        if index != -1:
            self.removeAt(index)
        else:
            print(e, ' does not exist!!!')
    
    def remove2(self, e: object) -> None:
        """remove the first occurrence of e in the list. If e does not exist, it prints a message. 
        This solution does not  use any method of the SList class"""
        prev = None
        node_it = self._head
        found = False
        while not found and node_it:  # node_it!=None
            if node_it.elem == e:
                # remove node
                if prev is None:
                    # it is the first node
                    self._head = self._head.next
                    if self._head is None:
                        self._tail = None
                else:
                    # it's not the first node
                    prev.next = node_it.next
                    if node_it.next is None:
                        # node_it was the last node
                        self._tail = prev

                self._size -= 1
                found = True
            else:
                prev = node_it
                node_it = node_it.next
                
        if not found:
            print(e, ' does not exist!!!')

    def remove2(self, e: object) -> None:
        """a different version of remove"""
        previous = None
        node_it = self._head
        while node_it is not None and node_it.elem != e:
            mode_it = node_it.next

        if node_it is None:
            print(e, ' does not exist')
        else:
            #node_it is the node to remove
            if previous is None:
                self._head = self._head.next
                if self._head is None:
                    self._tail = None
            else:
                previous.next = node_it.next
                if node_it is self._tail:
                    self._tail = previous

            self._size -= 1

    def remove_all_byindex(self, e: object) -> None:
        """This solution is based on the functions index and removeAt"""
        index = self.index(e)
        while index != -1:
            self.removeAt(index)
            index = self.index(e)
            
    def remove_all(self, e: object) -> None:
        """This solution does not use any method of the SList class"""
        prev = None
        node_it = self._head
        found = False
        while node_it:  # node_it! = None
            if node_it.elem == e:
                # remove node
                if prev is None:
                    # it is the first node
                    self._head = self._head.next
                    if self._head is None:
                        self._tail = None
                else:
                    # it's not the first node
                    prev.next = node_it.next
                    if node_it.next is None:
                        # node_it was the last node
                        self._tail = prev
                self._size -= 1
                if not found:
                    found = True
            else:
                prev = node_it

            node_it = node_it.next

        if not found:
            print(e, ' does not exist!!!')

    def getAtRev_v1(self, index: int) -> object:
        """This solution is based on the method getAt"""
        result = None
        n = len(self)
        if 0 <= index < n:
            result = self.getAt(n-1-index)
        else:
            print(index, ' wrong!!!')
        return result

    def getAtRev(self, index: int) -> object:
        """This method does not use any methods"""
        result = None
        n = len(self)
        if 0 <= index < n:
            j = 0
            node_it = self._head
            while index < n-1-j:
                node_it = node_it.next
                j += 1
            result = node_it.elem
        else:
            print(index, ' wrong!!!')
        return result

    def get_middle_v1(self) -> object:
        result = None
        if self.is_empty():
            print('An empty list does not have middle!!!')
        else:
            m = len(self)//2
            result = self.getAt(m)
        return result

    def get_middle(self) -> object:
        node_it = self._head
        cont = 0
        while node_it:
            if cont == len(self) // 2:
                return node_it.elem
            node_it = node_it.next
            cont += 1
        return None

    def count(self, e: object) -> int:
        result = 0
        node_it = self._head
        while node_it:
            if node_it.elem == e:
                result += 1
            node_it = node_it.next
        return result

    def is_sorted(self) -> bool:
        """ returns True if the list is sorted. We consider that empty lists are sorted"""
        if len(self) > 1:
            node1 = self._head
            node2 = node1.next
            for _ in range(1, len(self)):
                if node1.elem > node2.elem:
                    return False
                node1 = node2
                node2 = node2.next

        return True

    def remove_duplicates_sorted_v1(self) -> None:
        """This method removes the duplicate elements in a sorted list.
        The method uses other methods of the class"""
        if self.is_sorted():
            if len(self) > 1:
                k = 1
                while k < len(self):
                    if self.getAt(k-1) == self.getAt(k):
                        self.removeAt(k)
                    else:
                        k += 1
        else:
            print('list is not sorted!!!')

    def remove_duplicates_sorted(self):
        """This method removes the duplicate elements in a sorted list.
        The method does not use any method of the class SList"""
        if self.is_sorted():
            if len(self) > 1:
                prev = self._head
                node_it = prev.next
                while node_it:
                    if prev.elem == node_it.elem:
                        prev.next = node_it.next
                        if node_it.next is None:
                            self._tail = prev
                        self._size -= 1
                        node_it = node_it.next
                    else:
                        prev = node_it
                        node_it = node_it.next

        else:
            print('list is not sorted!!!')

    def remove_duplicates(self) -> None:
        """This method removes the duplicate elements in a list.
        The method does not use any method of the class SList"""
        node_it = self._head
        while node_it:
            prev = node_it
            node_it2 = node_it.next
            e = node_it.elem
            while node_it2:
                if e == node_it2.elem:
                    prev.next = node_it2.next
                    if node_it2.next is None:
                        self._tail = prev
                    self._size -= 1
                else:
                    prev = node_it2
                node_it2 = node_it2.next

            node_it = node_it.next

    def swap_pairwise(self) -> None:
        """ swaps the continues elements in the list. If the list has an odd number of elements,
        the last element is not swapped"""
        if len(self) > 1:
            node1 = self._head
            node2 = node1.next
            while node1 and node2:
                # swap elements
                node1.elem, node2.elem = node2.elem, node1.elem
                node1 = node2.next
                if node1:
                    node2 = node1.next

    def move_last_v1(self) -> None:
        """This method moves the last element to the front of the list. 
         It uses other methods of the class"""
        if len(self) > 1:
            x = self.remove_last()
            self.add_first(x)
            
    def move_last(self) -> None:
        """This method moves the last element to the front of the list. 
         It does not use any method of the class"""
        if self._size == 0:
            print('list is empty!!')
        else:
            next_to_last = None
            last = self._head
            while last != self._tail:
                next_to_last = last
                last = last.next
            
            last.next = self._head
            self._head = last
            
            next_to_last.next = None
            self._tail = next_to_last

    def intersection(self, other_list: "SList2") -> "SList2":
        """ returns a new list that is contains the elements that are in both lists"""
        output = SList2()
        if self.is_sorted() and other_list.is_sorted():
            node1 = self._head
            node2 = other_list._head

            while node1:
                while node2 and node2.elem < node1.elem:
                    node2 = node2.next
                if node2 is not None and node2.elem == node1.elem:
                    output.add_last(node1.elem)
                    node2 = node2.next
                node1 = node1.next

        return output

    def segregate_odd_even(self):
        """ updates de list to contains first the even numbers and after the odd numbers. The order of the numbers must
        be kept"""
        if len(self) > 1:
            evens = SList2()
            odds = SList2()
            node = self._head
            while node:
                e = node.elem
                if e%2 == 0:
                    evens.add_last(e)
                else:
                    odds.add_last(e)

                node = node.next

            if evens.is_empty():
                self._head = odds._head
                self._tail = odds._tail
            elif odds.is_empty():
                self._head = evens._head
                self._tail = evens._tail
            else:
                self._head = evens._head
                evens._tail.next = odds._head
                self._tail = odds._tail


if __name__ == '__main__':
    # Please, uncomment the code for test each function
    l1 = SList2()
    l2 = SList2()

    for x in [1, 1, 2, 3, 4, 5]:
        l1.add_last(x)
    for x in [-1, 0, 1, 2, 3, 3, 3, 3,  4, 5]:
        l2.add_last(x)

    print('l1:', l1)
    print('l2:', l2)
    print('l1 ^ l2:', l1.intersection(l2))


