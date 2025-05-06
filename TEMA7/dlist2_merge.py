import random
from dlist import DList

class DList2(DList):



    def split(self):
        """splits the list in a half and returns the two parts as two doubly linked lists
        Complexity O(n)"""

        left = DList2()
        node = self._head
        for i in range(len(self) // 2):
            left.add_last(node.elem)
            node = node.next

        right = DList2()
        for i in range(len(self) // 2, len(self)):
            right.add_last(node.elem)
            node = node.next

        return left, right

    def split2(self) -> ("DList2", "DList2"):
        """splits the list in a half and returns the two parts as two doubly linked lists
        Complexity O(n)"""

        i = 0
        half = self._head
        while i < len(self) // 2:
            half = half.next
            i += 1

        left = DList2()
        if half != self._head:
            left._head = self._head
            left._tail = half.prev
            left._tail.next = None
            left._size = len(self) // 2

        right = DList2()
        right._head = half
        if right._head:
            right._head.prev = None
        right._tail = self._tail
        right._size = len(self) // 2
        if len(self) % 2 != 0:
            right._size += 1

        return left, right

    @staticmethod
    def merge(list1:"DList2", list2:"DList2") -> "DList2":
        new_list = DList2()

        node1 = list1._head
        node2 = list2._head

        while node1 and node2:
            if node1.elem <= node2.elem:
                new_list.add_last(node1.elem)
                node1 = node1.next
            else:
                new_list.add_last(node2.elem)
                node2 = node2.next

        while node1:
            new_list.add_last(node1.elem)
            node1 = node1.next

        while node2:
            new_list.add_last(node2.elem)
            node2 = node2.next

        return new_list


def mergesort(l:DList2) -> "DList2":
    if l == None:
        return None

    if len(l) <= 1:
        return l

    left, right = l.split()

    sorted1 = mergesort(left)
    sorted2 = mergesort(right)

    return DList2.merge(sorted1, sorted2)

if __name__ == '__main__':

    input_list = DList2()
    for x in range(6):
        input_list.add_last(random.randint(0, 25))

    print('Input: ', input_list)

    print("after mergesort:", mergesort(input_list))