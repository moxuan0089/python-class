# -*- coding: utf-8 -*-
"""
Created on Fri May 20 19:42:27 2022

@author: user
"""

def add(x):
    v=0
        
    for i in range(1, x+1):
        v+=i
            
    return v

def mul(x):
    v=1
    for i in range(1, x+1):
        v*=i
    return v

def calAll(conta, func):
    
    return func(conta)
print(calAll(10, add))
print(calAll(5, mul))