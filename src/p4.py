#-*- coding: utf-8 -*-

from p import Problem

from toolbox import is_palind

class p4(Problem):

    """ 
        A palindromic number reads the same both ways. 
        The largest palindrome made from the product of two 2-digit numbers is 9009 = 91  99.

        Find the largest palindrome made from the product of two 3-digit numbers. 
        
    """


    def solve(self):
        palind = 1

        i = 1000
        j = 999

        while i > 98:
            i -= 1
            while j > 99:
                if is_palind(i*j) and (i*j > palind):
                    palind = i*j
                j -= 1
            j = i - 1
        
        return palind
