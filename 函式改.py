# -*- coding: utf-8 -*-
"""
Created on Fri May 20 19:29:43 2022

@author: user
"""

s=[(3, 4), (2, 4), (5,3)]

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

def clac(w,h):
    return w*h

def calAll(conta, func):
    for r in conta:
        print(func(r[0], r[1]), end='')
        
calAll(s, clac)
