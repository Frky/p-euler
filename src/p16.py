#-*- coding: utf-8 -*-

from math import ceil, log

from p import Problem

class p16(Problem):

    """ 
        2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

        What is the sum of the digits of the number 2^1000? 

    """

    def solve(self):
        n = 2**1000
        return sum([(n/(10**i)) % 10 for i in xrange(int(ceil(log(n)/log(10))))])
