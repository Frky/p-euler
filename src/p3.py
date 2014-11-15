#-*- coding: utf-8 -*-

from p import Problem

from toolbox import pfactors, largest_factor


class p3(Problem):

    """ 
        The prime factors of 13195 are 5, 7, 13 and 29.

        What is the largest prime factor of the number 600851475143 ? 
        
    """


    def solve(self):
        n = 600851475143
        return largest_factor(n)
        fact = pfactors(n)
        return max(fact)

