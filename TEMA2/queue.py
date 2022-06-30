#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Queue:
    """ FIFO Queue implementation using a Python list as storage.
    We add new elements at the tail of the list (enqueue)
    and remove elements from the head of the list (dequeue)."""
  
    def __init__(self) -> None:
        """Create an empty queue"""
        self._items = []

    def __len__(self) -> int:
        """Returns the number of elements in the queue"""
        return len(self._items)

    def is_empty(self) -> bool:
        """Returns True if the queue is empty"""
        return len(self) == 0

    def __str__(self) -> str:
        """Returns a string with the elements of the queue"""
        return str(self._items)

    def enqueue(self, e: object) -> None:
        """Adds the element e to the tail of the queue"""
        self._items.append(e)

    def dequeue(self):
        """Removes and returns the first element in the queue"""
        if self.is_empty():
            print('Error: Queue is empty')
            return None

        # remove first item from the list
        return self._items.pop(0)

    def front(self):
        """Return the first element in the queue"""
        if self.is_empty():
            print('Error: Queue is empty')
            return None

        # returns first element in the list
        return self._items[0]


if __name__ == '__main__':
    q = Queue()
    print('isEmpty()', q.is_empty())
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print('Content of queue:', str(q))
    print('front (first) element:', q.front())
    print('is_empty():',  q.is_empty())
    print('dequeue():', q.dequeue())
    print('Content of queue:', str(q))
    print('front element:', q.front())
    print('size:', len(q))
    q.enqueue(10)
    print('Content of queue:', str(q))
    print('front (first) element:', q.front())
    print('Content of queue:', str(q))
    print('result of dequeue operation:', q.dequeue())
    print('Content of queue:', str(q))
