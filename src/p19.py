#-*- coding: utf-8 -*-

from p import Problem

from toolbox import is_sunday

class p19(Problem):

    """ 
        You are given the following information, but you may prefer to do some research for yourself.

            1 Jan 1900 was a Monday.
            Thirty days has September,
            April, June and November.
            All the rest have thirty-one,
            Saving February alone,
            Which has twenty-eight, rain or shine.
            And on leap years, twenty-nine.
        
        A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

        How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)? 
        
    """

    def solve(self):
        y = 1901
        m = 0
        nb_sundays = 0
        while y <= 2000:
            while m < 12:
                if is_sunday(y,m):
                    nb_sundays += 1
                m += 1
            m = 0
            y += 1
        return nb_sundays
