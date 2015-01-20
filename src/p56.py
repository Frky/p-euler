#-*- coding: utf-8 -*-

from p import Problem

from toolbox import sum_of_digits

class p56(Problem):

    """
        A googol (10^100) is a massive number: one followed by one-hundred zeros; 
        100^100 is almost unimaginably large: one followed by two-hundred zeros. 
        Despite their size, the sum of the digits in each number is only 1.

        Considering natural numbers of the form, a^b, where a, b < 100, what is 
        the maximum digital sum?

    """


    def solve(self):
        res = 0
        for a in xrange(1, 100):
            for b in xrange(1, 100):
                ab = a**b
                res = max([res, sum_of_digits(ab)])
        return res

