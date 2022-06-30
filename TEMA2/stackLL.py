# -*- coding: utf-8 -*-
import random


class SNode:
    def __init__(self, e: object, next_node: 'SNode' = None) -> None:
        self.elem = e
        self.next = next_node


class Stack:
    """This is the implementation of a stack based on a singly linked list.
    We only use a reference to the first node, named head. This head references
    to the peak of the stack"""

    def __init__(self) -> None:
        """This constructor creates an empty stack"""
        self._head = None
        # the attribute size is not mandatory, but it helps to simplify the implementation
        self._size = 0

    def __len__(self) -> int:
        """Returns the size of the stack"""
        return self._size

    def is_empty(self) -> bool:
        """"It returns True if the stack is empty, and False eoc"""
        return self._head is None

    def push(self, e: object) -> None:
        """Adds a new element, e, on the stack (before the peak of the stack)"""

        # creates the new node, which must point to _head
        new_node = SNode(e, self._head)
        # updates the reference of head to point the new node
        self._head = new_node
        # increases the size of the list
        self._size += 1

    def pop(self) -> object:
        """Removes and returns the peak (first element) of the stack"""
        result = None
        if self.is_empty():
            print('Error: stack is empty!')
        else:
            # gets the first element, which we will return later
            result = self._head.elem
            # updates head to point to the new head (the next node)
            self._head = self._head.next
            self._size -= 1

        return result

    def top(self):
        """Returns the peak (first element) of the stack"""
        result = None
        if self.is_empty():
            print('Error: stack is empty!')
        else:
            # gets the first element, which we will return later
            result = self._head.elem

        return result

    def __str__(self):
        """Returns a string with the elements of the stack"""
        node_it = self._head
        result = ''
        while node_it:  # nodeIt is not None
            result += ',' + str(node_it.elem)
            node_it = node_it.next

        # removes the first ','
        if len(result) > 0:
            result = result[1:]

        return result


if __name__ == '__main__':
    s = Stack()
    print("stack:{}, len={}".format(str(s), len(s)))

    # we generate 5 random integers
    for i in range(5):
        x = random.randint(0, 100)  # creates a random number 0<=x<=100
        s.push(x)
        print("after push({}):{}, len:{}".format(x, str(s), len(s)))

    print()
    print("top (peak) of the stack:", s.top())  # 1

    print()
    while not s.is_empty():
        print("top (peak) of  {}:{}".format(str(s), s.pop()))
        print("after pop: {}, len={}".format(s, len(s)))

    for i in range(5):
        s.push(i)
        print("after push({}): {}, len={}".format(i, s, len(s)))
