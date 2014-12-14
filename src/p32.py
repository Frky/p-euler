#-*- coding: utf-8 -*-

from p import Problem

class p32(Problem):

    """ 
        We shall say that an n-digit number is pandigital if it makes use of all 
        the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 
        1 through 5 pandigital.
    
        The product 7254 is unusual, as the identity, 39 * 186 = 7254, containing 
        multiplicand, multiplier, and product is 1 through 9 pandigital.
    
        Find the sum of all products whose multiplicand/multiplier/product identity 
        can be written as a 1 through 9 pandigital.
    
        HINT: Some products can be obtained in more than one way so be sure to only 
        include it once in your sum. 
    
    """

    def is_pandigital(self, s):
        if len(s) != 9:
            return False
        for n in "123456789":
            if n not in s:
                return False
        return True

    def solve(self):
        pandigitals = list()
        a = 0
        b = 0
        while (a*b < 9876):
            a += 1
            while (a*b < 9876):
                s = str(a) + str(b) + str(a*b)
                if self.is_pandigital(s) and a * b not in pandigitals:
                    pandigitals.append(a*b)
                b += 1
            b = 1
        return sum(pandigitals)
