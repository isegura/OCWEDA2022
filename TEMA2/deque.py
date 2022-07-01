# -*- coding: utf-8 -*-


class Deque:
    """Implementation of a double queue based on a Python List"""
    def __init__(self) -> None:
        """Create an empty deque"""
        self._items = []
      
    def add_first(self, e: object) -> None:
        """Adds at the beginning of the deque"""
        self._items.insert(0, e)
      
    def add_last(self, e: object) -> None:
        """Adds at the tail of the deque"""
        self._items.append(e)

    def remove_first(self) -> object:
        """Removes and returns the first element in the deque"""
        if self.is_empty():
            print('Error: Deque is empty')
            return None
        # remove first item from the list
        return self._items.pop(0)
    
    def remove_last(self):
        """Removes and returns the element at the tail of the deque"""
        if self.is_empty():
            print('Error: Deque is empty')
            return None
        # remove last item from the list
        return self._items.pop()
    
    def __len__(self) -> int:
        """Returns the number of elements in the deque"""
        return len(self._items)
    
    def is_empty(self) -> bool:
        """Returns True if the deque is empty"""
        return len(self) == 0
    
    def __str__(self):
        """Returns a string with the elementos of the double queue"""
        return str(self._items)


if __name__ == '__main__':
    q = Deque()
    print('isEmpty()', q.is_empty())
    q.add_last(4)
    q.add_last(5)
    q.add_first(3)
    q.add_first(2)
    q.add_first(1)
    print('Content of queue:', str(q))
    print('isEmpty()', q.is_empty())
    print('removeFirst():', q.remove_first())
    print('removeLast():', q.remove_last())
    print('Content of queue:', str(q))
    print('size:', len(q))
