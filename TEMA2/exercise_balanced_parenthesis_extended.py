# -*- coding: utf-8 -*-

from stack1 import Stack1

# we create two lists (arrays) to save the opening and closing symbols.
# The opening symbols and their corresponding closing symbols are saved in the same order, so
# each pair of symbols of the same type will have the same index in their corresponding lists.
OPENING = ['(', '{', '[']
CLOSING = [')', '}', ']']


def same_type(a: str, b: str) -> bool:
    """This functions checks if a and b belong to the same type of parenthesis"""
    pos = OPENING.index(a)
    return b == CLOSING[pos]


def same_type1(a: str, b: str) -> bool:
    """This functions checks if a and b belong to the same type of parenthesis.
    Maybe, this functions is easier to understand for you than the previous one"""
    if a == '(' and b == ')':
        return True
    if a == '{' and b == '}':
        return True
    if a == '[' and b == ']':
        return True
    return False


def balanced_ext(expression: str) -> bool:
    """Checks if the parenthesis in the expression, exp, are well-balanced"""
    
    s = Stack1()    # for saving the opening symbols
    
    for c in expression:
        
        if c in OPENING:    # c=='(' or c=='{' or c=='[':
            s.push(c)
        elif c in CLOSING:  # c==')' or c=='}' or c==']'
            if s.is_empty():    
                return False    # there is not any opening symbol for the processed closing symbol 
            else:
                o = s.pop()     # we have to check that both symbols have the same type
                if not same_type(str(o), c):
                    return False    # if they do not have the same type, we must return False.
                
        # else:  # we ignore any other character
        #    pass

    # if we have read all characters, we check if the stack is empty. If it is empty, this means that the
    # expression is well-balanced, therefore, we return True, and False eoc.
    return s.is_empty()


if __name__ == '__main__':
    exp = '()'
    print('is balanced({})={}'.format(exp, balanced_ext(exp)))
    exp = '('
    print('is balanced({})={}'.format(exp, balanced_ext(exp)))
    exp = '([])'
    print('is balanced({})={}'.format(exp, balanced_ext(exp)))
    exp = '([]'
    print('is balanced({})={}'.format(exp, balanced_ext(exp)))
    exp = '([]))'
    print('is balanced({})={}'.format(exp, balanced_ext(exp)))
    exp = '([]{})'
    print('is balanced({})={}'.format(exp, balanced_ext(exp)))
    exp = '([{}]{()})'
    print('is balanced({})={}'.format(exp, balanced_ext(exp)))
    exp = '()(()){([()])}'
    print('is balanced({})={}'.format(exp, balanced_ext(exp)))
    exp = '((()(()){([()])}))'
    print('is balanced({})={}'.format(exp, balanced_ext(exp)))
    exp = ')(()){([()])}'
    print('is balanced({})={}'.format(exp, balanced_ext(exp)))
    exp = '({[]})'
    print('is balanced({})={}'.format(exp, balanced_ext(exp)))
    exp = '({[}])'
    print('is balanced({})={}'.format(exp, balanced_ext(exp)))
    exp = '({[])}'
    print('is balanced({})={}'.format(exp, balanced_ext(exp)))

