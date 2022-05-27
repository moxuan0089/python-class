# -*- coding: utf-8 -*-
"""
Created on Fri May 27 19:17:40 2022

@author: MoXuan
"""

def math(val, gate):
    return gate(val)

a= lambda x: list(range(1,x+1))
    
    
        

print(math(3,a))