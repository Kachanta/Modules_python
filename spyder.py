# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 06:57:25 2023

@author: user
"""
class Spyder:
    def execute(self):
        print("compile")
        print("runing")

class MyIde:
    def execute(self):
        print("erro correction")
        print("Spelling checks")
        print("compile")
        print("run")
        
class Laptop:    

    def code(self, ide):
        ide.execute()
        
ide1 = Spyder()
lap1 = Laptop()
ide2 = MyIde()

lap1.code(ide2)