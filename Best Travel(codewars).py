# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 14:59:16 2022

@author: melik
"""

from itertools import combinations
def choose_best_sum(t, k, ls):
    a=list(combinations(ls,k))
    max=0
    for x in a:
        while sum(x)<=t:
            if sum(x)>max:
                max=sum(x)
            else:
                break
    if max==0:
        return 
    else:
        return max