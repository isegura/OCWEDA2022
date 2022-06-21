#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


class Complex:

    def __init__(self, real: int = 0, imag: int = 0) -> None:
        """ This is the constructor method. By default,
        the values for the attributes are 0"""
        self.a = real  # real part
        self.b = imag  # imaginary part

    def __neg__(self) -> "Complex":
        """Returns the negation of the complex number"""
        return Complex(-self.a, -self.b)

    def __add__(self, other):
        """Returns a nex complex number, which is
        the sum of the invoking complex number and the other parameter"""
        return Complex(self.a + other.a, self.b + other.b)

    def __sub__(self, other):
        """Returns a nex complex number, which is
        the subtraction of the invoking complex number and the other parameter"""
        return Complex(self.a - other.a, self.b - other.b)

    def __mul__(self, other):
        """Returns a new complex number, which is the multiplication
        of the invoking complex number
        and the other parameter"""
        return Complex(self.a * other.a - self.b * other.b,
                       self.a * other.b + self.b * other.a)

    def module(self):
        """Returns the module of the invoking complex number"""
        return math.sqrt(math.pow(self.a, 2) + math.pow(self.b, 2))

    def __str__(self):
        """Returns a string representing the complex number"""
        if self.a == 0 and self.b == 0:
            return '0'
        text = ''
        if self.a == 0:
            text = '{}i'.format(self.b)
        elif self.b == 0:
            text = '{}'.format(self.a)
        elif self.b < 0:
            text = '{}{}i'.format(self.a, self.b)
        elif self.b > 0:
            text = '{}+{}i'.format(self.a, self.b)
        return text


if __name__ == '__main__':
    c1 = Complex(3, 5)
    print('c1:', str(c1))
    c2 = Complex(2, 8)
    print('c2:', str(c2))
    c3 = Complex(-1, -2)
    print('c3:', str(c3))
    c4 = Complex(0, -2)
    print('c4:', str(c4))
    c5 = Complex(-1, 0)
    print('c5:', str(c5))

    print('Neg of {} = {}'.format(str(c1), str(-c1)))
    print('Module of {} = {}'.format(str(c1), c1.module()))
    print('Module of {} = {}'.format(str(c5), c5.module()))

    print('({})+({}) = {}'.format(str(c1), str(c2), str(c1 + c2)))
    print('({})-({}) = {}'.format(str(c1), str(c3), str(c1 - c3)))
    print('({})*({}) = {}'.format(str(c1), str(c4), str(c1 * c4)))
