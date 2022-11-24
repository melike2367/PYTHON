# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 13:58:06 2022

@author: melik
"""

def solution(array_a, array_b):
    x=0
    lst=[]
    for x in range(0,len(array_a)):
        lst.append((abs(array_a[x]-array_b[x])**2))
        
        x=x+1
    return sum(lst)/len(lst)