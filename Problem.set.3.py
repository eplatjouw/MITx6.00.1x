# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 18:13:08 2019

@author: Emiel
"""

s = 'azcbobobegghakl'
r=len(s)
alphabet = "abcdefghijklmnopqrstuvwxyz"
x = ""
temp = ""
while r > 0:
    s = s[len(temp):]
    print(s)
    count = 0
    temp = ""
    for i in range(len(alphabet)):
        if s[count] == alphabet[i]:
            temp = temp + str(s[count])
            count += 1
            print(temp)
    if len(temp) > len(x):
        x = temp
    if x[len(x)-1] == temp[0]:
        x = x + temp
print("Longest substring in alphabetical order is: "+ x)            
            
   
        
        
           
        