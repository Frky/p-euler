#-*- coding: utf-8 -*-

from math import log, floor

from p import Problem


class p48(Problem):

    """
        The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
        Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

    """


    def solve(self):
        n = 1
        s = 0 
        while n <= 1000:
            s += n ** n
            if n == 10:
                print "Checkpoint: {0}".format(s)
            n += 1
        return s % 10000000000
