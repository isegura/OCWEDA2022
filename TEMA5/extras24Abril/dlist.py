# -*- coding: utf-8 -*-


class DNode:
    def __init__(self, e: object, prev_node: 'DNode' = None, next_node: 'DNode' = None):
        self.elem = e
        self.next = next_node
        self.prev = prev_node
    
    
class DList:
    def __init__(self) -> None:
        """creates an empty list"""
        self._head = None
        self._tail = None
        self._size = 0
    
    def __len__(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        """Checks if the list is empty"""
        return len(self) == 0
  
    def __str__(self):
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
                result += "'"+str(node_it.elem) + "', "
            node_it = node_it.next
        
        if len(result) > 1:
            result = result[:-2]

        result += ']'
        return result

    def add_first(self, e: object) -> None:
        """Adds a new element, e, at the beginning of the list"""
        # create the new node
        new_node = DNode(e)
        # the new node must point to the current head
        if self.is_empty():
            self._tail = new_node
        else:
            self._head.prev = new_node
        
        # update the reference of head to point the new node
        self._head = new_node
        # increase the size of the list
        self._size += 1

    def add_last(self, e: object) -> None:
        """Adds a new element, e, at the end of the list"""
        # creates the new node
        new_node = DNode(e)
        
        if self.is_empty():
            self._head = new_node
        else:
            new_node.prev = self._tail
            self._tail.next = new_node
        
        # update the reference of head to point the new node
        self._tail = new_node
        # increase the size of the list
        self._size += 1

    def remove_first(self):
        """Returns and removes the first element of the list"""
        result = None
        if self.is_empty():
            print("Error: list is empty")
        else:
            result = self._head.elem
            
            self._head = self._head.next
            if self._head is None:
                self._tail = None
            else:
                self._head.prev = None

            self._size -= 1

        return result
    
    def remove_last(self):
        """Returns and removes the last element of the list"""
        result = None

        if self.is_empty():
            print("Error: list is empty")
        else:
            result = self._tail.elem
            self._tail = self._tail.prev
            if self._tail is None:
                self._head = None
            else:
                self._tail.next = None

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
            for _ in range(index):
                node_it = node_it.next

            # node_it is the node at the position index
            result = node_it.elem

        return result

    def index(self, e: object) -> int:
        """Returns the first position of e into the list.
        If e does not exist in the list, then it returns -1"""
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
        if not isinstance(index, int) or index not in range(len(self)+1):
            print('Error: index out of range')
        elif index == 0:
            self.add_first(e)
        elif index == len(self):
            self.add_last(e)
        else:
            node_it = self._head
            for _ in range(index):
                node_it = node_it.next
            # node_it is the node at the index

            prev_node = node_it.prev
        
            new_node = DNode(e)
            # we have to insert the new node before node_it
            new_node.next = node_it
            new_node.prev = prev_node
            prev_node.next = new_node
            node_it.prev = new_node
            self._size += 1
      
    def removeAt(self, index: int) -> object:
        """Removes and returns the element at the index position in the list"""
        # We must check that index is a right position in the list
        # Remember that the indexes in a list can range from 0 to size-1
        result = None
        if not isinstance(index, int) or index not in range(len(self)):
            print(index, 'Error removeAt: index out of range')
        elif index == 0:
            result = self.remove_first()
        elif index == len(self)-1:
            result = self.remove_last()
        else:
            node_it = self._head
            for _ in range(index):
                node_it = node_it.next

            # node_it is the node to be removed
            result = node_it.elem
            prev_node = node_it.prev
            next_node = node_it.next
            
            prev_node.next = next_node
            next_node.prev = prev_node
            self._size -= 1
        
        return result

    @property
    def head(self):
        return self._head

    @property
    def tail(self):
        return self._tail

    def __eq__(self, other: 'DList') -> bool:
        """returns True if self and other have the same elements,
        eoc False"""
        if other is None or len(self) != len(other):
            return False

        node = self._head
        node_o = other._head  # node to traverse the list other
        while node:
            if node.elem != node_o.elem:
                return False
            node = node.next
            node_o = node_o.next
        return True
