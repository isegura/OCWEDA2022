import time


def sum_n(n: int) -> (int, float):
    """returns the sum of the first n numbers"""

    if not isinstance(n, int) or n < 0:
        return None

    result = 0
    start = time.time()  # returns the time in milliseconds
    for j in range(n+1):
        result += j
    end = time.time()
    return result, end-start    # we also return the time


def sum_gauss(n: int) -> (int, float):
    """returns the sum of the first n numbers, by
    applying Gauss sum"""

    if not isinstance(n, int) or n < 0:
        return None

    start = time.time()
    result = n*(n+1) / 2
    end = time.time()
    # we return the result and the execution time in seconds
    return result, (end-start)


if __name__ == '__main__':
    for i in range(1, 8):
        input_size = pow(10, i)
        result_sum, execution_time = sum_gauss(input_size)
        # print("sum_n({})={}, time={} ms".format(input_size, result_sum, execution_time))
        print("sum_gauss({})={}, time={} ms".format(input_size, result_sum, execution_time))

