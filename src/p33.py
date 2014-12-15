#-*- coding: utf-8 -*-

from fractions import gcd

from p import Problem

class p33(Problem):

    """ 
        The fraction 49/98 is a curious fraction, as an inexperienced 
        mathematician in attempting to simplify it may incorrectly believe
        that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

        We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

        There are exactly four non-trivial examples of this type of fraction, 
        less than one in value, and containing two digits in the numerator and 
        denominator.

        If the product of these four fractions is given in its lowest common 
        terms, find the value of the denominator.
        
    """

    def solve(self):
        a = 10
        b = 10
        frac = list()
        
        while a < 100:
            while b < 100:
                for i in str(a):
                    if (i in str(b)):
                        na = int(str(a).replace(i,"", 1))
                        nb = int(str(b).replace(i,"", 1))
                        if (na * b == nb * a):
                            if (i != "0" and a != b):
                                frac.append(("{0}".format(a),"{0}".format(b)))
                b += 1
            a += 1
            b = a
        
        numerator = 1
        denominator = 1
        for i in frac:
            numerator *= int(i[0])
            denominator *= int(i[1])
        
        denominator = denominator / gcd(numerator, denominator)
        return denominator 
