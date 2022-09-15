# coding=utf-8
import math
import random
import string  # Python module for strings.
import sys

lowercase_letters = string.ascii_lowercase  # A constant containing lowercase letters


def factorial(n: int) -> int:
    """n!=n*(n-1)*...*2*1"""
    if n < 0 or not isinstance(n, int):
        return None
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def multiplication_by_suma(a: int, b: int) -> int:
    """returns a*b, a, b>=0"""
    if a < 0 or not isinstance(a, int):
        return None
    if b < 0 or not isinstance(b, int):
        return None
    if b == 0:
        return 0
    else:
        return a + multiplication_by_suma(a, b - 1)


def sum_n(n: int) -> int:
    """given a positive integer, returns the sum of
    the numbers from 1 to n"""

    if n <= 0 or not isinstance(n, int):
        return None

    if n == 1:
        return 1
    else:
        return n + sum_n(n - 1)


def power(a: int, n: int) -> int:
    """a^n, n >=0"""
    if not isinstance(a, int) or n < 0 or not isinstance(n, int):
        return None

    if n == 0:
        return 1
    else:
        return a * power(a, n - 1)


def gcd(a: int, b: int) -> int:
    """returns the greatest common divisor of a and b"""
    if not isinstance(a, int) or a < 0 or not isinstance(a, int) or b < 0:
        return None # a, b must be >=0
    # suppose a > b, if a < b, we change
    if a < b:
        a, b = b, a
    return _gcd(a,b)


def _gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def sum_list0(a: list) -> list:
    """Returns the sum of the elements in the list.
    In this solution, it is not allowed to update the input list,
    but you can use slice"""
    if a is None or not isinstance(a, list):
        return None

    if len(a) == 0:
        return 0
    else:
        return a[0] + sum_list0(a[1:])


def sum_list1(a: list) -> int:
    """In this solution, it is allowed to update the input list"""
    if a is None or not isinstance(a, list):
        return None

    if len(a) == 0:
        return 0
    else:
        return a.pop(0) + sum_list1(a)


def sum_list2(a):
    """returns the sum of the elements in a.
    It does not modify the list.
    It does not use slicing"""
    if a is None or not isinstance(a, list):
        return None
    return _sum_list(a, 0)


def _sum_list(a: list, index: int) -> int:
    """auxiliary function that """
    if index >= len(a):
        return None
    elif index == len(a) - 1:
        return a[index]
    else:
        return a[index] + _sum_list(a, index + 1)



def find_max1(a: list) -> int:
    """In this solution, it is not allowed to update the input list,
    but you can use slicing"""

    if a is None or not isinstance(a, list) or len(a) == 0:
        return None

    if len(a) == 1:
        return a[0]
    else:
        return max(a[0], find_max1(a[1:]))


def find_max2(a):
    """In this solution, it is  allowed to update the input list"""

    if a is None or not isinstance(a, list) or len(a) == 0:
        return None

    if len(a) == 1:
        return a[0]
    else:
        return max(a.pop(0), find_max2(a))


def find_max3(a: list) -> int:
    """This function uses an auxiliary recursive function"""
    if a is None or not isinstance(a, list) or len(a) == 0:
        return None
    return _find_max(a, 0)


def _find_max(a: list, index: int) -> int:
    if index == len(a) - 1:
        return a[index]
    else:
        return max(a[index], _find_max(a, index + 1))


def is_sorted1(a: list) -> bool:
    """checks if a is sorted. It uses slicing"""
    if a is None or not isinstance(a, list):
        return False
    if len(a) <= 1:
        return True
    else:
        return a[0] <= a[1] and is_sorted1(a[1:])


def is_sorted2(a: list) -> bool:
    """ checks if a is sorted. It does not use slicing"""
    if a is None or not isinstance(a, list):
        return False
    return _is_sorted(a, 0)


def _is_sorted(a: list, index: int) -> bool:
    if index >= len(a) - 1:
        return True
    else:
        return a[index] <= a[index + 1] and _is_sorted(a, index + 1)


def is_palindrome1(word: str) -> bool:
    """recursive function that checks if words is palindrome or not.
    In this version, we can use slicing"""
    if word is None or not isinstance(word, str):
        # we consider that None is not palindrome
        return False

    if len(word) <= 1:
        return True
    else:
        return word[0] == word[len(word) - 1] and is_palindrome1(word[1:-1])


def is_palindrome2(word: str) -> bool:
    """recursive function that checks if words is palindrome or not.
    YOu cannot use slicing"""
    if word is None or not isinstance(word, str):
        return False
    return _is_palindrome(word, 0)


def _is_palindrome(word: str, index: int) -> bool:
    if index >= len(word) // 2:
        return True
    else:
        return word[index] == word[len(word) - (index + 1)] and _is_palindrome(word, index + 1)


def binary_search1(a: list, x: int) -> bool:
    """returns True if x exist into data, False eoc. It uses slicing"""
    if a is None or not isinstance(a, list) or not isinstance(x, int):
        return False

    if not is_sorted2(a):
        return False

    if len(a) == 0:
        return False

    m = len(a) // 2
    if a[m] == x:
        return True
    elif x < a[m]:
        # we must search at the first half of the array
        return binary_search2(a[0:m], x)
    else:  # x>data[m]
        # we must search from m+1 to the end, always after than m (we already know that data[m]!=x)
        return binary_search2(a[m + 1:], x)


def binary_search2(a: list, x: int) -> bool:
    """returns the index of x in a (a is sorted).
    It does not use slicing"""
    if a is None or not isinstance(a, list) or not isinstance(x, int):
        return False

    if not is_sorted2(a):
        return False

    return _binary_search(a, x, 0, len(a) - 1)


def _binary_search(a: list, x: int, start: int, end: int) -> bool:
    """returns True if x exist into data, False eoc.
    O(log n), O"""
    if start <= end:
        m = (start + end) // 2
        if x == a[m]:
            return True
        elif x < a[m]:
            return _binary_search(a, x, start, m - 1)
        else:
            return _binary_search(a, x, m + 1, end)
    else:
        return False


def binary_search_index(a: list, x: int) -> int:
    """returns the index of x in a. a must be sorted.
    It does not use slicing"""
    if a is None or not isinstance(a, list) or not isinstance(x, int):
        return -1

    if not is_sorted2(a):
        return -1

    return _binary_search_index(a, x, 0, len(a) - 1)


def _binary_search_index(a: list, x: int, start: int, end: int) -> int:
    """returns True if x exist into data, False eoc.
    O(log n), O"""

    if start <= end:
        m = (start + end) // 2
        if x == a[m]:
            return m
        elif x < a[m]:
            return _binary_search_index(a, x, start, m - 1)
        else:
            return _binary_search_index(a, x, m + 1, end)
    else:
        return -1


def reverse1(a: list) -> None:
    """ The list a is modified by its reverse list.
    The function does not return anything.
    It is allowed to update the list
    """
    if a is None or not isinstance(a, list):
        return
    if len(a) >= 1:
        aux = a.pop(0)
        reverse1(a)
        a.append(aux)

def reverse2(a: list) -> None:
    """ The list a is modified by its reverse list.
    The function does not return anything.
    It is not allowed to update the list
    """
    if a is None or not isinstance(a, list):
        return
    _reverse(a, 0)


def _reverse(a: list, index: int) -> None:
    if index < len(a) // 2:
        a[index], a[len(a) - (index + 1)] = a[len(a) - (index + 1)], a[index]
        _reverse(a, index + 1)


def binary_sum(a: list) -> int:
    """returns the sum of the elements in a by using
    binary recursion"""
    if a is None or not isinstance(a, list):
        return None
    if len(a) == 0:
        return 0
    else:
        m = len(a) // 2
        return binary_sum(a[0:m]) + a[m] + binary_sum(a[m+1:])


def count_digits1(n: int) -> int:
    """returns the number of digits that form n.
    This function only works for positive numbers"""
    if not isinstance(n, int) or n < 0:
        return 0

    if n < 10:
        return 1
    else:
        return 1 + count_digits1(n // 10)


def count_digits(n: int) -> int:
    """returns the number of digits that form n.
    this function work for any integer"""
    if not isinstance(n, int):
        return 0
    if 0 <= abs(n) < 10:
        return 1
    else:
        return 1 + count_digits(abs(n // 10))


def sum_digits1(n: int) -> int:
    """returns the sum of digits that form n.
    This function only works for positive numbers"""
    if not isinstance(n, int) or n < 0:
        return 0

    if n < 10:
        return n
    else:
        return n % 10 + sum_digits1(n // 10)


def sum_digits(n: int) -> int:
    """returns the sum of digits that form n.
    this function work for any integer"""
    if not isinstance(n, int):
        return 0
    if 0 <= abs(n) < 10:
        return abs(n)
    else:
        return abs(n) % 10 + sum_digits(abs(n) // 10)


def fibo(n: int) -> int:
    """This functions allows to obtain the Fibonaci sequence"""
    if n < 0 or not isinstance(n, int):
        return None

    if n <= 1:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)


def fibo2(n: int) -> (int, int):
    """This implementation is more efficient than the previous one.
    It returns a pair (x, y), where x is the Fibonacci number for n-1, and y for n"""
    if n < 0 or not isinstance(n, int):
        return None

    if n <= 1:
        # returns the fibonacci for 0 and for 1
        return 0, n
    else:
        # a is the fibonacci number for n-2, b is the Fibonacci number for n-1
        a, b = fibo2(n-1)
        # Now, we have to return the Fibonacci number for n-1, and the Fibonacci number for n,
        # which is a + b
        return b, a + b


if __name__ == '__main__':

    '''
    # Test factorial
    n = random.randint(0, 10)
    fact = 1
    for i in range(1,n+1):
        fact *= i
    result = factorial(n)
    print("factorial({})={}".format(n, result))
    assert(fact == result)
    '''

    '''
    # Test multiplication_by_sum
    x = random.randint(0, 10)
    y = random.randint(0, 5)
    result = multiplication_by_suma(x, y)
    print('multiplication_by_suma({},{}) = {}'.format(x, y, result))
    assert(x*y == result)
    '''

    '''
    # Test sum_n
    n = random.randint(0, 10)
    sum_digits = 0
    for i in range(n+1):
        sum_digits += i
    result = sum_n(n)
    print("sum_n({})={}".format(n, result))
    assert(result == sum_digits)
    '''

    '''
    # Test power
    a = random.randint(0, 5)
    n = random.randint(0, 10)
    result = power(a, n)
    print("power({},{})={}".format(a, n, result))
    assert(result == math.pow(a, n))
    '''

    '''
    # Test gcd
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    # a, b = 250, 6250
    result = gcd(a, b)
    print('gcd({},{}) = {}'.format(a, b, result))
    assert(result == math.gcd(a, b))
    '''

    '''
    # Test sum_List
    n = random.randint(0, 7)
    original_list = []
    for _ in range(n):
        original_list.append(random.randint(-10, 10))

    aux_list = original_list.copy()
    result_sum = sum(original_list)
    # Please, uncomment just one of the following calls
    # result = sum_list0(aux_list) # by using slicing
    # result = sum_list1(aux_list) # by allowing the list
    result = sum_list2(aux_list) # no slicing, no updating the list; by using indexes
    print("sum_list({}) = {}".format(original_list, result))
    assert(result == result_sum)
    '''

    '''
    # Test find_max
    n = random.randint(0, 7)
    original_list = []
    for _ in range(n):
        original_list.append(random.randint(-10, 10))

    aux_list = original_list.copy()
    if len(aux_list) == 0:
        result_max = None
    else:
        result_max = max(aux_list)
    # Please, uncomment just one of the following calls
    # result = find_max1(aux_list) # by using slicing
    # result = find_max2(aux_list) # by allowing the list
    result = find_max3(aux_list) # no slicing, no updating the list; by using indexes
    print("find_max({}) = {}".format(original_list, result))
    assert(result == result_max)
    '''

    '''
    # Test is_sorted
    n = random.randint(0, 7)
    original_list = []
    for _ in range(n):
        original_list.append(random.randint(-10, 10))

    aux_list = original_list.copy()
    # Please, uncomment just one of the following calls
    # result = is_sorted1(aux_list) # by using slicing
    result = is_sorted2(aux_list) # not slicing
    print("is_sorted({}) = {}".format(original_list, result))
    aux_list.sort()
    assert(result == (original_list == aux_list) )
    '''

    '''
    # Test is_palindrome
    for word in [None, '', 'a', 'ab', 'aba','abb', 'abba', 'baab', 'babb', 'abcba', 'aabbaa']:
        result = is_palindrome1(word)  # by slicing
        # result = is_palindrome2(word)    # no slicing
        print("is_palindrome({}) = {}".format(word, result))
        if word is not None: # we can check it for all cases except None
            result_reverse = (word == ''.join(reversed(word)))
            assert(result == result_reverse)
    '''

    '''
    # Test binary_search
    n = random.randint(0, 15)
    original_list = []
    for _ in range(n):
        original_list.append(random.randint(0, 10))

    # we have to sort it
    original_list.sort()
    aux_list = original_list.copy()
    x = random.randint(0, 10)
    # Please, uncomment just one of the following calls
    # result = binary_search1(aux_list, x) # by using slicing
    result = binary_search2(aux_list, x) # not slicing
    print("binary_search({}, {}) = {}".format(original_list, x, result))
    assert(result == (x in original_list) )
    '''

    '''
    # Test binary_search_index
    n = random.randint(0, 15)
    original_list = []
    for _ in range(n):
        original_list.append(random.randint(0, 10))

    # we have to sort it
    original_list.sort()
    # To avoid problems with duplicates elements, we remove them. 
    original_list = list(set(original_list))
    
    x = random.randint(0, 10)
    result = binary_search_index(original_list, x) # not slicing
    print("binary_search_index({}, {}) = {}".format(original_list, x, result))
    if x in original_list:
        assert(result == (original_list.index(x)) )
    else:
        assert(result == -1)
    '''

    '''
    # Test reverse
    n = random.randint(0, 7)
    original_list = []
    for _ in range(n):
        original_list.append(random.randint(-10, 10))

    result = original_list.copy()
    # Please, uncomment just one of the following calls
    # reverse1(result) # by using slicing
    reverse2(result) # no slicing
    print("reverse({}) = {}".format(original_list, result))
    result.reverse()
    assert(original_list == result)
    '''

    '''
    # Test binary_sum
    n = random.randint(0, 7)
    input_list = []
    for _ in range(n):
        input_list.append(random.randint(-10, 10))
    result = binary_sum(input_list) # no slicing
    print("binary_sum({}) = {}".format(input_list, result))

    assert(result == sum(input_list))
    '''

    '''
    # Test count_digits and sum_digits
    n = random.randint(-10000, 10000)
    # n = random.randint(-sys.maxsize, sys.maxsize)
    result = count_digits(n)
    print("count_digits({}) = {}".format(n, result))
    assert ( result == len(str(abs(n))))

    result = sum_digits(n)
    print("sum_digits({}) = {}".format(n, result))
    n = abs(n)
    digit_map = list(map(int, str(abs(n))))
    assert ( result == sum(digit_map) )
    '''
