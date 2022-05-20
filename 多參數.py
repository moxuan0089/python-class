# -*- coding: utf-8 -*-
"""
Created on Fri May 20 19:57:55 2022

@author: user
"""

def calc(w, *hs):
    for h in hs:
        w=w*h
    return w

y=calc(3, 4, 2, 6, 7)
print(y)