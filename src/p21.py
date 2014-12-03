#-*- coding: utf-8 -*-

from p import Problem

from toolbox import divisors 

class p21(Problem):

    """ 
        Let d(n) be defined as the sum of proper divisors of n (numbers less 
        than n which divide evenly into n).
        If d(a) = b and d(b) = a, where a  b, then a and b are an amicable pair 
        and each of a and b are called amicable numbers.

        For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 
        44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 
        2, 4, 71 and 142; so d(284) = 220.

        Evaluate the sum of all the amicable numbers under 10000. 
        
    """

    def solve(self):
        d = list()
        d.append(0)
        d.append(1)
        res = 0
        for i in xrange(2, 10001):
            sum_div = sum(divisors(i)[:-1])
            d.append(sum_div)
            if (sum_div < i and d[sum_div] == i):
                res += i
                res += sum_div
        return res


