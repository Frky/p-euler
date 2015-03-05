#-*- coding: utf-8 -*-

from p import Problem

from toolbox import Fraction

class p65(Problem):

    """
        The square root of 2 can be written as an infinite continued fraction.
        
        √2 = 1 + 1/(2 + 1/(2 + 1/(2 + ...
        
        The infinite continued fraction can be written, √2 = [1;(2)], (2) 
        indicates that 2 repeats ad infinitum. In a similar way, 
        √23 = [4;(1,3,1,8)].
        
        It turns out that the sequence of partial values of continued fractions 
        for square roots provide the best rational approximations. Let us 
        consider the convergents for √2.
        
            1 + 1/2                         = 3/2
            1 + 1/(2 + 1/2)                 = 7/5
            1 + 1/(2 + 1/(2 + 1/2))         = 17/12
            1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29
         
        Hence the sequence of the first ten convergents for √2 are:
        
            1, 3/2, 7/5, 17/12, 41/29, 99/70, 239/169, 577/408, 1393/985, 
            3363/2378, ...
        
        What is most surprising is that the important mathematical constant,
        e = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ...].
        
        The first ten terms in the sequence of convergents for e are:
        
            2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, ...
        
        The sum of digits in the numerator of the 10th convergent is 1+4+5+7=17.
        
        Find the sum of digits in the numerator of the 100th convergent of the 
        continued fraction for e.

    """

    
    def simplify(self, seq, val):
        res = val
        while len(seq) != 0:
            val = seq.pop(-1)
            res = val + ~res
        return res


    def gen_seq(self, n):
        if n == 0:
            return
        i = 1
        senti = 2
        yield 2
        while i < n:
            i += 1
            yield 1
            if (i == n):
                return
            i += 1
            yield senti
            senti += 2
            if (i == n):
                return
            i += 1
            yield 1


    def solve(self):
        vals = list()
        for i in self.gen_seq(100):
            vals.append(Fraction(i))
        res = self.simplify(vals[:-1], vals[-1]).num
        return sum([int(c) for c in str(res)])

