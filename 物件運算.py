# -*- coding: utf-8 -*-
"""
Created on Fri May 27 19:49:04 2022

@author: MoXuan
"""

class mathops():
    pi = 3.14159926
    def add(self, x, y):
        return x+y
    def multiply(self, x, y):
        return x*y


class printops():
    str = 'abc'
    def printstr(self, in_str):
        print(f'{self.str}={in_str}')
        
mathobj1 = mathops()
mathobj2 = mathops()
mathobj3 = mathops()

printobj = printops()
printobj.printstr('123')

print(mathobj1.pi)
print(mathobj2.add(1, 2))
print(mathobj3.multiply(2, 3))