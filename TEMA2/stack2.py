#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Stack2:
    """LIFO Stack implementation using a Python list as storage.
    The top of the stack is stored at the beginning of the list."""

    def __init__(self) -> None:
        """Create an empty stack. We will use an array (Python list)
        to save the elements of the stack"""
        self._items = []

    def __len__(self) -> int:
        """Returns the number of elements in the stack"""
        return len(self._items)

    def is_empty(self) -> bool:
        """Returns True if the stack is empty, False eoc"""
        return len(self._items) == 0

    def __str__(self) -> str:
        """Returns a string with the elements of the stack"""
        return str(self._items)

    def push(self, e: object) -> None:
        """Adds the element e to the top of the stack"""
        self._items.insert(0, e)

    def pop(self) -> object:
        """Removes and returns the element from the top of the stack"""
        if self.is_empty():
            print('Error: Stack is empty')
            return None

        return self._items.pop(0)  # removes the first item from the list
  
    def top(self) -> object:
        """Returns the element from the top of the stack"""
        if self.is_empty():
            print('Error: Stack is empty')
            return None

        # returns last element in the list
        return self._items[0]


if __name__ == '__main__':
    print('testing Stack2')
    s = Stack2()
    print('isEmpty()', s.is_empty())
    s.push('W')
    s.push('O')
    print('top element', s.top())
    print('isEmpty()', s.is_empty())
    s.push('R')
    s.push('D')
    print('Content of stack', str(s))
    print('pop:', s.pop())
    print('Content of stack', str(s))
    print('top element:', s.top())
