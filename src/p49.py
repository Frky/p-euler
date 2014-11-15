#-*- coding: utf-8 -*-

from p import Problem

from toolbox import is_prime


class p49(Problem):

    """
        The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, 
        is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit 
        numbers are permutations of one another.

        There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, 
        but there is one other 4-digit increasing sequence.

        What 12-digit number do you form by concatenating the three terms in this sequence?

    """

    
    def is_permutation(self, n, m):
        """
            Retourne True ssi les chiffres composant n sont les mêmes que les chiffres composant
            m.

        """

        sn = str(n)
        sm = str(m)
        if len(sn) != len(sm):
            return False

        for c in sn:
            if c not in sm:
                return False
        return True


    def solve(self):
        n = 1000
        for n in xrange(1000, 10000 - (2 * 3330)):
            if not is_prime(n):
                continue
            m = n + 3330
            if not self.is_permutation(n, m) or not is_prime(m):
                continue
            o = m + 3330
            if not self.is_permutation(n, o) or not is_prime(o):
                continue
            if n == 1487:
                continue
            return 100000000 * n + 10000 * m + o
            
