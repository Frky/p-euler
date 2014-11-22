#-*- coding: utf-8 -*-

from p import Problem

from toolbox import is_permutation


class p52(Problem):

    """
        It can be seen that the number, 125874, and its double, 251748, contain exactly 
        the same digits, but in a different order.

        Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain 
        the same digits.

    """


    def solve(self):
        n = 9
        found = False
        while not found:
            n += 1
            double_n = 2*n
            found = True
            for i in xrange(3, 7):
                if not is_permutation(double_n, i*n):
                    found = False
                    continue
        return n
