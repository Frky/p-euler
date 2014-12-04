#-*- coding: utf-8 -*-

from p import Problem

class p22(Problem):

    """ 
        Using names.txt (right click and 'Save Link/Target As...'), a 46K text 
        file containing over five-thousand first names, begin by sorting it into 
        alphabetical order. Then working out the alphabetical value for each 
        name, multiply this value by its alphabetical position in the list to 
        obtain a name score.

        For example, when the list is sorted into alphabetical order, COLIN, 
        which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
        So, COLIN would obtain a score of 938 * 53 = 49714.

        What is the total of all the name scores in the file? 
        
    """

    def __init__(self, id):
        self.names = list()
        return super(p22, self).__init__(id)

    def parse_names(self, file_name):
        """
            Parse le fichier contenant les noms à utiliser.
            Après cette fonction, self.names contient une liste
            des noms contenus dans le fichier sous forme de chaine
            de caractère.

        """
        with open(file_name, "r") as names:
            names_parsed = names.readline()
            names_parsed = names_parsed.replace("\"", "")
            names_parsed = names_parsed.replace(" ", "")
            self.names = names_parsed.split(",")

    def sort_names(self):
        """
            Trie la liste des noms par ordre alphabétique

        """
        self.names.sort()

    def value(self, name):
        """
            Renvoie la valeur alphabétique d'un nom

        """
        return sum([ord(c) - ord('A') + 1 for c in name])

    def solve(self):
        self.parse_names("data/p22.txt")
        self.sort_names()
        res = 0
        for rank, name in enumerate(self.names):
            res += (rank + 1) * self.value(name)
        return res
