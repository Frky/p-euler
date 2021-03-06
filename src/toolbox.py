#-*- coding: utf-8 -*-

import random
from math import sqrt, floor, ceil
from fractions import gcd

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

    assert n >= 1
    if n == 1:
        return False
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


def smallest_pfactor(n):
    """
        Retourne le plus petit facteur premier de n

    """

    if n % 2 == 0:
        return 2
    j = 3
    while (n % j != 0) or not is_prime(j):
        j += 2
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


def phi(n, table):
    """
        Retourne le nombre de nombres inférieurs à n premiers avec n
        /!\ table doit contenir l'ensemble des valeurs de phi(i)
        pour tout 1 < i < n

    """
    if n == 1:
        return 1
    elif is_prime(n):
        return n - 1
    else:
        m = smallest_pfactor(n)
        if n/m % m == 0:
            return table[n/m] * m
        else:
            return table[n/m] * table[m]


##### TRIANGULAR / PENTAGONAL / HEXAGONAL RELATIVE FUNCTIONS #####

def t(n):
    """
        Retourne le nè nombre triangonal

    """

    return n * (n + 1) / 2


def is_triang(x):
    """
        Retourne true ssi x est un nb triangulaire

    """

    n = (sqrt(8 * x + 1) - 1) / 2.
    return n.is_integer()


def is_cube(x):
    """
        Retourne true ssi x est le carré d'un entier
    
    """
    
    n = x**(1/3.)
    return round(n) ** 3 == x


def is_square(x):
    """
        Retourne true ssi x est le carré d'un entier
    
    """
    
    n = sqrt(x)
    return n.is_integer()


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


def hp(n):
    """
        Retourne le nè nombre heptagonal

    """

    return n * (5*n - 3) / 2


def is_hepta(x):
    """
        Retourne true ssi x est hetpagonal

    """
    
    n = (sqrt(40 * x + 9) + 3) / 10.
    return n.is_integer()


def o(n):
    """
        Retourne le nè nombre octagonal

    """

    return n * (3 * n - 2)


def is_octa(x):
    """
        Retourne true ssi x est octagonal

    """

    n = (sqrt(3 * x + 1) + 1) / 3.
    return n.is_integer()

##### MISC #####

def int_length(n):
    """
        Retourn la longueur du nombre n

    """
    if n>=0 :
        return len(str(n)) 
    else :
        return len(str(n)) - 1

def sum_of_digits(n):
    """
        Retourne la somme des chiffres composant n

    """
    return sum([int(c) for c in str(n)])

def fibonacci(n, prev_terms=None):
    """
        Retourne le nè terme de la suite de Fibonacci

    """
    a = 1
    b = 1
    nb_terms = 2
    if prev_terms != None:
        nb_terms = len(prev_terms)
        if nb_terms > n-1:
            return prev_terms[n-1]
        else:
            a = prev_terms[nb_terms - 2]
            b = prev_terms[nb_terms - 1]
    while nb_terms < n:
        b = a + b
        a = b - a 
        if prev_terms != None:
            prev_terms.append(b)
        nb_terms += 1
    return b


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


def lowest_perm(n):
    """
        Retourne la plus petite permutation de n (éventuellement
        avec des zéros au début)

    """
    s = [int(x) for x in list(str(n))]
    s = sorted(s)
    return int("".join([str(x) for x in s]))


def is_permutation(m, n):
    """
        Retourne true ssi n est une permutation de m, c'est-à-dire
        ssi m et n sont composés exactement des mêmes chiffres.

    """

    if len(str(n)) != len(str(m)):
        return False

    for c in str(n):
        if c not in str(m) or str(n).count(c) != str(m).count(c):
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


def reverse(n):
    """
        Retourne l'entier n lu de droite à gauche.
        Par exemple, pour n = 375, reverse(n) retourne 573.

    """

    return int("".join([str(n)[-i] for i in xrange(1, len(str(n)) + 1)]))


def is_lychrel(n):
    """
        Retourne vrai ssi n est un nombre de Lychrel (pour n <= 10000)
        Cette fonction prend pour hypothèse qu'un nombre est de Lychrel
        s'il n'a toujours pas produit de nombre palindromique après 50 
        itérations.

    """

    n += reverse(n)
    for i in xrange(1, 51):
        if is_palind(n):
            return False
        n += reverse(n)
    return True


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

class Tree:

    def __init__(self, filename):
        self.data = []
        self.n = -1
        self.parse(filename)
        self.max_sum = [-1] * len(self.data)

    def parse(self, filename):
        with open(filename, "r") as f:
            for line in f.readlines():
                self.data += [int(x) for x in line[:-1].split(" ")]
                self.n += 1

    def node(self, i, j):
        if (j > i):
            return None
        return self.data[i * (i + 1) / 2 + j]

    def depth(self):
        return self.n

    def set_sum(self, i, j, s):
        self.max_sum[i * (i + 1) / 2 + j] = s

    def sum_path(self, i, j):
        return self.max_sum[i * (i + 1) / 2 + j]

    def compute_path(self, i, j):
        if i == self.depth():
            self.set_sum(i, j, self.node(i, j))
        else:
            self.set_sum(i, j, 
                            self.node(i, j) + max(self.sum_path(i + 1, j), 
                                                    self.sum_path(i + 1, j + 1)
                                                )
                            )

    def __str__(self):
        s = ""
        for i in xrange(self.depth() + 1):
            for j in xrange(i + 1):
                s += str(self.node(i, j)) + " "
            s += "\n"
        return s


    def max_path(self):
        k = self.depth()
        while (k != 0):
            for j in xrange(0, k + 1):
                self.compute_path(k, j)
            k = k - 1
        self.compute_path(0, 0)
        return self.sum_path(0, 0)


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


### FRACTIONS ###

class Fraction:
    """
        Classe de fractions rationnelles.

    """
    
    def __init__(self, num, den=1):
        self.num = num
        self.den = den
    
    def __str__(self):
        return "{0}/{1}".format(self.num, self.den)


    def __add__(self, other):
        res = Fraction(self.num * other.den + other.num * self.den, other.den*self.den)
        res.reduce()
        return res
        

    def __invert__(self):
        return Fraction(self.den, self.num)

    def reduce(self):
        self.num /= gcd(self.num, self.den)
        self.den /= gcd(self.num, self.den)


def quad_step(n, p, q):
    """
        Calcule une étape de la décomposition en fraction continue de
        la racine carrée de n

    """
    a = floor((sqrt(n) + p) / q)
    p -= q * a
    return a, -p, (n - p*p)/q

def continuous_fraction(n):
    """
        Calcule la décomposition en fraction continue de la racine carrée 
        de n

    """
    p = 0
    q = 1
    a0, p, q = quad_step(n, p, q)
    a0 = int(a0)
    a = list()
    while len(a) == 0 or floor(a[-1]) != 2*a0:
        a1, p, q = quad_step(n, p, q)
        a.append(int(a1))
    return (a0, a)

def seq_to_frac(seq):
    """
        A partir d'un développement en fraction continue, 
        calcule la fraction réduite correspondante

    """
    res = Fraction(seq.pop(-1))
    while len(seq) > 0:
        val = Fraction(seq.pop(-1))
        res = val + ~res
    return res 
