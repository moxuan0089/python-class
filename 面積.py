# -*- coding: utf-8 -*-
"""
Created on Fri May 20 19:10:41 2022

@author: user
"""

def clac(w, h, d=1):
    if(w<=0 or h<=0):
        return
    return [(w*h,w*h*d,(w+h)*2), '正方形'if w==h else '長方形']
    
((y, z, w),c) = clac(2, 2, 6)

print(y,c)
print(z,c)
print(w,c)