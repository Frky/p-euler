#-*- coding: utf-8 -*-

from p import Problem

from toolbox import is_prime, eratosthene

class p60(Problem):

    """
        The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes 
        and concatenating them in any order the result will always be prime. For 
        example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four 
        primes, 792, represents the lowest sum for a set of four primes with this 
        property.

        Find the lowest sum for a set of five primes for which any two primes 
        concatenate to produce another prime.

    """

    def __init__(self, id):
        self.NMAX = 10000
        self.commute_with = list()
        for x in xrange(self.NMAX):
            self.commute_with.append(list())
        return super(p60, self).__init__(id)

    def commute(self, p, q):
        if not is_prime(int(str(p) + str(q))):
            return False
        if not is_prime(int(str(q) + str(p))):
            return False
        return True

    def find_commutation(self, n, curr):
        if n == 0:
            return curr
        if len(curr) != 0 and len(self.commute_with[curr[-1]]) == 0:
            return None
        if len(curr) == 0:
            mini = 3
        else:
            mini = curr[-1] + 1
        if mini >= len(self.commute_with):
            return None
        for p, pcom in enumerate(self.commute_with[mini:]):
            p += mini
            possible = True
            for c in curr:
                if p not in self.commute_with[c]:
                    possible = False
                    break
            if possible:
                res = self.find_commutation(n - 1, curr + [p])
                if res != None:
                    return res
        return None

    def solve(self):
        primes = eratosthene(self.NMAX)
        primes.remove(2)
        primes.remove(5)
        for i, p in enumerate(primes):
            for q in primes[i:]:
                if self.commute(p, q):
                    self.commute_with[p].append(q)

        return sum(self.find_commutation(5, list()))

