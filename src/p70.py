#-*- coding: utf-8 -*-

from p import Problem

from toolbox import phi, is_permutation

class p70(Problem):

    """ 
        Euler's Totient function, φ(n) [sometimes called the phi function], is
        used to determine the number of positive numbers less than or equal to 
        n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 
        8, are all less than nine and relatively prime to nine, φ(9)=6. The 
        number 1 is considered to be relatively prime to every positive number, 
        so φ(1)=1.

        Interestingly, φ(87109)=79180, and it can be seen that 87109 is a 
        permutation of 79180.

        Find the value of n, 1 < n < 10^7, for which φ(n) is a permutation of n 
        and the ratio n/φ(n) produces a minimum.

    """

    def solve(self):
        res = 2
        mini = 10**10
        table = [0]
        for n in range(1, 10**7):
            pn = phi(n, table)
            table.append(pn)
            if n > 1 and float(n) / pn < mini and is_permutation(n, pn):
                res = n
                mini = float(n)/pn
        return res

