#-*- coding: utf-8 -*-

from math import factorial

from p import Problem

class p24(Problem):

    """ 
        A permutation is an ordered arrangement of objects. For example, 3124 is
        one possible permutation of the digits 1, 2, 3 and 4. If all of the 
        permutations are listed numerically or alphabetically, we call it 
        lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

            012   021   102   120   201   210

        What is the millionth lexicographic permutation of the digits 0, 1, 2,
        3, 4, 5, 6, 7, 8 and 9? 
        
    """

    def solve(self):
        # avec 0 comme premier nombre, on a 9! permutations possibles
        # soit 362880 permutations
        # la 362881e est donc <1023456789>
        # la 725761e est donc <2013456789>
        # -> il reste à trouver la (1000000 - 725761)e permutation de 9 chiffres

        res = 0
        tmp = 1000000

        used = range(0,10)

        for i in range(1,11):
            a = tmp / factorial(10 - i)
            tmp = tmp % factorial(10 - i)
            if tmp == 0:
                a -= 1
            res *= 10
            res += used[a]
            used.remove(used[a])
        return res

