#-*- coding: utf-8 -*-

from p import Problem
from toolbox import int_length

class Fraction:

    def __init__(self, num, den):

        self.num = num
        self.den = den
    
    def read(self):

        print( str(self.num )+'/'+str(self.den))
        return

    def invert(self):

        tmp = self.num
        self.num = self.den
        self.den = tmp
        return

def int_to_frac(n):

    return Fraction(n, 1)

def frac_sum(frac1, frac2):
    """
        Return the exact sum of two fractions (without simplification)
    """
    result = Fraction(frac1.num * frac2.den + frac2.num * frac1.den, frac1.den*frac2.den)
    return result

def next_in_damn_suite(prev_frac):
    """
        Return the n-th iteration of the suite given the (n-1)-th
    """
    tmp_frac =  frac_sum(int_to_frac(1), prev_frac)
    tmp_frac.invert()
    return frac_sum(int_to_frac(1), tmp_frac)

class p57(Problem):

    """


        It is possible to show that the square root of two can be expressed as an infinite continued 
        fraction.

        √ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

        By expanding this for the first four iterations, we get:

        1 + 1/2 = 3/2 = 1.5
        1 + 1/(2 + 1/2) = 7/5 = 1.4
        1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
        1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

        The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion, 1393/985, 
        is the first example where the number of digits in the numerator exceeds the number of digits 
        in the denominator.

        In the first one-thousand expansions, how many fractions contain a numerator with more digits 
        than denominator?


    """


    def solve(self):

        frac = Fraction(3,2)
        res = 0

        #TEST :
        #for i in xrange(1, 10):
            #if int_length(frac.num) > int_length(frac.den) :
                #res += 1
            #frac.read()
            #frac = next_in_damn_suite(frac)
        
        for i in xrange(1, 1000):
            if int_length(frac.num) > int_length(frac.den) :
                res += 1
            frac = next_in_damn_suite(frac)

        return res