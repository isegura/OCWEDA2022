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
    
    def remove(self, e: object) -> None:
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
            result=self.getAt(m)
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

    def count(self,e: object) -> int:
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
                i = 1
                while i < len(self):
                    if self.getAt(i-1) == self.getAt(i):
                        self.removeAt(i)
                    else:
                        i += 1
        else:
            print('list is not sorted!!!')

    def remove_duplicates_sorted(self):
        """This method removes the duplicate elements in a sorted list.
        The method does not any method of the class SList"""
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
            node_it=self._head
            while node_it:
                prev=node_it
                nodeIt2=node_it.next

                e=node_it.elem
                while nodeIt2:
                    if e==nodeIt2.elem:
                        prev.next=nodeIt2.next
                        if nodeIt2.next==None:
                            self._tail=prev
                        self._size-=1
                    else:
                        prev=nodeIt2

                    nodeIt2=nodeIt2.next

                node_it=node_it.next

if __name__ == '__main__':
    # Please, uncomment the code for test each function
    l1 = SList2()
    for i in range(15):
        l1.add_last(random.randint(0, 10))
    print("before remove(0)", l1)
    # Please, uncomment just one of the two calls
    # l1.remove(0)
    l1.remove_byindex(0)
    print("after remove(0)", l1)
    print()
    
    print()
    print("before remove_all(1)", l1)
    # Please, uncomment just one of the two calls
    # l1.remove_all(1)
    l1.remove_all_byindex(1)
    print("before remove_all(1)", l1)
    print()

    # for i in range(len(l1)):
    #    print("l.getAtRev({})={}".format(i, l1.getAtRev(i)))
    #    print("l.getAtRev({})={}".format(i, l1.getAtRev_v1(i)))

    print("before middle:", l1)
    print("middle: ", l1.get_middle(), "getAt(len/2):", l1.getAt(len(l1)//2))
    print("middle: ", l1.get_middle_v1(), "getAt(len/2):", l1.getAt(len(l1)//2))

    assert(l1.get_middle() == l1.getAt(len(l1)//2) )
    assert(l1.get_middle_v1() == l1.getAt(len(l1)//2) )

    l2 = SList2()
    print("middle: ", l2.get_middle())
    assert(l2.get_middle() is None)
    assert(l2.get_middle_v1() is None)

    print("before count: ", l1)
    for i in range(len(l1)):
        print("count({})={}".format(i, l1.count(i)))

    print("{}.is_sorted() = {} ".format(l1, l1.is_sorted()))
    print("{}.is_sorted() = {} ".format(l2, l2.is_sorted()))
    l2.add_last(3)
    print("{}.is_sorted() = {} ".format(l2, l2.is_sorted()))
    l2.add_last(5)
    print("{}.is_sorted() = {} ".format(l2, l2.is_sorted()))
    l2.add_last(8)
    print("{}.is_sorted() = {} ".format(l2, l2.is_sorted()))
    l2.add_last(8)
    print("{}.is_sorted() = {} ".format(l2, l2.is_sorted()))
    l2.add_last(7)
    print("{}.is_sorted() = {} ".format(l2, l2.is_sorted()))

    print("remove duplicates in : ", l2)
    l2.remove_duplicates_sorted_v1()
    print(l2)
    l2.remove(7)
    l2.add_last(9)
    l2.add_last(10)
    l2.add_last(10)
    l2.add_last(10)
    l2.add_last(11)
    l2.add_last(13)
    # Please, uncomment just one call
    # l2.remove_duplicates_sorted_v1()
    l2.remove_duplicates_sorted()
    print("remove duplicates in : ", l2)

