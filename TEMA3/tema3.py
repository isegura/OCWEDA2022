import time
import random


def sum_n(n: int) -> (int, float):
    """returns the sum of the first n numbers"""

    if not isinstance(n, int) or n < 0:
        return None

    result_sum = 0
    start = time.time()  # returns the time in milliseconds
    for j in range(n+1):
        result_sum += j
    end = time.time()
    return result_sum, end-start    # we also return the time


def sum_gauss(n: int) -> (int, float):
    """returns the sum of the first n numbers, by
    applying Gauss sum"""

    if not isinstance(n, int) or n < 0:
        return None

    start = time.time()
    result_gauss = n*(n+1) / 2
    end = time.time()
    # we return the result and the execution time in seconds
    return result_gauss, (end-start)


def sum_list(a: list) -> (int, float):
    """gets a list and returns the sum of its elements.
    It is not allowed to use the functon sum.
     It also returns the execution time"""
    if a is None or not isinstance(a, list):
        return None, None

    start = time.time()  # return the number of seconds
    result_sum = 0
    for x in a:
        result_sum += x
    end = time.time()
    return result_sum, end - start


def random_list(n: int, start: int = -10, end: int = 10) -> list:
    """gets a positive number and returns a list of integers that have been randomly
    created. You can define the range [start, end] for the elements."""
    if not isinstance(n, int) or n < 0:
        return None

    result_list = []
    for _ in range(n):
        result_list.append(random.randint(start, end))
    return result_list


def pair_0(a: list) -> int:
    """returns the number of pairs such as i!=j and a[i]+a[j]=0"""
    num_pairs = 0                      # 1
    for i in range(len(a)-1):       # it will be run n-1 times, where n is len(a)
        for j in range(i+1, len(a)):  # it will be run n-(i+1),
            if a[i] + a[j] == 0:    # 1 + 1 +1 + 1
                num_pairs += 1         # 2

    return num_pairs                   # 1


def multiply(matrix1, matrix2):
    """gets two matrices and multiplies them. To multiply one matrix with another,
    we need to check first, if the number of columns of the first matrix
    is equal to the number of rows of the second matrix.
    Now multiply each element of the column of the first matrix
    with each element of rows of the second matrix and add them all.
    """
    if len(matrix1[0]) != len(matrix2):                                         # 4
        print('Error: cannot be multiplied!!!')
        return None

    n_rows = len(matrix1)                                                       # 2
    n_columns = len(matrix2[0])                                                 # 3
    product_matrix = [[0 for _ in range(n_columns)] for _ in range(n_rows)]     # n_columns * n_rows

    for i in range(n_rows):                                                     # n_columns
        for j in range(n_columns):                                              # n_rows
            for k in range(n_rows):                                             # n_columns
                product_matrix[i][j] += matrix1[i][k] * matrix2[k][j]           # 6

    return product_matrix                                                       # 1


if __name__ == '__main__':
    '''
    # Execution times for sum_n
    for i in range(1, 8):
        input_size = pow(10, i)
        result_sum, execution_time = sum_n(input_size)
        # print("sum_n({})={}".format(input_size, result_sum))
        print("{}\t{}".format(input_size, str(execution_time*1000)).replace(".", ","))
    '''

    '''
    # Execution times for sum_gauss
    for i in range(1, 8):
        input_size = pow(10, i)
        result_sum, execution_time = sum_gauss(input_size)
        # print("sum_n({})={}".format(input_size, result_sum))
        print("{}\t{}".format(input_size, str(execution_time*1000)).replace(".", ","))
    '''

    '''
    # Execution times for sum_list 
    for i in range(0, 8):
        input_size = pow(10, i)
        input_list = random_list(input_size)
        result_sum, execution_time = sum_list(input_list)
        # print("sum_list({}) = {}".format(input_list, result_sum))
        # we multiply * 1000 to obtain ms
        # Maybe you need to replace '.' by ',' (this depends on the setting of your worksheet)
        print("{}\t{}".format(input_size, str(execution_time*1000)).replace(".", ","))
    '''

    '''
    # Test for pair_0
    array = [-5, 0, 5, -1, 1, 5, 0, 1, 2, -2]
    print("pair_0({}) = {}".format(array, pair_0(array)))
    '''

    ''' Test for multiply
    # take a 3x3 matrix
    matrix_a = [[12, 7, 3], [4, 5, 6], [7, 8, 9]]

    # take a 3x4 matrix
    matrix_b = [[5, 8, 1, 2], [6, 7, 3, 0], [4, 5, 9, 1]]

    result = multiply(matrix_a, matrix_b)
    print(result)
    '''
