#-*- coding: utf-8 -*-

from p import Problem


class p15(Problem):

    """ 
        Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, 
        there are exactly 6 routes to the bottom right corner.

        How many such routes are there through a 20x20 grid? 
        
    """

    def __init__(self, id):
        self.imax = 20
        self.jmax = 20
        self.data = list()
        for i in xrange(self.imax + 1):
            self.data.append([-1] * (self.jmax + 1))
        return super(p15, self).__init__(id)

    def nb_path(self, i, j):
        """
            Retourne le nombre de chemins dans une grille de i * j cases

        """

        if j <= self.jmax and i <= self.imax and self.data[i][j] != -1:
            return self.data[i][j]
        else:
            if (i == 0 or j == 0):
                self.data[i][j] = 1
                return 1
            else:
                self.data[i-1][j] = self.nb_path(i-1, j)
                self.data[i][j-1] = self.nb_path(i, j-1)
                return self.data[i-1][j] + self.data[i][j-1]

    def solve(self):
        return self.nb_path(self.imax, self.jmax)
