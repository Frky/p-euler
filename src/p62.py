#-*- coding: utf-8 -*-

from p import Problem

from toolbox import lowest_perm

class p62(Problem):

    """
        The cube, 41063625 (345^3), can be permuted to produce two other cubes: 
        56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the smallest 
        cube which has exactly three permutations of its digits which are also 
        cube.

        Find the smallest cube for which exactly five permutations of its digits 
        are cube.

    """

    def __init__(self, id):
        self.nmax = 100000
        self.seen = list()
        for i in xrange(10000):
            self.seen.append(dict())
        return super(p62, self).__init__(id)


    def solve(self):
        N = 5
        for n in xrange(300, self.nmax):
            r = lowest_perm(n ** 3)
            key = r / 10**7
            rest = r % 10**7
            while len(self.seen) < key + 1:
                self.seen.append(dict())
            if rest not in self.seen[key].keys():
                self.seen[key][rest] = list()
                self.seen[key][rest].append(n ** 3)
            elif len(str(n ** 3)) == len(str(self.seen[key][rest][0])): 
                self.seen[key][rest].append(n ** 3)
            if len(self.seen[key][rest]) == N:
                print self.seen[key][rest]
                return self.seen[key][rest][0]
        return None

