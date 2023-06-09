# -*- coding: utf-8 -*-
"""
Created on Wed May 31 11:52:54 2023

@author: user
"""
class car:
    
    wheel = 4
    
    def __init__(self):
        self.mil = 10
        self.com = "BMW"
    
c1 = car()
c2 = car()

c1.com = "Meceded"
c1.wheel = 54
car.wheel = 8

print(c1.com, c1.mil, c1.wheel)
print(c2.com, c2.mil, c2.wheel)

