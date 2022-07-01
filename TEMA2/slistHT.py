# -*- coding: utf-8 -*-
import random


class SNode:
    def __init__(self, e, next_node: 'SNode' = None) -> None:
        self.elem = e
        self.next = next_node


class SList:
    """This is the implementation of a singly linked list. We use 
    a reference to the first node, named _head, and also a reference 
    to the last node, named as _tail. Also, we use an attribute, _size,
    to store the number of nodes"""
    def __init__(self) -> None:
        self._head = None
        self._tail = None
        self._size = 0
    
    def __len__(self) -> int:
        return self._size
    
    def is_empty(self) -> bool:
        """Checks if the list is empty"""
        return len(self) == 0

    def __str__(self) -> str:
        """Returns a string with the elements of the list"""
        # This functions returns the same format used
        # by the Python lists, i.e, [], ['i'], ['a', 'b', 'c', 'd']
        # [1], [3, 4, 5]
        node_it = self._head
        result = '['
        while node_it:
            if type(node_it.elem) == int:
                result += str(node_it.elem) + ", "
            else:
                result += "'" + str(node_it.elem) + "', "
            node_it = node_it.next
        
        if len(result) > 1:
            result = result[:-2]

        result += ']'
        return result

    def add_first(self, e: object) -> None:
        """Adds a new element, e, at the beginning of the list"""
        # create the new node
        new_node = SNode(e)
        if self.is_empty():
            self._tail = new_node
        else:
            new_node.next = self._head

        # update the reference of head to point the new node
        self._head = new_node
        # increase the size of the list
        self._size += 1

    def add_last(self, e: object) -> None:
        """Adds a new element, e, at the end of the list"""
        # create the new node
        new_node = SNode(e)
        # the last node must point to the new node
        # also, we must update the tail reference
        if self.is_empty():
            self._head = new_node
        else:
            self._tail.next = new_node
        
        self._tail = new_node
        # increase the size of the list
        self._size += 1
    
    def remove_first(self) -> object:
        """Removes and returns the first element of the list"""
        result = None
        if self.is_empty():
            print('Error: list is empty!')
        else:
            # gets the first element, which we will return later
            result = self._head.elem
            # updates head to point to the new head (the next node)
            self._head = self._head.next
            # if the list only has one node, tail must be None
            if self._head is None:
                self._tail = None
            self._size -= 1
        
        return result

    def remove_last(self) -> object:
        """Removes and returns the last element of the list"""
        result = None
        if self.is_empty():
            print('Error: list is empty!')
        elif len(self) == 1:
            result = self.remove_first()
        else:
            result = self._tail.elem

            prev_last = self._head
            while prev_last.next != self._tail:
                prev_last = prev_last.next
            
            prev_last.next = None
            self._tail = prev_last
            self._size -= 1
        
        return result

    def getAt(self, index: int) -> object:
        """Returns the element at the position index.
        If the index is an invalid position, the function
        will return None"""
        result = None
        if not isinstance(index, int) or index not in range(0, len(self)):
            print(index, 'Error getAt: index out of range')
        else:
            node_it = self._head
            k = 0
            while node_it and k < index:
                node_it = node_it.next
                k += 1

            # node_it is at the position index
            result = node_it.elem

        return result

    def index(self, e: object) -> int:
        """Returns the first position of e into the list.
        If e does not exist in the list, then the function will return -1"""

        node_it = self._head
        index = 0
        while node_it:
            if node_it.elem == e:
                return index
            node_it = node_it.next
            index += 1
            
        # print(e,' does not exist!!!')
        return -1 

    def insertAt(self, index: int, e: object) -> None:
        """Inserts a new node containing the element e at the index
        position in the list"""
        if not isinstance(index, int) or index not in range(0, len(self)+1):
            print(index, 'Error insertAt: index out of range')
        elif index == 0:
            self.add_first(e)
        elif index == len(self):
            self.add_last(e)
        else:
            node_it = self._head
            for _ in range(index-1):
                node_it = node_it.next
            
            # node_it is at index-1
            new_node = SNode(e)
            new_node.next = node_it.next
            # node_it must point with its next reference to the new node
            node_it.next = new_node
            self._size += 1
      
    def removeAt(self, index: int) -> object:
        """Removes and returns the element at the index position in the list"""
        result = None
        if not isinstance(index, int) or index not in range(len(self)):
            print(index, 'Error removeAt: index out of range')
        elif index == 0:
            result = self.remove_first()
        elif index == len(self)-1:
            result = self.remove_last()
        else:
            # we must reach the node before the node at the index position
            node_it = self._head
            for _ in range(index-1):
                node_it = node_it.next
                
            # node_it is the node at index -1 position
            # node_it.next is the node at index position
            aux_node = node_it.next  # node to remove
            result = aux_node.elem
            node_it.next = aux_node.next
            
            self._size -= 1
        
        return result


if __name__ == '__main__':
    mylist = SList()
    for i in range(5):
        mylist.add_last(random.randint(-5, 5))

    print('Content of l:', mylist)
    print('len(l):', len(mylist))
    print()

    while not mylist.is_empty():
        print('after removeFirst()={}, l={}, len={}'.format(mylist.remove_first(), mylist, len(mylist)))

    for _ in range(3):
        x = random.randint(-5, 5)
        mylist.add_first(x)
        print('after addFirst({}), l={}, len={}'.format(x, mylist, len(mylist)))

    print('Content of l:', mylist)
    print('len(l):', len(mylist))
    print()

    while not mylist.is_empty():
        print('after removeLast()={}, l={}, len={}'.format(mylist.remove_last(), mylist, len(mylist)))
    print('---------------------')

    for _ in range(3):
        x = random.randint(-5, 5)
        mylist.add_first(x)
        mylist.add_last(x)

    print('Content of l:', mylist)
    print('len(l):', len(mylist))
    print()

    for i in range(len(mylist)):
        print(' getAt({})={}'.format(i, mylist.getAt(i)))
    print()

    for _ in range(3):
        x = random.randint(-5, 5)
        print(' index({})={}'.format(x, mylist.index(x)))
    print()

    print('Content of l:', mylist)
    print('len(l):', len(mylist))
    print()

    x = 666
    mylist.insertAt(0, x)
    print(' insertAt(0,{}), l={}, len={}'.format(x, mylist, len(mylist)))
    mylist.insertAt(len(mylist), x)
    print(' insertAt(len(l),{}), l={}, len={}'.format(x, mylist, len(mylist)))
    mylist.insertAt(len(mylist) // 2, x)
    print(' insertAt(len(l)//2,{}), l={}, len={}'.format(x, mylist, len(mylist)))
    print()
    print()

    print(' removeAt(0)={}, l={}, len={}'.format(mylist.removeAt(0), mylist, len(mylist)))
    print(' removeAt(len(l)-1)={}, l={}, len={}'.format(mylist.removeAt(len(mylist) - 1), mylist, len(mylist)))
    print(' removeAt(len(l)//2+1)={}, l={}, len={}'.format(mylist.removeAt(len(mylist) // 2 + 1), mylist, len(mylist)))
