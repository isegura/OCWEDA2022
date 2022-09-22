from random import randint
from random import randrange


def find_max(list_numbers: int) -> int:
    """returns the greatest element in list_number by using divide and conquer"""

    if list_numbers is None or len(list_numbers) == 0:
        return None

    # base case
    if len(list_numbers) == 1:
        return list_numbers[0]

    # Recursive case
    # divide
    m = len(list_numbers) // 2
    part1 = list_numbers[0:m]
    part2 = list_numbers[m:]

    # conquer
    mayor1 = find_max(part1)  # el mayor del array part1
    mayor2 = find_max(part2)  # el mayor del array part2

    # combine
    return max(mayor1, mayor2)


def find_max2(list_numbers: list) -> int:
    """This function also obtain the maximum number in a list of numbers by
    using divide and conquer. """
    if list_numbers is None or len(list_numbers) == 0:
        return None

    return _find_max(list_numbers, 0, len(list_numbers) - 1)


def _find_max(list_numbers: list, start: int, end: int) -> int:
    if start == end:
        return list_numbers[start]
    else:
        mid = (start + end) // 2
        max1 = _find_max(list_numbers, start, mid)
        max2 = _find_max(list_numbers, mid + 1, end)
        return max(max1, max2)


def find_min_max(list_numbers: list) -> (int, int):
    """Returns a tuple with the minimum and maximum numbers in
     list_numbers, by using divide and conquer"""

    if list_numbers is None or len(list_numbers) == 0:
        return None, None

    # base case
    if len(list_numbers) == 1:
        return list_numbers[0], list_numbers[0]

    # Recursive case
    # divide
    m = len(list_numbers) // 2
    part1 = list_numbers[0:m]
    part2 = list_numbers[m:]

    # conquer
    min1, max1 = find_min_max(part1)
    min2, max2 = find_min_max(part2)
    # combine
    return min(min1, min2), max(max1, max2)


def find_lowest_even_odd(list_numbers):
    """returns a tuple with the lowest even and odd numbers in list_numbers.
    The solution must use divide and conquer"""

    if list_numbers is None or len(list_numbers) == 0:
        return None, None

    if len(list_numbers) == 1:
        if list_numbers[0] % 2 == 0:
            return list_numbers[0], None
        else:
            return None, list_numbers[0]

    # divide
    m = len(list_numbers) // 2
    part1 = list_numbers[0:m]
    part2 = list_numbers[m:]

    min_even1, min_odd1 = find_lowest_even_odd(part1)
    min_even2, min_odd2 = find_lowest_even_odd(part2)

    if min_even1 is None:
        min_even = min_even2
    elif min_even2 is None:
        min_even = min_even1
    else:  # both are not None
        min_even = min(min_even1, min_even2)

    if min_odd1 is None:
        min_odd = min_odd2
    elif min_odd2 is None:
        min_odd = min_odd1
    else:  # both are not None
        min_odd = min(min_odd1, min_odd2)

    return min_even, min_odd

def sum_list(list_numbers: list) -> int:
    """returns the sum of numbers in list_numbers. The
    solution must use divide and conquer"""
    if list_numbers is None or len(list_numbers) == 0:
        return 0

    # base case
    if len(list_numbers) == 1:
        return list_numbers[0]

    # recursive case

    # divide
    m = len(list_numbers) // 2
    part1 = list_numbers[0:m]
    part2 = list_numbers[m:]

    # conquer
    sum1 = sum_list(part1)
    sum2 = sum_list(part2)

    # combine
    return sum1 + sum2


def sum_multiply_5(list_numbers: list) -> int:
    """returns the sum of the multiples of 5 in list_numbers"""
    if list_numbers is None or len(list_numbers) == 0:
        return None, None

    if len(list_numbers) == 1:
        if list_numbers[0] % 5 == 0:
            return list_numbers[0]
        else:
            return 0

    m = len(list_numbers) // 2
    part1 = list_numbers[0:m]
    part2 = list_numbers[m:]

    sum1 = sum_multiply_5(part1)
    sum2 = sum_multiply_5(part2)
    return sum1 + sum2




def get_words_len_lower_2(words: list) -> list:
    """This function gets a list of words and returns a new list with
    those words whose length is lower or equal than 2"""
    if words is None or len(words) == 0:
        return []

    if len(words) == 1:
        w = words[0]
        if len(w) <= 2:
            return [w]
        else:
            return []

    m = len(words) // 2
    part1 = words[:m]
    part2 = words[m:]

    result1 = get_words_len_lower_2(part1)
    result2 = get_words_len_lower_2(part2)

    return result1 + result2


def longest_word(words):
    """This function based on divide and conquer gets a list of strings
    and returns the word with the longest length"""
    if words is None or len(words) == 0:
        return None

    if len(words) == 1:
        return words[0]

    m = len(words) // 2
    part1 = words[:m]
    part2 = words[m:]

    word1 = longest_word(part1)
    word2 = longest_word(part2)

    if word1 is None:
        return word2
    elif word2 is None:
        return word1
    else:
        if len(word1) >= len(word2):
            return word1
        else:
            return word2


def merge(list_1: list, list_2: list) -> list:
    """This functions gets two sorted lists and returns a new list
    whose elements are sorted in ascending order"""

    result = []
    i = 0  # for list_1
    j = 0  # for list_2

    while i < len(list_1) and j < len(list_2):
        if list_1[i] <= list_2[j]:
            result.append(list_1[i])
            i += 1
        else:
            result.append(list_2[j])
            j += 1

    while i < len(list_1):
        result.append(list_1[i])
        i += 1

    while j < len(list_2):
        result.append(list_2[j])
        j += 1

    return result


def mergesort(list_numbers: list) -> list:
    """This function takes a list of numbers and returns the sorted list"""

    if list_numbers is None or len(list_numbers) <= 1:
        return list_numbers
    else:
        # divide
        mid = len(list_numbers) // 2
        part1 = list_numbers[0:mid]
        part2 = list_numbers[mid:]

        # conquer
        sort1 = mergesort(part1)
        sort2 = mergesort(part2)

        # combine
        return merge(sort1, sort2)


def quicksort(list_numbers: list) -> None:
    if list_numbers is not None and len(list_numbers) > 1:
        _quicksort(list_numbers, 0, len(list_numbers) - 1)


def _quicksort(list_numbers: list, left: int, right: int):
    """This function implements quicksort by using the middle element
    as pivot"""
    i = left
    j = right

    m = (left + right) // 2

    p = list_numbers[m]  # pivot element in the middle

    while i <= j:
        while list_numbers[i] < p:
            i += 1

        while list_numbers[j] > p:
            j -= 1

        if i <= j:  # swap
            if i < j:
                list_numbers[i], list_numbers[j] = list_numbers[j], list_numbers[i]

            i += 1
            j -= 1

    if left < j:  # sort left list
        _quicksort(list_numbers, left, j)
    if i < right:  # sort right list
        _quicksort(list_numbers, i, right)


def quicksort_random(list_numbers: list) -> None:
    """This function implements the quicksort by using as pivot a random
    element in the list. In this case, the function does not return a new list, rather
    than update the input list to sort it."""
    if list_numbers is not None and len(list_numbers) > 1:
        _quicksort_random(list_numbers, 0, len(list_numbers) - 1)


def _quicksort_random(list_numbers: list, left: int, right) -> None:
    i, j = left, right
    p = list_numbers[randint(left, right)]  # pivot is random element

    while i <= j:
        while list_numbers[i] < p:
            i += 1
        while list_numbers[j] > p:
            j -= 1
        if i <= j:  # swap
            list_numbers[i], list_numbers[j] = list_numbers[j], list_numbers[i]
            i += 1
            j -= 1

    if left < j:  # sort left list
        _quicksort_random(list_numbers, left, j)
    if i < right:  # sort right list
        _quicksort_random(list_numbers, i, right)


def quicksort_first(list_numbers) -> list:
    """returns the sorted list by using quicksort. In this case, the pivot will be the first element of
    the  list"""
    if len(list_numbers) < 2:
        return list_numbers

    lower, p, greater = partition_first(list_numbers)

    return quicksort_first(lower) + [p] + quicksort_first(greater)


def partition_first(list_numbers: list) -> (list, int, list):
    """This function gets a list and takes its first element as pivot to create
    two partitions: lower and greater, where lower contains all elements lower than pivot,
    and greater contains all elements greater than pivot"""
    lower = []
    greater = []
    p = list_numbers[0]  # the pivot is the first element

    for i in range(1, len(list_numbers)):
        if list_numbers[i] < p:
            lower.append(list_numbers[i])
        else:
            greater.append(list_numbers[i])

    return lower, p, greater


def quicksort_last(list_numbers: list) -> list:
    """This function using quicksort to sort a list. The function returns the sorted list.
    In this case, pivot will be the last element """
    if len(list_numbers) < 2:
        return list_numbers

    lower, p, greater = partition_last(list_numbers)

    return quicksort_last(lower) + [p] + quicksort_last(greater)


def partition_last(list_numbers: list) -> (list, int, list):
    """This function gets a list and takes its last element as pivot to create
    two partitions: lower and greater, where lower contains all elements lower than pivot,
    and greater contains all elements greater than pivot"""
    lower = []
    greater = []
    p = list_numbers[-1]  # the pivot is the last element

    for j in range(0, len(list_numbers) - 1):
        if list_numbers[j] < p:
            lower.append(list_numbers[j])
        else:
            greater.append(list_numbers[j])

    return lower, p, greater


def quicksort_middle(arr: list, start: int, stop: int) -> None:
    """ Python implementation QuickSort using
        Lomuto's partition Scheme. """

    if start < stop:
        # pivot_index is the index where
        # the pivot lies in the array 
        pivot_index = partition_rand(arr, start, stop)

        # At this stage the array is partially sorted  
        # around the pivot. Separately sorting the  
        # left half of the array and the right half of the array. 
        quicksort_middle(arr, start, pivot_index - 1)
        quicksort_middle(arr, pivot_index + 1, stop)


def partition_rand(arr, start, stop):
    """This function creates a random number between the starting index of the array and the
    ending index of the array. """

    rand_pivot = randrange(start, stop)

    # Swapping the starting element of the array and the pivot 
    arr[start], arr[rand_pivot] = arr[rand_pivot], arr[start]
    return partition_sig(arr, start, stop)


''' 
This function takes the first element as pivot,  
places the pivot element at the correct position  
in the sorted array. All the elements are re-arranged  
according to the pivot, the elements smaller than the 
pivot is places on the left and the elements 
greater than the pivot is placed to the right of pivot. 
'''


def partition_sig(arr, start, stop):
    pivot = start  # pivot 
    k = start + 1  # a variable to memorize where the
    # partition in the array starts from. 
    for j in range(start + 1, stop + 1):

        # if the current element is smaller or equal to pivot, 
        # shift it to the left side of the partition. 
        if arr[j] <= arr[pivot]:
            arr[k], arr[j] = arr[j], arr[k]
            k = k + 1
    arr[pivot], arr[k - 1] = arr[k - 1], arr[pivot]
    pivot = k - 1
    return pivot


if __name__ == '__main__':

    '''
    #  Test find_max, find_max2
    list_n = []
    n = randint(0, 10)
    for i in range(n):
        list_n.append(randint(0, 50))
    
    print("The maximum element in {} is {} ".format(list_n, find_max(list_n)))
    print("The maximum element in {} is {} ".format(list_n, find_max2(list_n)))
    # These assertions must check to True
    assert(max(list_n) == find_max(list_n))
    assert(max(list_n) == find_max2(list_n))

    # Test
    list_n = []
    n = randint(0, 10)
    for i in range(n):
        list_n.append(randint(0, 50))
    min_result, max_result = find_min_max(list_n)
    print("The maximum and minimum elements in {} are ({},{}) ".format(list_n, min_result, max_result))
    # These assertions must check to True
    assert(min(list_n) == min_result)
    assert(max(list_n) == max_result)
    '''

    '''
    # Test find_lowest_even_odd
    list_n = []
    n = randint(0, 10)
    for i in range(n):
        list_n.append(randint(0, 25))

    print("findLowestEvenOdd({})={}".format(list_n, find_lowest_even_odd(list_n)))
    '''

    '''
    # Test sum_list and sum_multiply_5
    list_n = []
    n = randint(0, 10)
    for i in range(n):
        list_n.append(randint(0, 100))
    print("sum_list({})={}".format(list_n, sum_list(list_n)))
    print("sum_multiply_5({})={}".format(list_n, sum_multiply_5(list_n)))
    '''
    '''
    # Test get_words_len_lower_2
    words = ["Ha", "llegado", "el", "afilador", "a", "su", "domicilio", "a", "la", "puerta", "de", "su", "casa", "se",
             "afilan", "cuchillos", "tijeras"]
    print("get_words_len_lower_2({})  =\n    {}".format(words, get_words_len_lower_2(words)))
    '''

    '''
    # Test longest_word
    words = ['ata', 'mata', 'atare', 'vitamina', 'oz']
    print("longestWord({})={}".format(A, longest_word(words)))
    '''


    #  Test merge
    lista1 = [3, 4, 6, 7, 7, 8, 9]
    lista2 = [0, 1, 3, 4, 5, 6, 7, 10, 11, 12, 13]
    
    mergeList = merge(lista1, lista2)
    print(mergeList)

    # Test mergesort
    list_n = []
    n = randint(0, 10)
    for i in range(n):
        list_n.append(randint(-25, 25))
    print("mergesort({}) = {}".format(list_n, mergesort(list_n)))
    # Test quicksort returning a new list that is sorted
    print("quicksort_first({}) = {}".format(list_n, quicksort_first(list_n)))
    print("quicksort_last({}) = {}".format(list_n, quicksort_last(list_n)))

    # Test quicksort that sorts the input list and returns nothing
    input_list = list_n.copy()
    quicksort(list_n)
    print("quicksort({}) = {}".format(input_list, list_n))
    list_n = input_list.copy()
    quicksort_random(list_n)
    print("quicksort_random({}) = {}".format(input_list, list_n))

