#-*- coding: utf-8 -*-

import random
from math import sqrt, ceil


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


def decompose(n, primes = None):
    """
        Retourne la décomposition en facteurs premiers de n, 
        sous la forme d'une liste de tuples (facteur, puissance)

    """
    decomp = list()
    if primes is None:
        primes = eratosthene(n)
    for p in primes:
        power = 0
        while n % p ** power == 0:
            power += 1
        power -= 1
        if (power > 0):
            decomp.append((p, power))
    if reduce(lambda a, b: a*(b[0] ** b[1]), decomp, 1) != n:
        print ("Error computing prime factors of {0}.".format(n))
    return decomp



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
    return factors


def largest_pfactor(n):
    """
        Retourne le plus grand facteur premier de n

    """

    if is_prime(n):
        return n

    j = int(round(sqrt(n))) + 1
    while (n % j != 0) or not is_prime(j):
        j -= 1
    return j


def divisors(n):
    """
        Retourne l'ensemble des diviseurs de n (premiers ou non), n inclus

    """
    div = list()
    div.append(1)
    for i in xrange(2, int(ceil(sqrt(n)))):
        if (n % i == 0):
            div.append(i)
            if (i*i != n):
                div.append(n/i)
    div.append(n)
    return div 

def proper_divisors(n):
    """
        Retourne l'ensemble des diviseurs de n (premiers ou non), n exclus

    """
    return divisors(n)[:-1]

def nb_divisors(n):
    """
        Retourne le nombre de facteurs de n

    """
    nb_fact = 2
    for i in xrange(2, int(ceil(sqrt(n)))):
        if (n % i == 0):
            if (i*i == n):
                nb_fact += 1
            else:
                nb_fact += 2
    
    return nb_fact


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


def squareSum(n):
    """ 
        Retourne le carré de la somme des entiers allant de 1 à n 
    
    """
    
    return ((n*(n+1))/2)**2


def sumSquare(n):
    """ 
        Retourne la somme des carrés des entiers allant de 1 à n 
    """
    
    return sum([i**2 for i in xrange(1, n+1)])


def is_pythagorean(a, b, c):
    """
        Retourne vrai ssi a^2 + b^2 == c^2

    """
    return a**2 + b**2 == c ** 2


def is_permutation(m, n):
    """
        Retourne true ssi n est une permutation de m, c'est-à-dire
        ssi m et n sont composés exactement des mêmes chiffres.

    """

    if len(str(n)) != len(str(m)):
        return False

    for c in str(n):
        if c not in str(m):
            return False

    return True


def factorial(n):
    if n <= 0:
        return 1
    else:
        return n * factorial(n - 1)


def combination(r, n):
    """
        Retourne C(r, n), c'est-à-dire le nombre de combinaisons possibles
        de r éléments tirés parmi n.

    """

    return factorial(n) / (factorial(r) * factorial(n - r))



### SYRACUSE ###
def syracuse(n):
    """
        Retourne la séquence des termes de la suite de Syracuse de premier 
        terme n jusqu'à 1

    """
    
    if n <= 0:
        return list()
    syr = [n]
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3*n + 1
        syr.append(n)
    return syr


def syracuseLength(n, data=None):
    """
        Retourne le nombre de termes de la suite de Syracuse de premier terme n

    """
    
    if n <= 0:
        return -1
    elif data != None and len(data) > n and data[n] != -1:
        return data[n]
    elif n == 1:
        return 1
    elif n % 2 == 0:
        return 1 + syracuseLength(n / 2, data)
    else:
        return 1 + syracuseLength(3*n + 1, data)


### GRAPH ANT PATH RELATIVE FUNCTIONS ###

class Node:

    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


def max_path(tree, i):
    """
        À partir du noeud i ne l'arbre tree, calcule le chemin le plus long jusqu'à une feuille.

    """
    if (i >= len(tree)):
        return 0
    k = 0
    l = 0
    # recherche du début de la ligne suivante
    while (i + k < len(tree) and tree[i + k] != "."):
        k += 1
    # recherche du début de la ligne courante
    while ( i-l > 0 and tree[i - l - 1] != "."):
        l += 1
    if i + k == len(tree):
        # on retourne la valeur de la feuille
        return int(tree[i])
    else:
        #        print("{0} | k: {1} - l: {2}".format(tree[i],tree[i + k + 1 + l],tree[i + k + l + 2]))
        # la ligne suivante commence à tree[i + k + 1]
        # les fils de i sont donc à tree[i + k + 1 + l + 1] et tree[i + k + 1 + l + 2]
        return int(tree[i]) + max(max_path(tree, i + k + l + 1), max_path(tree, i + k + l + 2))


### CALENDAR RELATIVE FUNCTIONS ###

monthLast = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
leapMonthLast = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    """
        Retourne vrai ssi l'année passée en paramètre est bissextile.

    """
    if (year % 4 == 0):
        if (year % 100 == 0):
            if (year % 400 == 0): 
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def first_day(year):
    """
        Retourne le premier jour de l'année passée en paramètre sous forme d'un entier 
        de 0 à 6 (0 correspond à un dimanche).

    """
    i = 1900
    day = 1
    while (i < year):
        if is_leap(i):
            day += 366
        else:
            day += 365
        i += 1
    return day % 7


def is_sunday(year, month):
    """
        Retourne vrai ssi le premier jour du mois month de l'année year est un dimanche.

    """
    i = 0
    days = 0
    if is_leap(year):
        while i < month:
            days += leapMonthLast[i]
            i += 1
    else:
        while i < month:
            days += monthLast[i]
            i += 1
    return (first_day(year) + days) % 7 == 0

