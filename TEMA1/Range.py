# -*- coding: utf-8 -*-

class Range:
    """A class that mimics the built-in range class."""

    def __init__(self, start: int, end: int, step=1) -> None:
        """Initialize a Range instance
        - _start is the initial value of the range,
        - _end is the upper limit. This value does not belong
        to the range.
        - _step: by default 1.
        """
        if step == 0:
            raise ValueError('_step cannot be 0') #we throw an error
        self._start = start
        self._end = end
        self._step = step

    def __len__(self) -> int:
        """ returns the number of elements in the range"""
        result = (self._end - self._start + self._step - 1) // self._step
        return max(0, result)

    def __getitem__(self, i: int) -> int:
        """Returns the ith element of the sequence"""
        if i < 0 or i > len(self):
            raise IndexError('index out of range')

        return self._start + i * self._step

    def __str__(self):
        """Returns a string containing the sequence"""
        result = '['
        for i in range(0,len(self)):
            result = result + str(self[i]) + ','
        result = result[:-1]
        result += ']'
        return result

    def __sum__(self):
        """Returns a string containing the sequence"""
        elem = self._start
        result = 0
        while elem < self._end:
            result += elem
            elem += self._step
        return result


if __name__ == '__main__':
    r = Range(2, 20, 2)
    print(str(r))
    print("size = {}".format(len(r)))
    print("sum = {}".format(sum(r)))
