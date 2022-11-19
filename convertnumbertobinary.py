# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 19:27:43 2022

@author: melik
"""
reverse=0
n=int(input("enter number:"))
while n!=0:
    reverse=reverse*10+(n%2)
    n=n//2
reverse=str(reverse)
duz=reverse[::-1]
print(duz)
    
    