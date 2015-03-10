#-*- coding: utf-8 -*-

from p import Problem

from toolbox import is_square, continuous_fraction, seq_to_frac

class p66(Problem):

    """
        Consider quadratic Diophantine equations of the form:
        
            x^2 – D x y^2 = 1
        
        For example, when D=13, the minimal solution in x is 649^2 – 13×180^2 = 1.
        
        It can be assumed that there are no solutions in positive integers when D is square.
        
        By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:
        
            3^2 – 2×2^2 = 1
            2^2 – 3×1^2 = 1
            9^2 – 5×4^2 = 1
            5^2 – 6×2^2 = 1
            8^2 – 7×3^2 = 1
        
        Hence, by considering minimal solutions in x for D ≤ 7, the largest x is obtained when D=5.
        
        Find the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained.
    
    """

    def solve(self):
        res = 0
        x_max = 0
        for d in xrange(2, 1000):
            if is_square(d):
                continue
            (a, b) = continuous_fraction(d)
            if len(b) % 2 == 0:
                f = seq_to_frac([a] + b[:-1])
            else:
                f = seq_to_frac([a] + b + b[:-1])
            x, y = f.num, f.den
            if x**2 - d * y**2 != 1:
                print "ERROR COMPUTING SOLUTION"
                return None
            if x > x_max:
                x_max = x
                res = d
        return res
