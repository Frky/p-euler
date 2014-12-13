#-*- coding: utf-8 -*-

from p import Problem

class p31(Problem):

    """ 
        1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
        It is possible to make £2 in the following way:

            1£1 + 150p + 220p + 15p + 12p + 31p
    
        How many different ways can £2 be made using any number of coins? 
    
    """

    def __init__(self, id):
        self.coins = [200,100,50,20,10,5,2,1]
        self.ways = list()
        return super(p31, self).__init__(id)

    def nb_sum(self, n, mincoin, s):
        for i in self.coins:
            if i < mincoin:
                continue
            if (i == n):
                self.ways.append(s)
            elif (i < n):
                self.nb_sum(n-i, i, s + str(i))

    def solve(self):
        self.nb_sum(200, 1, "")
        return len(self.ways)

