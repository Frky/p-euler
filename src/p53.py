#-*- coding: utf-8 -*-

from p import Problem

from toolbox import combination


class p53(Problem):

    """
        There are exactly ten ways of selecting three from five, 12345:

            123, 124, 125, 134, 135, 145, 234, 235, 245, and 345
        
        In combinatorics, we use the notation, C(3, 5) = 10.
        In general,

            C(r, n) = n! / [r!(n−r)!] ,
        
        where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.
        It is not until n = 23, that a value exceeds one-million: C(10, 23) = 1144066.

        How many, not necessarily distinct, values of  C(r,n), for 1 ≤ n ≤ 100, are greater than one-million?

    """


    def solve(self):
        res = 0
        for n in xrange(1, 101):
            for r in xrange(1, n + 1):
                if combination(r, n) >= 1000000:
                    res += 1
        return res
