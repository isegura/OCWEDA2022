# -*- coding: utf-8 -*-
from dlist import DList


def is_palindrome(input_word: str) -> bool:
    if input_word is None:
        return False

    my_list = DList()
    for c in input_word:
        my_list.add_last(c)

    m = len(my_list)//2
    left = my_list.head
    right = my_list.tail
    i = 0

    while i < m:
        if left.elem != right.elem:
            return False
        left = left.next
        right = right.prev
        i += 1

    return True


if __name__ == '__main__':
    for word in [None, '', 'r', 'ra', 'rad', 'rada', 'radar', 'abaaba', 'a', 'ab','aba','abc','abba','ababa']:
        print('is_palindrome({})={}'.format(word, is_palindrome(word)))
