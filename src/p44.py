#-*- coding: utf-8 -*-

from p import Problem

from math import sqrt

class p44(Problem):

    """
        Pentagonal numbers are generated by the formula, Pn=n(3n−1)/2. The first ten pentagonal numbers are:
        1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...
        It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference, 70 − 22 = 48, is not pentagonal.
        Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference are pentagonal and D = |Pk − Pj| 
        is minimised; what is the value of D?

    """


    def __is_pent(self, x):
        """
            Retourne true si x est un nombre pentagonal, false sinon

        """
        n = (sqrt(24*x + 1) + 1)/6.
        return n.is_integer()


    def test_pent(self):
        """
            Fonction test pour tester l'implémentation de __is_pent

        """

        res_test = True

        # Teste si la réponse est bien 'true' pour des nombres pentagonaux
        for n in xrange(1, 50):
            p = n * (3 * n - 1) / 2
            if (not self.__is_pent(p)):
                print "[err] {0} is the {1}-th pentagonal number (__is_pent returned false)".format(p, n)
                res_test = False
        # Teste si la réponse est bien 'false' pour des nombres non pentagonaux
        for n in xrange(1, 50):
            p = n * (3 * n - 1) / 2 + 1
            if (self.__is_pent(p)):
                print "[err] {0} is not a pentagonal number (__is_pent returned true)".format(p)
                res_test = False

        return res_test


    def p(self, n):
        """
            Retourne le nè nombre pentagonal

        """

        return n * (3*n - 1) / 2


    def solve(self):
        """
            Idée: pour un k donné, on cherche un couple (i, j) tel que P(j) - P(i) = P(k)
            Pour h = j - i donné, cela donne P(i + h) - P(i) = P(k), ce qui amène a i = ((P(k) - P(h)) / (3*h).
            En effet:
                P(i + h) - P(i) = P(k)
            <=> (i + h) (3i + 3h - 1) - i (3i - 1) = 2P(k)
            <=> 3ii + 3ih - i + 3ih + 3hh - h - 3ii - i = 2P(k)
            <=> 6ih + 3hh - h = 2P(k)
            <=> 6ih + h(3h - 1) = 2P(k)
            <=> 6ih = 2P(k) - 2P(h)
            <=> i = (P(k) - P(h)) / (3*h)

            Une fois le couple i, j trouvé, il ne reste plus qu'à tester si P(i) + P(j) est pentagonal.

        """
        
        k = 1
        d = -1
        while d == -1:
            pk = self.p(k)
            for h in xrange(1, k - 1):
                ph = self.p(h)
                i = (pk - ph) / (3*h)
                j = i + h
                pi = self.p(i)
                pj = self.p(j)
                if self.__is_pent(pi + pj) and self.__is_pent(pj - pi):
                    d = pj - pi 
            k += 1

        return d


if __name__ == "__main__":
    p = p44(44)
    if p.test_pent():
        print "[ok] Tests successful."
    else:
        print "[ko] Some tests failed."

