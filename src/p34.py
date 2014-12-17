#-*- coding: utf-8 -*-

from math import factorial

from p import Problem

class p34(Problem):

    """ 
        145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

        Find the sum of all numbers which are equal to the sum of the factorial
        of their digits.

        Note: as 1! = 1 and 2! = 2 are not sums they are not included. 
        
    """

    def solve(self):
        sup = 7*factorial(9)
        res = 0
        fact = [factorial(i) for i in xrange(0, 10)]
        for i in xrange(3, sup):
            s = str(i)
            tot = 0
            for a in s:
                tot += fact[(int(a))]
            if (tot == i):
                res += i
        return res
