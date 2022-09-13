import time


def sum_n(n: int) -> int:
    """returns the sum of the first n numbers"""
    result = 0
    for j in range(n+1):
        result += j

    return result


def sum_gauss(n: int) -> int:
    """returns the sum of the first n numbers, by
    applying Gauss sum"""
    return n*(n+1) // 2


if __name__ == '__main__':
    for i in range(1, 8):
        input_size = pow(10, i)
        result_sum, execution_time = sum_gauss(input_size)
        print("sum_gauss({})={}, time={} ms".format(input_size, result_sum, execution_time*1000))


