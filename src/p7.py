#-*- coding: utf-8 -*-

from p import Problem

from toolbox import eratosthene

class p7(Problem):

    """ 
        By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

        What is the 10001st prime number? 
        
    """

    def solve(self):
        # Crible d'érathostène
        # Estimation : un nombre sur dix est premier
        # (pas trop faux jusque un million)
        # => crible de 1 à 150 000 (soyons large)
        sieve = eratosthene(150000)
        return sieve[10000]


