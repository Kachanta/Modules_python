# -*- coding: utf-8 -*-
"""
Created on Wed May 31 07:46:08 2023

@author: user
"""

class Computer:
    
    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram
        # print("in init")
    
    def config(self):
        print('PC ram:',self.ram, 'cpu Type:', self.cpu)

com1 = Computer("ryzen3", "16gb")
com2 = Computer("core i7", "32gb")

#Computer.config(com1)

com1.config()
com2.config()