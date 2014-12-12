#-*- coding: utf-8 -*-

from math import log

from p import Problem

class p30(Problem):

    """ 
        Surprisingly there are only three numbers that can be written as the sum
        of fourth powers of their digits:

            1634 = 14**4 + 64**4 + 34**4 + 44**4
            8208 = 84**4 + 24**4 + 04**4 + 84**4
            9474 = 94**4 + 44**4 + 74**4 + 44**4
            As 1 = 1**4 is not a sum it is not included.

        The sum of these numbers is 1634 + 8208 + 9474 = 19316.

        Find the sum of all the numbers that can be written as the sum of fifth 
        powers of their digits. 
        
    """

    def find_sup(self):
        k = 2
        while (k*9**5 > 10**k):
            k += 1
        return k

    def solve(self):
        sup = 10**self.find_sup()
        res = 0

        for i in range(2,sup):
            s = str(i)
            tot = 0
            for j in s:
                tot += int(j)**5
            if (tot == i):
                res += i
        return res

