#-*- coding: utf-8 -*-

from math import sqrt


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
