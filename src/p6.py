#-*- coding: utf-8 -*-

from p import Problem

from toolbox import sumSquare, squareSum

class p6(Problem):

    """ 
        The sum of the squares of the first ten natural numbers is,
        
        12 + 22 + ... + 102 = 385
        The square of the sum of the first ten natural numbers is,
        
        (1 + 2 + ... + 10)2 = 552 = 3025
        Hence the difference between the sum of the squares of the first ten natural numbers and 
        the square of the sum is 3025  385 = 2640.
        
        Find the difference between the sum of the squares of the first one hundred natural numbers 
        and the square of the sum. 
        
    """


    def solve(self):
        return squareSum(100) - sumSquare(100)
