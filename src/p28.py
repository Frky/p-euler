#-*- coding:utf-8 -*-

from p import Problem

class p28(Problem):

    """ 
        Starting with the number 1 and moving to the right in a clockwise 
        direction a 5 by 5 spiral is formed as follows:

            21 22 23 24 25
            20  7  8  9 10
            19  6  1  2 11
            18  5  4  3 12
            17 16 15 14 13

        It can be verified that the sum of the numbers on the diagonals is 101.

        What is the sum of the numbers on the diagonals in a 1001 by 1001 
        spiral formed in the same way? 
        
    """

    def generate_spiral(self, n):
        spiral = list()
        for i in range(0,n):
            spiral.append(range(0,n))


    def solve(self):
        # 1 est sur la diagonale du carré de coté 1
        # génération d'un carré de coté 3 commençant par 2
        # -> 3, 5, 7, 9 sont sur la diagonale
        # génération d'un carré de coté 5 commançant par 10
        # -> 13, 17, 21, 25 sont sur la diagonale
        
        n = 1001
        res = 1
        i = 3
        k = 2
        c = [1,1,1,1]
        while i <= n:
            c[0] = c[3] + i - 1
            res += c[0]
            c[1] = c[0] + i - 1
            res += c[1]
            c[2] = c[1] + i - 1
            res += c[2]
            c[3] = c[2] + i - 1
            res += c[3]
            i += 2
        return res

