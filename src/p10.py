#-*- coding: utf-8 -*-

from p import Problem

from toolbox import eratosthene

class p10(Problem):

    """ 
        The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

        Find the sum of all the primes below two million. 
    
    """

    def solve(self):
        primes = eratosthene(2000000)
        return sum(primes)
