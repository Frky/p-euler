#-*- coding: utf-8 -*-

from p import Problem

from toolbox import next_prime


class Node(object):

    def __init__(self, vals):
        self.vals = vals
        self.weight = sum(vals)
        self.children = list()

    def generate_children(self):
        for i, v in enumerate(self.vals):
            child_vals = list(self.vals)
            child_vals[i] = next_prime(v)
            self.children.append(Node(child_vals))

class p60(Problem):

    """
        The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes 
        and concatenating them in any order the result will always be prime. For 
        example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four 
        primes, 792, represents the lowest sum for a set of four primes with this 
        property.

        Find the lowest sum for a set of five primes for which any two primes 
        concatenate to produce another prime.

    """

    def explore(self, tree, max_sum):
        print tree.vals
        if tree.weight >= max_sum:
            return
        tree.generate_children()
        for child in tree.children:
            self.explore(child, max_sum)


    def solve(self):
        tree = Node([2, 3])
        self.explore(tree, 7 + 11)
        return 0

