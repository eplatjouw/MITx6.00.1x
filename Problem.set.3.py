# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 18:13:08 2019

@author: Emiel
"""

s = 'azcbobobegghakl'
alphabet = "abcdefghijklmnopqrstuvwxyz"
x = ""

while len(s) > 0:
    temp = ""
    print(s)
    count = 0
    for i in range(len(alphabet)):
        if s[count] == alphabet[i]:
            temp = temp + str(s[count])
            count += 1
            print(temp)
            if s[len(s)-1] == alphabet [i]:
                break
    if len(temp) > len(x):
        x = temp
    if x[len(x)-1] == temp[0]:
        x = x + temp
    s = s[len(temp):]
print("Longest substring in alphabetical order is: "+ x)            
            
   
        
        
           
        