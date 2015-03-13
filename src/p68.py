#-*- coding: utf-8 -*-

from p import Problem

import itertools

class p68(Problem):

    """ 
        Consider the following "magic" 3-gon ring, filled with the numbers 1 to 
        6, and each line adding to nine.
       
                4
                  3
                1   2   6
             5

        Working clockwise, and starting from the group of three with the 
        numerically lowest external node (4,3,2 in this example), each solution 
        can be described uniquely. For example, the above solution can be 
        described by the set: 4,3,2; 6,2,1; 5,1,3.
        
        It is possible to complete the ring with four different totals: 9, 10, 
        11, and 12. There are eight solutions in total.
        
            Total   Solution Set
            9   4,2,3; 5,3,1; 6,1,2
            9   4,3,2; 6,2,1; 5,1,3
            10  2,3,5; 4,5,1; 6,1,3
            10  2,5,3; 6,3,1; 4,1,5
            11  1,4,6; 3,6,2; 5,2,4
            11  1,6,4; 5,4,2; 3,2,6
            12  1,5,6; 2,6,4; 3,4,5
            12  1,6,5; 3,5,4; 2,4,6

        By concatenating each group it is possible to form 9-digit strings; the
        maximum string for a 3-gon ring is 432621513.
        
        Using the numbers 1 to 10, and depending on arrangements, it is possible 
        to form 16- and 17-digit strings. What is the maximum 16-digit string 
        for a "magic" 5-gon ring?

            o
              o  o
            o   o
          o  o o o
              o

    """

    class GonRing(object):
        def __init__(self, vals):
            self.gon = list()
            self.gon.append((vals[0], vals[1], vals[2]))
            i = 3
            while i != len(vals) - 1:
                self.gon.append((vals[i], vals[i - 1], vals[i + 1]))
                i += 2
            self.gon.append((vals[-1], vals[-2], vals[1]))
            min_start = min([x[0] for x in self.gon])
            while self.gon[0][0] != min_start:
                self.gon = self.gon[1:] + [self.gon[0]]

        def is_magic(self):
            ref = sum(self.gon[0])
            for t in self.gon[1:]:
                if sum(t) != ref:
                    return False
            return True
            
        def hash(self):
            h = 0
            for t in self.gon:
                for e in t:
                    if (e < 10):
                        h = 10 * h + e
                    else:
                        h = 100 * h + e
            return h

        def __str__(self):
            return str(self.gon)

    def solve(self):
        gons = list()
        for vals in itertools.permutations(range(1, 11)):
            if sum(vals[:3]) != sum((vals[-1], vals[-2], vals[1])):
                continue
            gon = self.GonRing(vals)
            if gon.is_magic() and gon.hash() not in gons:
                gons.append(gon.hash())
        return max([n for n in gons if n < 10**16])
