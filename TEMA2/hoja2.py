# -*- coding: utf-8 -*-
from dlist import DList
from dlist import DNode


class DList2(DList):
    def remove_v1(self, e: object) -> None:
        """removes the first occurrence of e in the list. 
        This solution is based on the functions index and remove"""
        index = self.index(e)
        if index != -1:
            self.removeAt(index)
        else:
            print(e, ' does not exist!!!')

    def remove(self, e: object) -> None:
        """This method removes the first occurrence of the element e in the list.
        This solution does not use any function of the DList class"""
        prev = None
        node_it = self._head
        found = False
        while not found and node_it:  # node_it != None
            if node_it.elem == e:
                # remove node
                if prev is None:
                    # it is the first node
                    self._head = self._head.next
                    if self._head is None:
                        self._tail = None
                    else:
                        self._head.prev = None
                else:
                    # it's not the first node
                    prev.next = node_it.next
                    if node_it.next is None:
                        # node_it was the last node
                        self._tail = prev
                    else:
                        node_it.next.prev = prev

                self._size -= 1
                found = True
            else:
                prev = node_it
                node_it = node_it.next

        if not found:
            print(e, ' does not exist!!!')

    def remove_all_v1(self, e: object) -> None:
        """This method removes all occurrences of e in the list.
        This solution is based on the functions index and removeAt"""
        index = self.index(e)
        if index == -1:
            print(e, ' does not exist!!!')
        while index != -1:
            self.removeAt(index)
            index = self.index(e)

    def remove_all(self, e: object) -> None:
        """This method removes all occurrences of e in the list.
        This solution does not use any function of the SList class"""
        prev = None
        node_it = self._head
        exist = False
        while node_it:  # node_it!=None
            if node_it.elem == e:
                exist = True
                # remove node
                if prev is None:
                    # it is the first node
                    self._head = self._head.next
                    if self._head is None:
                        self._tail = None
                    else:
                        self._head.prev = None
                else:
                    # it's not the first node
                    prev.next = node_it.next
                    if node_it.next is None:
                        # node_it was the last node
                        self._tail = prev
                    else:
                        node_it.next.prev = prev
                self._size -= 1
            else:
                prev = node_it
            node_it = node_it.next

        if not exist:
            print(e, 'does not exist!!!')

    def getAtRev_v1(self, index: int) -> object:
        """The method returns the element at the position index from the end. 
        This solution is based on the function getAt"""
        result = None
        n = len(self)
        if 0 <= index < n:
            result = self.getAt(n - 1 - index)
        else:
            print(index, ' wrong!!!')
        return result

    def getAtRev(self, index: int) -> object:
        """The method returns the element at the position index from the end. 
        This solution does not use any method of DList (only len)"""
        result = None
        n = len(self)
        if 0 <= index < n:
            k = 0
            node_it = self._head
            while index < n - 1 - k:
                node_it = node_it.next
                k += 1

            result = node_it.elem

        else:
            print(index, ' wrong!!!')
        return result

    def getAtEff(self, index: int) -> object:
        """Returns the element at the index position taking advantage of the
        reversing order"""
        if index < 0 or index >= len(self):
            print('error: index out of range')
            return None

        if index <= len(self) // 2:
            print(index, len(self), 'searching from the beginning')
            return self.getAt(index)
        else:
            print(index, 'searching from the tail')
            aux = self._tail
            k = len(self) - 1
            result = None
            while aux:
                if k == index:
                    return aux.elem
                aux = aux.prev
                k -= 1
            return result

    def insertAtEff(self, index: int, elem: object) -> None:
        """It inserts the element e at the index position of the list,
        taking advantage of traversing the list backward"""
        if index < 0 or index > len(self):
            print('Error: index out of range')
            return

        if index == 0:
            self.add_first(elem)
        elif index == len(self):
            self.add_last(elem)
        elif index <= len(self) // 2:
            print(index, 'insert- starting from the head')
            self.insertAt(index, elem)
        else:
            print(index, 'insert- starting from the end')
            k = len(self) - 1
            aux = self._tail
            while k > index:
                aux = aux.prev
                k -= 1
            # aux is the node at the index position
            previous = aux.prev
            new_node = DNode(elem)
            new_node.next = aux
            new_node.prev = previous
            aux.prev = new_node
            previous.next = new_node
            self._size += 1

    def removeAtEff(self, index: int) -> object:
        """It removes the element at the index position of the list,
        taking advantage of traversing the list backward"""
        if index < 0 or index > len(self):
            print('Error: index out of range')
            return None

        if index == 0:
            return self.remove_first()
        elif index == len(self) - 1:
            return self.remove_last()
        elif index <= len(self) // 2:
            print(index, 'remove- starting from the head')
            return self.removeAt(index)
        else:
            # we must reach the node at the index position
            print(index, 'remove- starting from the tail...')
            k = len(self) - 1
            node = self._tail
            while k > index:
                node = node.prev
                k -= 1
            # node is the node that we want to remove
            previous = node.prev
            node_next = node.next

            previous.next = node_next
            node_next.prev = previous

            self._size -= 1
            return node.elem

    def get_middle(self):
        """returns the element at the middle of the list"""
        result = None
        if self.is_empty():
            print('An empty list does not have middle!!!')
        else:
            m = len(self) // 2
            result = self.getAt(m)
        return result

    def count(self, e: object) -> int:
        """ returns the number of occurrences of e in the list"""
        cont = 0
        node_it = self._head
        while node_it:
            if node_it.elem == e:
                cont += 1
            node_it = node_it.next

        return cont

    def is_sorted(self) -> bool:
        """checks if the list is sorted"""
        if len(self) <= 1:
            return True

        node1 = self._head
        node2 = node1.next
        while node2:
            if node1.elem > node2.elem:
                return False
            node1 = node2
            node2 = node2.next

        return True

    def remove_duplicates_sorted(self) -> None:
        """removes the duplicate elements (keeping the first occurrence). The list has to be sorted."""
        if not self.is_sorted():
            print("Error: the list is not sorted")
            return
        if len(self) <= 1:
            # the list does not contain duplicates
            return

        prev = self._head
        node_it = prev.next
        while node_it:
            if prev.elem != node_it.elem:
                prev = node_it
                node_it = node_it.next
            else:
                count = 0
                while node_it and prev.elem == node_it.elem:
                    node_it = node_it.next
                    count += 1
                prev.next = node_it
                if node_it is None:
                    self._tail = prev
                else:
                    node_it.prev = prev
                    node_it = node_it.next
                self._size -= (count-1)
                #


    def remove_duplicates(self) -> None:
        """removes the duplicate elements (keeping the first occurrences). The list can be non-sorted"""
        node_it = self._head
        while node_it:
            e = node_it.elem
            prev = node_it
            node_it2 = node_it.next
            while node_it2:
                if e == node_it2.elem:
                    prev.next = node_it2.next
                    if node_it2.next is None:
                        self._tail = prev
                    else:
                        node_it2.next.prev = prev
                    self._size -= 1
                else:
                    prev = node_it2
                node_it2 = node_it2.next

            node_it = node_it.next

    def swap_pairwise(self):
        """ swap the contiguous elements. If the list has an odd number of elements, the last one 
        is not swapped"""
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
        """This method takes the last element and moves it to the front of the list.
        This method uses other methods of the class"""
        if len(self) > 1:
            x = self.remove_last()
            self.add_first(x)

    def move_last(self) -> None:
        """This method takes the last element and moves it to the front of the list.
        This method does not use any method of the class"""
        if self._size == 0:
            print('list is empty!!')
        else:
            last = self._tail
            next_to_last = self._tail.prev

            last.next = self._head
            self._head.prev = last
            self._head = last
            self._head.prev = None

            next_to_last.next = None
            self._tail = next_to_last

    def intersection(self, other_list: "DList2") -> "DList2":
        """returns a new list containing the elements that are in both lists"""
        output = DList2()
        if self.is_sorted() and other_list.is_sorted():
            node1 = self._head
            node2 = other_list._head

            while node1 and node2:
                if node2.elem < node1.elem:
                    node2 = node2.next
                elif node1.elem < node2.elem:
                    node1 = node1.next
                else:
                    output.add_last(node1.elem)
                    node1 = node1.next
                    node2 = node2.next

        return output

    def segregate_odd_even(self):
        """ the even numbers appear at the beginning of the list, while the odd numbers at the end. The order of the 
        numbers must be kept"""
        if len(self) > 1:
            evens = DList2()
            odds = DList2()
            node = self._head
            while node:
                e = node.elem
                if e % 2 == 0:
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
                odds._head.prev = evens._tail

                self._tail = odds._tail


if __name__ == '__main__':
    import random

    for i in range(20):
        l = DList2()
        l_sorted = DList2()
        aux = []
        for j in range(i):
            x = random.randint(-10, 10)
            aux.append(x)
            l.add_last(x)
        aux = sorted(aux)
        for x in aux:
            l_sorted.add_last(x)
        print(l)
        l.remove_duplicates()
        print(l)
        print(l_sorted)
        l_sorted.remove_duplicates()
        print(l_sorted)

        print()




