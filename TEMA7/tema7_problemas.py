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


def findMax2(A):
    if A is not None and len(A) > 0:
        return _findMax(A, 0, len(A) - 1)
    else:
        return None


def _findMax(A, start, end):
    if start == end:
        return A[start]
    else:
        mid = (start + end) // 2
        max1 = _findMax(A, start, mid)
        max2 = _findMax(A, mid + 1, end)
        return max(max1, max2)


A = [5, 3, 4]
print("findMax({})={}".format(A, find_max(A)))
print("findMax({})={}".format(A, findMax2(A)))

from random import randint

# Test 
data = []
for i in range(5):
    data.append(randint(0, 50))

print("The maximum element in {} is {} ".format(data, find_max(data)))
print("The maximum element in {} is {} ".format(data, findMax2(data)))

"""## Función que devuelva el mayor y menor elemento de un array 


"""


def findMaxMin(A):
    # A none or A=[]
    if A is None or len(A) == 0:
        return None, None

    # base case
    if len(A) == 1:
        return A[0], A[0]

        # Recursive case
    # dividir
    m = len(A) // 2
    part1 = A[0:m]
    part2 = A[m:]

    # vencer
    max1, min1 = findMaxMin(part1)
    max2, min2 = findMaxMin(part2)
    # combinar
    return max(max1, max2), min(min1, min2)


from random import randint

# Test 
data = []
for i in range(5):
    data.append(randint(0, 50))

print("The maximum and minimum elements in {} are {} ".format(data, findMaxMin(data)))
print("The maximum and minimum elements in {} are {} ".format(data, findMaxMin(data)))


def findLowestEvenOdd(A):
    """returns the lowest even and the lowest odd of A"""

    if A is None or len(A) == 0:
        return None, None

    if len(A) == 1:
        if A[0] % 2 == 0:
            return A[0], None
        else:
            return None, A[0]

    # dividir
    m = len(A) // 2
    part1 = A[0:m]
    part2 = A[m:]

    minEven1, minOdd1 = findLowestEvenOdd(part1)
    minEven2, minOdd2 = findLowestEvenOdd(part2)

    if minEven1 is not None and minEven2 is not None:
        minEven = min(minEven1, minEven2)
    elif minEven1 is None and minEven2 is not None:
        minEven = minEven2
    elif minEven2 is None and minEven1 is not None:
        minEven = minEven1
    else:  # los dos son None
        minEven = None

    if minOdd1 is not None and minOdd2 is not None:
        minOdd = min(minOdd1, minOdd2)
    elif minOdd1 is None and minOdd2 is not None:
        minOdd = minOdd2
    elif minOdd2 is None and minOdd1 is not None:
        minOdd = minOdd1
    else:  # los dos son None
        minOdd = None

    return minEven, minOdd


A = [3, 4, 2, 10, 0, -2, 1]

# print("findLowestEvenOdd({})={}".format(A,findLowestEvenOdd(A)))


import random

A = []
for i in range(0, 5):
    x = random.randint(0, 25)
    A.append(x)

print("findLowestEvenOdd({})={}".format(A, findLowestEvenOdd(A)))

import random

A = []
for i in range(0, 3):
    x = random.randint(0, 100)
    A.append(x)

print("findLowestEven({})={}".format(A, findLowestEven(A)))

A = [10, 14, 9, 20, 2, 38, 50]

print("findLowestEven({})={}".format(A, findLowestEven(A)))
A = [11, 15, 9, 21, 23, 381, 501]
print("findLowestEven({})={}".format(A, findLowestEven(A)))


def findLowestEvenOdd(A):
    """returns the lowest even and lowest odd"""
    if A is None or len(A) == 0:
        return None, None

    if len(A) == 1:
        if A[0] % 2 == 0:
            return A[0], None
        else:
            return None, A[0]

    m = len(A) // 2
    part1 = A[0:m]
    part2 = A[m:]

    even1, odd1 = findLowestEvenOdd(part1)
    even2, odd2 = findLowestEvenOdd(part2)

    if even1 is not None and even2 is not None:
        even = min(even1, even2)
    elif even1 is not None:
        even = even1
    else:
        even = even2

    if odd1 is not None and odd2 is not None:
        odd = min(odd1, odd2)
    elif odd1 is not None:
        odd = odd1
    else:
        odd = odd2

    return even, odd


import random

A = []
for i in range(0, 10):
    x = random.randint(0, 100)
    A.append(x)

print("findLowestEvenOdd({})={}".format(A, findLowestEvenOdd(A)))
A = [21, 3, 89, 43, 87, 41]
print("findLowestEvenOdd({})={}".format(A, findLowestEvenOdd(A)))
A = [58, 76, 10, 34]
print("findLowestEvenOdd({})={}".format(A, findLowestEvenOdd(A)))

"""Implementa una función basada en divide y 
vencerás que **sume los elementos múltiplos de 5 **en una array.

"""


def sumMultiply5(A):
    if A is None or len(A) == 0:
        return None, None

    if len(A) == 1:
        if A[0] % 5 == 0:
            return A[0]
        else:
            return 0

    m = len(A) // 2
    part1 = A[0:m]
    part2 = A[m:]

    sum1 = sumMultiply5(part1)
    sum2 = sumMultiply5(part2)
    return sum1 + sum2


import random

A = []
for i in range(0, 5):
    x = random.randint(0, 100)
    A.append(x)

print("sumMultiply5({})={}".format(A, sumMultiply5(A)))

lista1 = [3, 4, 6, 7, 7, 8, 9]
lista2 = [0, 1, 3, 4, 5, 6, 7, 10, 11, 12, 13]

mergeList = merge(lista1, lista2)
print(mergeList)

# Test
A = [5, 7, 1, 2, 4, 0, 3, 9, 10, 2, 3, 5]
print(A)
print(mergesort(A))

"""## Binary search

Given a **sorted list** and a number, x, return True if x is found, False otherwise.
"""


def binarySearch(A, x):
    """A is a sorted array. 
    It returns True if x is found, False eoc."""
    if A is None:
        return False

    # base case
    if len(A) == 0:
        return False
    # recursive case
    m = len(A) // 2

    if x == A[m]:
        return True

    if x < A[m]:
        return binarySearch(A[0:m], x)

    if x > A[m]:
        return binarySearch(A[m + 1:], x)


# Test
A = [1, 4, 38, 39, 40, 61, 69, 71, 81, 87]

x = 71  # an element that exists
print("binarySearch({},{})={}\n".format(A, x, binarySearch(A, x)))

# An element that does not exist
x = 50
print("binarySearch({},{})={}\n".format(A, x, binarySearch(A, x)))

# we randomly create a list 
data = []
for i in range(10):
    data.append(randint(0, 100))
# we sort it
data.sort()

for i in range(5):
    x = randint(0, 100)
    print("binarySearch({},{})={}\n".format(data, x, binarySearch(data, x)))

"""Implementa una función que reciba un **array  ordenado de enteros** A y un valor x, y **devuelva el índice de x en el array A**. Si x no existe, la función devuelve -1. No está permitido aplicar slicing (es decir, expresiones del tipo A[0:m] o A[m:]) ni crear sublistas auxiliares."""


def binarySearch(A, x, start=0, end=len(A) - 1):
    """returns the index of x in A. """
    # base case
    if A is None or len(A) == 0:
        return -1
    # recursive case

    m = (start + end) // 2
    if x == A[m]:
        return m

    if x < A[m]:
        return binarySearch(A, x, start, m - 1)
    if x > A[m]:
        return binarySearch(A, x, m + 1, end)


A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x = 4  # index=3
print(binarySearch(A, x))
for x in A:
    print(binarySearch(A, x), A.index(x))

"""## Suma de los elementos de un array

Implementa una función que reciba un array de enteros y devuelva su suma (aplicando divide y vencerás).


"""


def sumaArray(A):
    if A is None or len(A) == 0:
        return 0

    # base case
    if len(A) == 1:
        return A[0]

    # recursive case

    # dividir
    m = len(A) // 2
    part1 = A[0:m]
    part2 = A[m:]

    # vencer
    sum1 = sumaArray(part1)
    sum2 = sumaArray(part2)

    # combinar
    return sum1 + sum2


A = [1, 0, 3, 5, 2, 4, 5]
print(sum(A))
print(sumaArray(A))

"""Implementa una función basada en divide y vencerás que reciba una lista de strings y **devuelva una lista con los strings que tengan longitud menor o igual que 2**. 

"""


def getWordsLength2(words):
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

    result1 = getWordsLength2(part1)
    result2 = getWordsLength2(part2)

    return result1 + result2


words = ["Ha", "llegado", "el", "afilador", "a", "su", "domicilio", "a", "la", "puerta", "de", "su", "casa", "se",
         "afilan", "cuchillos", "tijeras"]
print("getWordsLength2({})  =\n    {}".format(words, getWordsLength2(words)))

"""Implementa una función basada en divide y vencerás que reciba una lista de strings y que devuelva la **palabra con mayor longitud**. """


def longestWord(words):
    if words is None or len(words) == 0:
        return None

    if len(words) == 1:
        return words[0]

    m = len(words) // 2
    part1 = words[:m]
    part2 = words[m:]

    word1 = longestWord(part1)
    word2 = longestWord(part2)

    if word1 is None and word2 is None:
        return None
    elif word1 is None:
        return word2
    elif word2 is None:
        return word1
    else:
        if len(word1) >= len(word2):
            return word1
        else:
            return word2


A = ['ata', 'mata', 'atare', 'vitamina', 'oz']
print("longestWord({})={}".format(A, longestWord(A)))

"""Algoritmo MergeSort"""


def merge(lista1, lista2):
    # lsita1 y lista2 están ordenadas!!!
    # devolver la lista ordenada
    result = []
    i = 0  # lista 1
    j = 0  # lista 2

    while i < len(lista1) and j < len(lista2):
        if lista1[i] <= lista2[j]:
            result.append(lista1[i])
            i += 1
        else:  # lista1[i]>lista2[j]
            result.append(lista2[j])
            j += 1

    while i < len(lista1):
        result.append(lista1[i])
        i += 1

    while j < len(lista2):
        result.append(lista2[j])
        j += 1

    return result


def mergesort(A):
    """returns a sorted array"""
    # Casos Bases

    if A is None or len(A) <= 1:
        return A
    else:
        # dividir
        mid = len(A) // 2
        part1 = A[0:mid]
        part2 = A[mid:]

        sort1 = mergesort(part1)
        sort2 = mergesort(part2)

        # part1 y part2 van a estar ordenadas

        return merge(sort1, sort2)


"""#Problemas propuestos (ídeas para el examen)


1) Implementa el algoritmo de **mergesort** adaptado para **listas enlazadas**. 

Te recomiendo que primero visualices este video https://www.youtube.com/watch?v=ywWBy6J5gz8&t=121s (pivote primer elemento)


9) Implementa una versión del quicksort que tome como el **último elemento como pivote**. Te recomiendo que primero visualices este vídeo: https://www.youtube.com/watch?v=biOjCLbdr7Y&t=37s (pivote último elemento)


10) Implementa una versión del quicksort que tome como un **pivote aleatorio**. En este link, puedes encontrar el pseudocódigo para comprobar si vas por buen camino: https://www.geeksforgeeks.org/quicksort-using-random-pivoting/

## Quicksort

### 1) Quicksort con pivote en la posición central del array
"""


def quicksort(A):
    _quicksort(A, 0, len(A) - 1)


def _quicksort(A, left, right):
    i = left
    j = right

    m = (left + right) // 2

    p = A[m]  # pivot element in the middle

    while i <= j:
        while A[i] < p:
            i += 1

        # estoy en un i cuyo valor es mayor que p

        while A[j] > p:
            j -= 1

        # llego un j cuyo valor es menor que p

        if i <= j:  # swap 
            if i < j:
                A[i], A[j] = A[j], A[i]

            i += 1
            j -= 1

    if left < j:  # sort left list
        _quicksort(A, left, j)
    if i < right:  # sort right list
        _quicksort(A, i, right)


# Test quicksort
import random

data = []
for i in range(0, 11):
    data.append(random.randint(0, 100))

print('input:', data)
quicksort(data)
print('sorted:', data)

"""## Implementation of quicksort using the first element as pivot

"""


def partition(A):
    lower = []
    greater = []
    p = A[0]  # the pivot is the first element

    for i in range(1, len(A)):
        if A[i] < p:
            lower.append(A[i])
        else:
            greater.append(A[i])

    return (lower, p, greater)


def quicksort_first(A):
    if len(A) < 2:
        return A

    lower, p, greater = partition(A)

    return quicksort_first(lower) + [p] + quicksort_first(greater)


import random

A = []
for i in range(15):
    A.append(random.randint(-20, 20))

print(A)
print(quicksort_first(A))

"""## Implementation of quicksort using the last element as pivot


"""


def partition(A):
    lower = []
    greater = []
    p = A[-1]  # the pivot is the last element

    for i in range(0, len(A) - 1):
        if A[i] < p:
            lower.append(A[i])
        else:
            greater.append(A[i])

    return (lower, p, greater)


def quicksort_last(A):
    if len(A) < 2:
        return A

    lower, p, greater = partition(A)

    return quicksort_last(lower) + [p] + quicksort_last(greater)


import random

A = []
for i in range(15):
    A.append(random.randint(-20, 20))

print(A)
print(quicksort_last(A))

"""## Quicksort with random

## Implementation of quicksort using a random pivot
"""


def quicksortRand(A):
    _quicksortRand(A, 0, len(A) - 1)


def _quicksortRand(A, left, right):
    i, j = left, right
    p = A[random.randint(left, right)]  # pivot is random element

    while i <= j:
        while A[i] < p:
            i += 1
        while A[j] > p:
            j -= 1
        if i <= j:  # swap 
            A[i], A[j] = A[j], A[i]
            i += 1
            j -= 1

    if left < j:  # sort left list
        _quicksortRand(A, left, j)
    if i < right:  # sort right list
        _quicksortRand(A, i, right)


import random

A = []
for i in range(15):
    A.append(random.randint(-20, 20))

print(A)
quicksortRand(A)
print(A)

# Python implementation QuickSort using  
# Lomuto's partition Scheme. 
import random

''' 
The function which implements QuickSort. 
arr :- array to be sorted. 
start :- starting index of the array. 
stop :- ending index of the array. 
'''


def quicksort(arr, start, stop):
    if (start < stop):
        # pivotindex is the index where  
        # the pivot lies in the array 
        pivotindex = partitionrand(arr, start, stop)

        # At this stage the array is partially sorted  
        # around the pivot. Separately sorting the  
        # left half of the array and the right half of the array. 
        quicksort(arr, start, pivotindex - 1)
        quicksort(arr, pivotindex + 1, stop)

    # This function generates random pivot, swaps the first 


# element with the pivot and calls the partition fucntion. 
def partitionrand(arr, start, stop):
    # Generating a random number between the  
    # starting index of the array and the 
    # ending index of the array. 
    randpivot = random.randrange(start, stop)

    # Swapping the starting element of the array and the pivot 
    arr[start], arr[randpivot] = arr[randpivot], arr[start]
    return partition(arr, start, stop)


''' 
This function takes the first element as pivot,  
places the pivot element at the correct position  
in the sorted array. All the elements are re-arranged  
according to the pivot, the elements smaller than the 
pivot is places on the left and the elements 
greater than the pivot is placed to the right of pivot. 
'''


def partition(arr, start, stop):
    pivot = start  # pivot 
    i = start + 1  # a variable to memorize where the  
    # partition in the array starts from. 
    for j in range(start + 1, stop + 1):

        # if the current element is smaller or equal to pivot, 
        # shift it to the left side of the partition. 
        if arr[j] <= arr[pivot]:
            arr[i], arr[j] = arr[j], arr[i]
            i = i + 1
    arr[pivot], arr[i - 1] = arr[i - 1], arr[pivot]
    pivot = i - 1
    return (pivot)


# Driver Code 
if __name__ == "__main__":
    array = [10, 7, 8, 9, 1, 5]
    quicksort(array, 0, len(array) - 1)
    print(array)
