#-*- coding: utf-8 -*-

from math import sqrt, floor

from p import Problem

from toolbox import is_pythagorean

class p9(Problem):

    """ 
        A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,

            a^2 + b^2 = c^2

        For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

        There exists exactly one Pythagorean triplet for which a + b + c = 1000.
        Find the product abc. 
        
    """

    def solve(self):

        a = 1
        b = 2
        c = int(floor(sqrt(a**2 + b**2)))
        while (a + b + c <= 1000):
            while (a + b + c <= 1000):
                if is_pythagorean(a, b, c) and a + b + c == 1000:
                    return a*b*c
                b += 1
                c = int(floor(sqrt(a**2 + b**2)))
            a +=1
            b = a + 1
            c = int(floor(sqrt(a**2 + b**2)))
