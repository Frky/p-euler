#-*- coding: utf-8 -*-

from p import Problem

from toolbox import eratosthene, is_prime


class p50(Problem):

    """
        The prime 41, can be written as the sum of six consecutive primes:

            41 = 2 + 3 + 5 + 7 + 11 + 13
        
        This is the longest sum of consecutive primes that adds to a prime below one-hundred.
        The longest sum of consecutive primes below one-thousand that adds to a prime, 
        contains 21 terms, and is equal to 953.

        Which prime, below one-million, can be written as the sum of the most consecutive primes?

    """


    def solve(self):
        pmax = 1000000
        primes = eratosthene(pmax)
        size = 0
        s = 0
        # Computing the max size of the sequence:
        # It is the largest number such that the first 
        # size prime numbers are less than pmax.
        while s < pmax:
            s += primes[size]
            size += 1
        while size > 1:
            for i in xrange(0, len(primes) - size + 1):
                p = sum(primes[i:i+size + 1])
                if p > pmax:
                    break
                if is_prime(p):
                    print "Found: sequence of size {0}".format(size)
                    return p
            size -= 1
