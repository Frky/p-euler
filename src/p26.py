#-*- coding: utf-8 -*-

from fractions import gcd

from p import Problem

class p26(Problem):

    """ 
        A unit fraction contains 1 in the numerator. The decimal representation
        of the unit fractions with denominators 2 to 10 are given:

            1/2 =   0.5
            1/3 =   0.(3)
            1/4 =   0.25
            1/5 =   0.2
            1/6 =   0.1(6)
            1/7 =   0.(142857)
            1/8 =   0.125
            1/9 =   0.(1)
            1/10    =   0.1

        Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It 
        can be seen that 1/7 has a 6-digit recurring cycle.

        Find the value of d  1000 for which 1/d contains the longest recurring 
        cycle in its decimal fraction part. 
        
    """

    def cycle_length(self, n):
        if (gcd(n,10) != 1):
            return 0
        l = 1
        while ((10**l - 1) % n != 0):
            l += 1
        return l
    
    def solve(self):
        # Liste des nombres dont les décimales sont finies de 1 à 1000
        regular = [1, 2, 4, 5, 8, 10, 16, 20, 25, 32, 40, 50, 64, 80, 100, 125, 128, 160, 200, 250, 256, 320, 400, 500, 512, 625, 640, 800, 1000]

        res = max([(val, self.cycle_length(val)) for val in xrange(1000)], key=lambda a: a[1])
        return res[0]
