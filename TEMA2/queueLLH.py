# -*- coding: utf-8 -*-

import random


class SNode:
    def __init__(self, e, next_node: 'SNode' = None) -> None:
        self.elem = e
        self.next = next_node


class Queue:
    """This implementation is based on linked list. It only uses a reference
    to the first element of the queue"""
    def __init__(self):
        self._head = None
        self._size = 0

    def is_empty(self) -> bool:
        """Checks if the list is empty"""
        return self._head is None
        
    def __len__(self) -> int:
        """Returns the number of elements in the queue"""
        return self._size
 
    def dequeue(self) -> object:
        """Removes and returns the first element of the queue"""
        result = None
        if self.is_empty():
            print('Error: queue is empty!')
        else:
            result = self._head.elem
            self._head = self._head.next
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

    def enqueue(self, e: object) -> None:
        """Adds a new element, e, at the end of the queue"""

        new_node = SNode(e)  # create the new node

        if self.is_empty():
            self._head = new_node
        else:
            # the current last node must point to this new node
            last_node = self._head
            while last_node.next:  # last_node.next is not None
                last_node = last_node.next
            # now, last_node must point to new_node
            last_node.next = new_node
         
        self._size += 1

    def last(self) -> object:
        """returns the last element of the queue"""
        result = None
        if self.is_empty():
            print('Error: queue is empty!')
        else:
            # searches the last node
            last_node = self._head
            while last_node.next:  # last_node.next != None
                last_node = last_node.next

            # now, last_node is the last node.
            result = last_node.elem

        return result 

    def __str__(self) -> str:
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


if __name__=='__main__':

    s = Queue()
    print("Queue:{}, len={}".format(str(s), len(s)))

    # we generate 5 random integers
    for i in range(5):
        # creates a positive integer between 0 <=x<= 100
        x = random.randint(0, 100)
        s.enqueue(x)
        print("after enqueue({}):{}, len:{}".format(x, str(s), len(s)))

    print()
    print("first of the queue:", s.first())
    print("last of the queue:", s.last())
    print()

    print()
    while not s.is_empty():
        print("first of  {}:{}".format(str(s), s.dequeue()))
        print("after dequeue: {}, len={}".format(s, len(s)))
        print()
