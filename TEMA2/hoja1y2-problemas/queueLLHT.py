# -*- coding: utf-8 -*-
import random


class SNode:
    def __init__(self, e, next_node: 'SNode' = None) -> None:
        self.elem = e
        self.next = next_node


class Queue:
    """This is the implementation of a queue based on a singly linked list. We use 
    a reference to the first node, named _head, and also a reference 
    to the last node, named as _tail.
    Also we keep an attribute, _size to store the number of nodes"""
    def __init__(self) -> None:
        """Creates an empty queue"""
        self._head = None
        self._tail = None
        self._size = 0

    def is_empty(self) -> bool:
        """Checks if the list is empty"""
        return self._head is None
        
    def __len__(self) -> int:
        """Returns the number of elements in the queue"""
        return self._size
 
    def dequeue(self) -> object:
        """Removes and returns the first element of the list"""
        result = None
        if self.is_empty():
            print('Error: queue is empty!')
        else:
            # gets the first element, which we will return later
            result = self._head.elem
            # updates head to point to the new head (the next node)
            self._head = self._head.next
            # if the queue only had one node, tail must become None
            if self.is_empty():
                self._tail = None
            # decreases the size of the queue
            self._size -= 1
            
        return result 

    def first(self) -> object:
        """returns the first element of the queue"""
        result = None
        if self.is_empty():
            print('Error: queue is empty!')
        else:
            # gets the first element, which we will return later
            result = self._head.elem
        return result 

    def last(self) -> object:
        """ returns the last element of the queue"""
        result = None
        if self.is_empty():
            print('Error: queue is empty!')
        else:
            # gets the last element, which we will return later
            result = self._tail.elem

        return result 

    def enqueue(self, e: object) -> None:
        """Adds a new element, e, at the end of the queue"""
        # create the new node
        new_node = SNode(e)
        # the last node must point to the new node
        # now, we must update the tail reference
        if self.is_empty():
            self._head = new_node
        else:
            self._tail.next = new_node
        # update tail to point the new last node
        self._tail = new_node
        # increases the size of the list
        self._size += 1

    def __str__(self):
        """Returns a string with the elements of the queue"""
        result = ''
        node_it = self._head
        
        while node_it:  # node_it!=None
            result += ', ' + str(node_it.elem)
            node_it = node_it.next
        # we must remove the first comma ','
        if len(result) > 0:
            result = result[2:]

        return result


if __name__ == '__main__':

    s = Queue()
    print("Queue:{}, len={}".format(str(s), len(s)))

    # we generate 5 random integers
    for i in range(5):
        # creates a positive integer between 0 <=x<= 100
        x = random.randint(0, 100)
        s.enqueue(x)
        print("after enqueue({}):{}, len:{}".format(x, str(s), len(s)))

    print()
    print("first element of the queue:", s.first())
    print("last element of the queue:", s.last())
    print()

    while not s.is_empty():
        print("first of {}: {}".format(str(s), s.dequeue()))
        print("after dequeue: {}, len={}".format(s, len(s)))
        print()
