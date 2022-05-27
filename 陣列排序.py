# -*- coding: utf-8 -*-
"""
Created on Fri May 27 19:49:04 2022

@author: MoXuan
"""

s = [(3, 7), (8, 9), (7, 6), (4, 9),(14, 3)]
result1 = sorted(s, key=lambda e: e[0])
result2 = sorted(s, key=lambda e: e[1])
print(result1)
print(result2)