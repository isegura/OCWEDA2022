#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Polynomial:
    """Python class to represent polynomial functions"""
    def __init__(self, coefficients: list) -> None:
        """This constructor takes the coefficients for the terms of the polynomial.
        We assume that the constant term (degree 0) is stored at the index 0 in the list,
        the term with degree 1 is at the index 1, and so on..."""
        self._coefficients = coefficients

    def __str__(self):
        """ Returns a string representing the polynomial function"""
        constant = self.get_coefficient(0)
        result = ''
        if constant != 0:
            result = str(constant)

        for i in range(1, self.degree()+1):
            term = self.get_coefficient(i)
            if term != 0:
                if result != '' and term > 0:
                    result = result+str('+')
                if term == 1:
                    term = ''
                elif term == -1:
                    term = '-'

            result += str(term)+str('x')

            if i > 1:
                result += str('^')+str(i)

        return result

    def degree(self) -> int:
        """It returns the degree of the polynomial"""
        return len(self._coefficients)-1

    def get_coefficient(self, i: int) -> int:
        """It returns the coefficient of the term with degree i"""
        if i < 0 or i > self.degree():
            print('{} index out of range'.format(i))
            return None

        return self._coefficients[i]

    def set_coefficient(self, i: int, new_value: int) -> None:
        """It modifies the coefficient of the term
        with degree i to new_value"""
        if i not in range(0, self.degree()+1):
            print('{} index out of range'.format(i))
            return

        self._coefficients[i] = new_value

    def evaluate(self, x: int) -> int:
        """This method returns the value
        of the polynomial functions for x"""
        result = 0
        for i in range(0, self.degree()+1):
            result += self.get_coefficient(i) * pow(x, i)

        return result

    def __add__(self, pol: "Polynomial") -> "Polynomial":
        """It returns a new polynomial which is the sum of the invoking polynomial (self)
        and pol. """

        # Create a new polynomial that is a copy of the polynomial with greater degree
        if self.degree() >= pol.degree():
            sum_pol = Polynomial(self._coefficients)
            # now, we have to add the coefficients from pol
            for i in range(0, pol.degree() + 1):
                sum_pol.set_coefficient(i, sum_pol.get_coefficient(i) + pol.get_coefficient(i))
        else:
            sum_pol = Polynomial(pol._coefficients)
            # now, we have to add the coefficients from self
            for i in range(0, self.degree()+1):
                sum_pol.set_coefficient(i, sum_pol.get_coefficient(i) + self.get_coefficient(i))

        return sum_pol


if __name__ == '__main__':
    # we create a polynomial
    p = Polynomial([1, 2, 3, 0, 0, -2, 8])
    # we test the method toString
    print('p={}'.format(str(p)))

    # we test the method degree
    print('Degree:{}'.format(p.degree()))

    # we test the method getCoefficient for different indexes
    print('getCoefficient(0)={}'.format(p.get_coefficient(0)))
    print('getCoefficient(1)={}'.format(p.get_coefficient(1)))
    print('getCoefficient(2)={}'.format(p.get_coefficient(2)))
    print('getCoefficient(3)={}'.format(p.get_coefficient(3)))

    # we test the method setCoefficient for several values
    p.set_coefficient(0, 0)
    print('setCoefficient(0,0)={}'.format(str(p)))

    p.set_coefficient(0, 5)
    print('setCoefficient(0,5)={}'.format(str(p)))

    p.set_coefficient(1, -1)
    print('setCoefficient(1,-1)={}'.format(str(p)))

    p.set_coefficient(2, 1)
    print('setCoefficient(2,1)={}'.format(str(p)))

    p.set_coefficient(3, 4)
    print('setCoefficient(3,4)={}'.format(str(p)))

    # we test the method evaluate for several values
    print('evaluate(0)={}'.format(p.evaluate(0)))
    print('evaluate(1)={}'.format(p.evaluate(1)))
    print('evaluate(2)={}'.format(p.evaluate(2)))

    q = Polynomial([3, -3, 7, 2, 0, 1])
    print('pol={}'.format(str(q)))
    print('p+pol={}'.format(str(p+q)))
