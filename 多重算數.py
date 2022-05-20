# -*- coding: utf-8 -*-
"""
Created on Fri May 20 19:49:32 2022

@author: user
"""

def add(x):
    v=0
        
    for i in x:
        v+=i
            
    return v

def mul(x):
    v=1
    for i in x:
        v*=i
    return v

def no(x):
    v=0
    for i in x:
        v-=i
    return v

def calAll(conta, func):
    
    return func(conta)

x=[1,2,5]
funcs=[add,mul,no]
for f in funcs:
    print(calAll(x,f))