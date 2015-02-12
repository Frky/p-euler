#-*- coding: utf-8 -*-

from p import Problem

class p63(Problem):

    """
        The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 
        9-digit number, 134217728=8^9, is a ninth power.

        How many n-digit positive integers exist which are also an n-th power?

    """

    def n_digits(self, N):
        i = 1
        res = 0
        for i in xrange(1, 10):
            if i ** N >= 10**(N-1):
                res += 1
        return res

    
    def limit(self, NMAX):
        pos = list()
        for i in xrange(1, NMAX):
            if 9 ** i > 10 ** (i - 1):
                pos.append(i)
        return pos


    def solve(self):
        res = 0
        for n in self.limit(100):
            res += self.n_digits(n)
        return res

