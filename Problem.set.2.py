# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 14:38:48 2019

@author: Emiel
"""

s = 'azcbobobegghakl'
r=len(s)
count = 0

for i in range(r):
    if s[i:i+3] == "bob":
        count += 1
        
print("Number of times bob occurs is: " + str(count))
