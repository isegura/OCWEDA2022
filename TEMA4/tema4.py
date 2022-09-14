# coding=utf-8
import random
import string  # Python module for strings.

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




def sum_list(a: list) -> int:
    """In this solution, it is allowed to update the input list"""
    if a is None or not isinstance(a, list):
        return None
    if len(a) == 0:
        return 0
    else:
        return a.pop(0) + sum_list(a)


def sum_list(a: list) -> list:
    """Returns the sum of the elements in the list.
    In this solution, it is not allowed to update the input list,
    but you can use slice"""
    if a is None or not isinstance(a, list):
        return None

    if len(a) == 0:
        return 0
    else:
        return a[0] + sum_list(a[1:])


def sum_list3(a):
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


def find_max(a):
    """In this solution, it is  allowed to update the input list"""

    if a is None or not isinstance(a, list):
        return None
    if len(a) == 0:
        return None
    elif len(a) == 1:
        return a[0]
    else:
        return max(a.pop(0), find_max(a))


def find_max2(a: list) -> int:
    """In this solution, it is not allowed to update the input list,
    but you can use slicing"""

    if a is None or not isinstance(a, list):
        return None

    if len(a) == 0:
        return None
    elif len(a) == 1:
        return a[0]
    else:
        return max(a[0], find_max2(a[1:]))


def find_max3(a: list) -> int:
    """This function uses an auxiliary recursive function"""
    if a is None or not isinstance(a, list):
        return None
    return _find_max(a, 0)


def _find_max(a: list, index: int) -> int:
    if index >= len(a):
        return None
    elif index == len(a) - 1:
        return a[index]
    else:
        return max(a[index], _find_max(a, index + 1))


def is_sorted1(a: list) -> bool:
    if a is None or not isinstance(a, list):
        return False
    if len(a) <= 1:
        return True
    else:
        return a[0] <= a[1] and is_sorted1(a[1:])


def is_sorted(a: list) -> bool:
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


def is_palindrome(word: str) -> bool:
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


def binary_search1(data, x):
    """returns True if x exist into data, False eoc"""
    if data is None or not isinstance(data, list) or not isinstance(x, int):
        return False

    if not is_sorted(data):
        return False

    if len(data) == 0:
        return False

    m = len(data) // 2
    if data[m] == x:
        return True
    elif x < data[m]:
        # we must search at the first half of the array
        return binary_search(data[0:m], x)
    else:  # x>data[m]
        # we must search from m+1 to the end, always after than m (we already know that data[m]!=x)
        return binary_search(data[m + 1:], x)


def binary_search(a: list, x: int) -> bool:
    if a is None or not isinstance(a, list) or not isinstance(x, int):
        return False

    if not is_sorted(a):
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
    if a is None or not isinstance(a, list) or not isinstance(x, int):
        return -1

    if not is_sorted(a):
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
    if a is None or not isinstance(a, list):
        return
    if len(a) >= 1:
        aux = a.pop(0)
        reverse(a)
        a.append(aux)


def reverse(a: list) -> None:
    """Reverse an array"""
    if a is None or not isinstance(a, list):
        return
    _reverse(a, 0)


def _reverse(a: list, index: int) -> None:
    if index < len(a) // 2:
        a[index], a[len(a) - (index + 1)] = a[len(a) - (index + 1)], a[index]
        _reverse(a, index + 1)


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
    if n < 0 or not isinstance(n, int):
        return None
    if n <= 1:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)


def random_word() -> str:
    """generate random words"""
    result = ''
    length = random.randint(1, 10)  # The random length of the word
    while len(result) != length:  # While loop
        result += random.choice(lowercase_letters)  # Selects a random character on each iteration
    return result  # Returns the word


def random_palindrome(odd: bool = False) -> str:
    """generate a random palindrome word"""
    result = ''
    length = random.randint(1, 5)  # The random length of the word
    if odd:
        letter = random.choice(lowercase_letters)
        result = letter
    while len(result) < 2 * length + 1:  # While loop
        letter = random.choice(lowercase_letters)
        result = letter + result + letter
    return result  # Returns the word


if __name__ == '__main__':

    n = random.randint(-1, 10)
    print("factorial({})={}".format(n, factorial(n)))

    '''
    a = random.randint(-5, 5)
    print("potencia({},{})={}".format(a, n, power(a, n)))

    a = random.randint(-1, 10)
    b = random.randint(-1, 10)
    print("multiSuma({},{})={}".format(a, b, multiplication_by_suma(a, b)))

    n = random.randint(-1, 6)
    if n == -1:
        data = None
        data1 = None
    else:
        data = []
        for i in range(n):
            data.append(random.randint(-10, 10))

        print(data)
        data1 = data.copy()

    print("sumArray1({})={}".format(data, sum_list(data1)))
    print("sumArray2({})={}".format(data, sum_list2(data)))
    print("sumArray3({})={}".format(data, sum_list3(data)))
    print()

    print("findMax1({})={}".format(data, find_max(data1)))
    print("findMax2({})={}".format(data, find_max2(data)))
    print("findMax3({})={}".format(data, findMax3(data)))

    if data != None:
        data1 = sorted(data)
    else:
        data1 = None

    print()
    print("isSorted({})={}".format(data, is_sorted1(data)))
    print("isSorted({})={}".format(data1, is_sorted1(data1)))

    print()
    print("isSorted({})={}".format(data, is_sorted(data)))
    print("isSorted({})={}".format(data1, is_sorted(data1)))

    print()

    print("isPalindrome({})={}".format(None, is_palindrome(None)))
    print("isPalindrome({})={}".format("", is_palindrome("")))
    print("isPalindrome({})={}".format("a", is_palindrome("a")))
    print("isPalindrome({})={}".format("radar", is_palindrome("radar")))
    print("isPalindrome({})={}".format("abba", is_palindrome("abba")))
    word = random_word()
    print("isPalindrome({})={}".format(word, is_palindrome(word)))
    word = random_palindrome()
    print("isPalindrome({})={}".format(word, is_palindrome(word)))
    word = random_palindrome(True)  # odd size of word
    print("isPalindrome({})={}".format(word, is_palindrome(word)))

    x = 5
    print("binarysearch({},{})={}".format(data1, x, binary_search(data1, x)))
    print("binarysearchindex({},{})={}".format(data1, x, binary_search_index(data1, x)))

    if data != None and len(data) > 0:
        data1 = sorted(data)
        x = data1[0]

        print("binarysearch({},{})={}".format(data1, x, binary_search(data1, x)))
        print("binarysearchindex({},{})={}".format(data1, x, binary_search_index(data1, x)))

        x = data[len(data) - 1]
        print("binarysearch({},{})={}".format(data1, x, binary_search(data1, x)))
        print("binarysearchindex({},{})={}".format(data1, x, binary_search_index(data1, x)))

        x = data[len(data) // 2]
        print("binarysearch({},{})={}".format(data1, x, binary_search(data1, x)))
        print("binarysearchindex({},{})={}".format(data1, x, binary_search_index(data1, x)))

    print()
    if data != None:
        data1 = data.copy()
    else:
        data1 = None

    print("before reverse:", data1)
    reverse(data)
    print("after reverse ={}".format(data))
    print()

    n = random.randint(-10000, 10000)
    print("countDigits({})={}".format(n, count_digits(n)))
    print("sumDigits1({})={}".format(n, sum_digits1(n)))
    print("sumDigits({})={}".format(n, sum_digits(n)))

    n = random.randint(-1, 10)
    print("fibo({})={}".format(n, fibo(n)))
    '''
