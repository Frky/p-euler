#-*- coding: utf-8 -*-

from math import sqrt 

from p import Problem

from toolbox import is_prime, next_prime


class p46(Problem):

    """
        It was proposed by Christian Goldbach that every odd composite number can be written 
        as the sum of a prime and twice a square.

            9 = 7 + 2×12
            15 = 7 + 2×22
            21 = 3 + 2×32
            25 = 7 + 2×32
            27 = 19 + 2×22
            33 = 31 + 2×12

        It turns out that the conjecture was false.
        What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

    """

    def solve(self):
        n = 9
        primes = [2]
        goldbach = True
        while goldbach:
            n += 2
            while is_prime(n):
                n += 2
            while primes[-1] < n:
                primes.append(next_prime(primes[-1]))
            goldbach = False
            for p in primes:
                if p > n:
                    break
                r = (n - p) / 2
                sr = int(round(sqrt(r))) 
                if (sr * sr == r):
                    goldbach = True
                    break  
        return n
