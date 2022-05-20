# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
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

z = add(10)
y = mul(5)
print(z)
print(y)