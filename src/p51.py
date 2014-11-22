#-*- coding: utf-8 -*-

from p import Problem

from toolbox import is_prime, next_prime


class p51(Problem):

    """
        By replacing the 1st digit of the 2-digit number *3, it turns out that six of the 
        nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

        By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number 
        is the first example having seven primes among the ten generated numbers, yielding 
        the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. 
        Consequently 56003, being the first member of this family, is the smallest prime with 
        this property.

        Find the smallest prime which, by replacing part of the number (not necessarily 
        adjacent digits) with the same digit, is part of an eight prime value family.

    """


    def solve(self):
        # Strating from 2
        n = 2
        # List of numbers from 0 to 9
        numerals = [str(i) for i in xrange(0, 10)]
        # Number to replace in the primes
        num_to_replace = "1"
        # Family of primes from n by replacing num_to_place by numerals
        family = list()
        
        while True:
            # Getting string from n
            str_n = str(n)
            # Family is empty at the beginning
            family = []
            # If there is no number to replace
            if str_n.count(num_to_replace) == 0:
                    # We compute the next prime and skip the rest of the loop
                    n = next_prime(n)
                    continue
            # else, for any possible numeral
            for numeral in numerals:
                # if we are replacing by 0, we check that we will not replace the first digit
                if (numeral == "0" and str_n[0] == num_to_replace):
                    continue
                # We compute the number obtained by replacing all num_to_replace in n by the current numeral
                m = int(str_n.replace(num_to_replace, numeral))
                # We check if m is prime
                if m >= 2 and is_prime(m):
                    # If it is, we add it to the family
                    family.append(m)
            # At the end, if the family contains at least 8 numbers
            if len(family) >= 8:
                # We return the first one
                return n
            # Else, we compute the next prime and perform another iteration
            n = next_prime(n)
