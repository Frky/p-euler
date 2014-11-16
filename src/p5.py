#-*- coding: utf-8 -*-

from p import Problem

from toolbox import decompose

class p5(Problem):

    """ 
        2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

        What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

    """


    def solve(self):
        Factors = list()
        Powers = list()
        for n in xrange(1, 21):
            decomp = decompose(n)
            for (f, p) in decomp:
                if f not in Factors:
                    Factors.append(f)
                    Powers.append(p)
                else:
                    ind = Factors.index(f)
                    Powers[ind] = max(Powers[ind], p)
        return reduce(lambda a, b: a * (b[0] ** b[1]), zip(Factors, Powers), 1)
