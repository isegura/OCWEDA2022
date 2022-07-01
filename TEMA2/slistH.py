# -*- coding: utf-8 -*-


class SNode:
    def __init__(self, e: object, next_node: 'SNode' = None) -> None:
        self.elem = e
        self.next = next_node


class SList:
    """This is the implementation of a singly linked list. We only use 
    a reference to the first node, named head"""
    def __init__(self) -> None:
        """This constructor creates an empty list"""
        self._head = None
        self._size = 0
    
    def __len__(self) -> int:
        """Returns the size of the list"""
        return self._size

    def is_empty(self) -> bool:
        """"Returns True if the list is empty, and False eoc"""
        return len(self) == 0

    def __str__(self) -> str:
        """Returns a string with the elements of the list"""
        result = ''

        node_it = self._head
        while node_it:  # node_it!=None
            result += ', ' + str(node_it.elem)
            node_it = node_it.next
        
        if len(result) > 2:
            result = result[1:]
        
        return result
  
    def add_first(self, e: object):
        """Adds a new element, e, at the beginning of the list"""
        # create the new node
        new_node = SNode(e)
        # the new node must point to the current head
        new_node.next = self._head
        # update the reference of head to point the new node
        self._head = new_node
        # increase the size of the list
        self._size += 1
    
    def add_last(self, e: object) -> None:
        """Adds e to the end of the list"""
        new_node = SNode(e)

        if self.is_empty():
            self._head = new_node
        else:
            # we traverse the list until to reach the last node
            last_node = self._head
            while last_node.next:  # last_node!=None
                last_node = last_node.next
            # now, last_node is the last node
            # the last node must point to the new node
            last_node.next = new_node
        self._size += 1

    def remove_first(self):
        """Removes the first element of the list"""
        result = None
        if self.is_empty():
            print('Error: list is empty!')
        else:  
            # gets the first element, which we will return later
            result = self._head.elem
            # updates head to point to the new head (the next node)
            self._head = self._head.next
            self._size -= 1
        
        return result

    def remove_last(self):
        """removes and returns the last node of the list. 
        If the list is empty, it prints an error and returns None"""
        result = None
        if self.is_empty():
            print('Error: list is empty!')
        elif len(self) == 1:
            result = self.remove_first()
        else:
            prev_last = None
            last_node = self._head
            while last_node.next:
                prev_last = last_node
                last_node = last_node.next
            
            result = last_node.elem
            prev_last.next = None
            self._size -= 1

        return result

    def getAt(self, index: int) -> object:
        """Returns the element at the position index.
        If the index is an invalid position, the function
        will return  None"""
        result = None
        if not isinstance(index, int) or index not in range(0, len(self)):  # range(0, n) -> 0,1,2,...,n-1
            print(index, 'Error getAt: index out of range')
        else:
            node_it = self._head
            i = 0
            while node_it and i < index:  # node_it != None and i < index
                node_it = node_it.next
                i += 1

            # node_it is the node at the position index
            result = node_it.elem

        return result

    def index(self, e: object) -> int:
        """Returns the first position of e into the list.
        If e does not exist in the list, 
        then the function will return -1"""
        node_it = self._head
        index = 0
        while node_it:  # node_it  != None
            if node_it.elem == e:
                return index
            node_it = node_it.next
            index += 1
            
        # print(e,' does not exist!!!')
        return -1 

    def insertAt(self, index: int, e: object) -> None:
        """Inserts a new node containing the element e at the index
        position in the list"""
        
        # first, we must check that index is a right position.
        # Please, Note that index=len()+1 would be a right position
        # to insert a new element

        if not isinstance(index, int) or index not in range(0,len(self)+1):
            print(index, 'Error insertAt: index out of range')
        elif index == 0:
            self.add_first(e)
        elif index == len(self):
            self.add_last(e)
        else:
            # we need to reach the previous node (the node at the index-1 position)
            previous = self._head
            for _ in range(index-1):
                previous = previous.next
                    
            # now, previous is the node with index-1
            # create the new node
            new_node = SNode(e)
            # new_node must point to the node after previous (which is previous.next)
            new_node.next = previous.next
            # previous must point with its next reference to the new node
            previous.next = new_node
            self._size += 1

    def removeAt(self, index: int) -> object:
        """Removes the node at the index position in the list"""
        result=None
        # We must check that index is a right position in the list
        # Remember that the indexes in a list can range from 0 to size-1
        if not isinstance(index,int) or index not in range(len(self)):
            print(index, 'Error removeAt: index out of range')
        elif index == 0:
            result = self.remove_first()
        elif index == len(self)-1:
            result = self.remove_last()
        else:
            # we must reach the node before the node at the index position
            previous = self._head
            for _ in range(index-1):
                previous = previous.next
                
            # previous is the node at index -1 position
            # previous.next is the node at index position
            result = previous.next.elem
            previous.next = previous.next.next
            self._size -= 1
        
        return result


if __name__=='__main__':

    l = SList()
    print("list:", str(l))
    print("len:", len(l))

    for i in range(3):
        l.add_last(i + 1)
        #print("after addLast({}): {}".format(i+1,l))

    for i in range(len(l)):
        print('getAt({})={}'.format(i, l.getAt(i)))

    print(str(l))
    print()
    print("index of {}={}".format(20,l.index(20)))
    print("index of {}={}".format(0,l.index(0)))
    print("index of {}={}".format(5,l.index(5)))
    print("index of {}={}".format(10,l.index(10)))


    #while l.isEmpty()==False:
    #    print("after removeLast():{}, {}".format(l.removeLast(),l))

    l.insertAt(-1, 1)
    l.insertAt(0, 0)
    print(str(l))
    print('after l.insertAt(0,0)', str(l))

    l.insertAt(2, 3)
    print('after l.insertAt(2,3)', str(l))
    print("index of {}={}".format(3,l.index(3)))
    print('len of l', len(l))
    l.insertAt(len(l), 3)
    print('after l.insertAt(12,3)', str(l))
    print("index of {}={}".format(3, l.index(3)))
    l.insertAt(len(l), 100)
    print('after l.insertAt(13,100)', str(l))
    print(l.getAt(len(l)))
    print(l.getAt(len(l)-1))

    print()
    print('testing removeAt', str(l))
    x=0
    print('after l.removeAt({})={}, {}'.format(x,l.removeAt(x), str(l)))

    x=0
    print('after l.removeAt({})={}, {}'.format(x,l.removeAt(x), str(l)))

    x=len(l)-1
    print('after l.removeAt({})={}, {}'.format(x,l.removeAt(x), str(l)))

    x=2
    print('after l.removeAt({})={}, {}'.format(x,l.removeAt(x), str(l)))

    x=5
    print('after l.removeAt({})={}, {}'.format(x,l.removeAt(x), str(l)))

    while not l.is_empty():
        print("after removeLast():{}, {}".format(l.remove_last(), l))
