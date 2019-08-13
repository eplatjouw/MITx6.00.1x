# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 14:32:29 2019

@author: Emiel
"""
s = "azcbobobegghak1"
count = 0
for i in s:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u" :
        count += 1
print(" The number of vowels: "+ str(count))