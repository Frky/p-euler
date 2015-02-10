#-*- coding: utf-8 -*-

from p import Problem


from toolbox import is_cube

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
        self.nmax = 1000
        self.cube = [i ** 3 for i in xrange(self.nmax)]
        return super(p62, self).__init__(id)


    def permutations(self, n):        
        curr = list(str(n))
        while True:
            k0 = None
            for i in range(len(curr)-1):
                if curr[i] < curr[i+1]:
                    k0=i
            if k0 == None:
                return
    
            l0 = k0+1
            for i in range(k0+1, len(curr)):
                if curr[k0] < curr[i]:
                    l0 = i
    
            curr[k0], curr[l0] = curr[l0], curr[k0]
            curr[k0+1:] = reversed(curr[k0+1:])
            yield int("".join(curr))


    def iscube(self, n):
        for x in self.cube:
            if x == n:
                return True
            if x > n:
                return False
        return False


    def solve(self):
        N = 3
        print self.cube
        for res in xrange(100, self.nmax):
            n = 1
            for i in self.permutations(res**3):
                if self.iscube(i): #is_cube(i):
                    n += 1
                if n > N:
                    break
            if n == N:
                return res**3
        return None

