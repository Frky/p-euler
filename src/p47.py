#-*- coding: utf-8 -*-

from math import sqrt

from p import Problem

from toolbox import pfactors, eratosthene, next_prime


class p47(Problem):

    """
        The first two consecutive numbers to have two distinct prime factors are:

        14 = 2 × 7
        15 = 3 × 5

        The first three consecutive numbers to have three distinct prime factors are:

        644 = 2² × 7 × 23
        645 = 3 × 5 × 43
        646 = 2 × 17 × 19.

        Find the first four consecutive integers to have four distinct prime factors. 
        What is the first of these numbers?

    """


    def __init__(self, id):
        self.primes = eratosthene(10000)
        return super(p47, self).__init__(id)


    def has_four_factors(self, n):
        """
            Retourne True ssi n a au moins 4 facteurs premiers

        """
        while self.primes[-1] < int(round(sqrt(n))) + 1:
            self.primes.append(next_prime(self.primes[-1]))
        return len(pfactors(n, self.primes)) >= 4


    def solve(self):
        n = 1
        while True:
            if self.has_four_factors(n):
                if self.has_four_factors(n+1):
                    if self.has_four_factors(n+2):
                        if self.has_four_factors(n+3):
                            return n
                        else:
                            n += 4
                    else:
                        n += 3
                else:
                    n += 2
            else:
                n += 1
