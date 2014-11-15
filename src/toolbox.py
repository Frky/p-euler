#-*- coding: utf-8 -*-

import random
from math import sqrt


##### PRIME NUMBERS RELATIVE FUNCTIONS #####


def eratosthene(n):
    """
        Retourne la liste des nombres premiers entre 1 et n
        Utilise la méthode du crible d'Ératosthène

    """
    
    sieve = range(2, n + 1)
    for i in xrange(2, int(round(sqrt(n))) + 2):
        j = 2 * i
        while (j <= n):
            sieve[j - 2] = 0
            j += i
    return [p for p in sieve if p != 0]


def is_prime(n):
    """
        Test de primalité de Miller-Rabin
        Code pris sur rosettacode.org

    """

    _mrpt_num_trials = 5

    assert n >= 2
    # special case 2
    if n == 2:
        return True
    # ensure n is odd
    if n % 2 == 0:
        return False
    # write n-1 as 2**s * d
    # repeatedly try to divide n-1 by 2
    s = 0
    d = n-1
    while True:
        quotient, remainder = divmod(d, 2)
        if remainder == 1:
            break
        s += 1
        d = quotient
    assert(2**s * d == n-1)
 
    # test the base a to see whether it is a witness for the compositeness of n
    def try_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True # n is definitely composite
 
    for i in range(_mrpt_num_trials):
        a = random.randrange(2, n)
        if try_composite(a):
            return False
 
    return True # no base tested showed n as composite


def next_prime(n):
    """
        Retourne le plus petit nombre premier strictement supérieur à n

    """
    
    if (n % 2 == 0):
        n += 1
    else:
        n += 2
    while not is_prime(n):
        n += 2
    return n


def pfactors(n, primes = None):
    """
        Retourne la liste des facteurs premiers de n

    """
    factors = list()
    if primes is None:
        primes = eratosthene(n)
    for p in primes:
        if n % p == 0:
            factors.append(p)
#    if reduce(lambda a, b: a*b, factors, 1) != n:
#        print ("Error computing prime factors of {0}.".format(n))
    return factors


def largest_factor(n):
    """
        Retourne le plus grand facteur premier de n

    """

    if is_prime(n):
        return n

    j = int(round(sqrt(n))) + 1
    while (n % j != 0) or not is_prime(j):
        j -= 1
    return j


##### TRIANGULAR / PENTAGONAL / HEXAGONAL RELATIVE FUNCTIONS #####

def t(n):
    """
        Retourne le nè nombre triangonal

    """

    return n * (n + 1) / 2


def p(n):
    """
        Retourne le nè nombre pentagonal

    """

    return n * (3*n - 1) / 2


def is_pent(x):
    """
        Retourne true si x est un nombre pentagonal, false sinon

    """

    n = (sqrt(24*x + 1) + 1)/6.
    return n.is_integer()


def h(n):
    """
        Retourne le nè nombre hexagonal

    """

    return n*(2*n - 1)


def is_hexa(x):
    """
        Retourne true si x est un nombre hexagonal, false sinon

    """
    n = (sqrt(8*x + 1) + 1)/4.
    return n.is_integer()



##### MISC #####

def is_palind(n):
    """
        Retourne True si n est un nombre palindromique, 
        False sinon. 

    """

    l = str(n)
    i = 0
    while (i < (len(l)/2 + 1)):
        if (l[i] != l[len(l)-1-i]):
            return False
        i += 1
    return True
