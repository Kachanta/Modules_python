# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 06:33:32 2023

@author: user
"""

class A:
    
    def __init__(self):
        print("A init")
    
    def feature1(self):
        print("feature one is working ")
        
class B(A):
    
    def __init__(self):
        super().__init__()
        print("B init")
        
    def feature2(self):
        print("feature two is working ")
        

class C(B):
    
    def __init__(self):
        super().__init__()
        print("C init")
        
    def feature3(self):
        print("feature three is working ")
    
a1 = C()

a1.feature1()