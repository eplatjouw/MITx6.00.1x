# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 11:42:27 2019

@author: Emiel
"""

# Strings
    # slice strings using [start:stop:step]
s="abcdefgh"
s[::-1]  # reverse string, evaluates to "hgfedcba"
s[3:6]
s[-1]    # evalutes to "h"
    # Stings are immutable
s="hello"
s[0] = "y" # gives error
s = "y"+ s[1:len(s)] # allowed as s is a new object

    # Strings and Loops
s = "abcdefghij"
for index in range(len(s)):
    if s[index] == "i" or s[index] == "u":
        print("There is an i or a u")

for char in s:                      # The same as the above!
    if char == "i" or char == "u":
        print("There is an i or u")
        

an_letters = "aefhilmnorsxAEFHILMNORSX"
word = input("I will cheer for you! Enter a word: ")
times = int(input("Enthusiasm level (1-10): "))
i = 0

while i < len(word):
    char = word[i]
    if char in an_letters:
        print("Give me an " + char + "! " + char)
    else:
        print("Give me a " + char + "! " + char)
    i += 1
print("What does that spell?")
for i in range(times):
    print(word, "!!!")
    

# Approximate Solutions
    # Define close enough, define increments
    # Cube root example
cube = 29
epsilon = 0.01
guess = 0.0
increment = 0.001      # play with increments
num_guesses = 0
while abs(guess**3 - cube) >= epsilon and guess <= cube:
    guess += increment
    num_guesses += 1
print('num_guesses =', num_guesses)
if abs(guess**3 - cube) >= epsilon:
    print("Failed on cube root of", cube)
else:
    print(guess, "is close to the cube root of", cube)
    

# Bisection Search
    # At each stage you lose half the values
    # Square root example
x = 25
epsilon = 0.01
numGuesses = 0
low = 1.0
high = x
ans = (high + low)/2.0

while abs(ans**2 - x) >= epsilon:
    print('low = ' + str(low) + " high = " + str(high) + " ans = " + str(ans))
    numGuesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print("numGuesses = " + str(numGuesses))
print(str(ans) + " is close to square root of " + str(x))

    # Cube root example
x = 27
epsilon = 0.01
numGuesses = 0
low = 1.0
high = x
ans = (high + low)/2.0

while abs(ans**3 - x) >= epsilon:
    print('low = ' + str(low) + " high = " + str(high) + " ans = " + str(ans))
    numGuesses += 1
    if ans**3 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print("numGuesses = " + str(numGuesses))
print(str(ans) + " is close to square root of " + str(x))


# Convert integers in binary
num = int(input("Give me an integer to convert in binary form: "))
if num < 0:
    isNeg = True
    num = abs(num)
else:
    isNeg = False
result = ''
if num == 0:
    result = '0'
while num > 0:
    result = str(num%2) + result
    num = num//2
    print(result)
if isNeg:
    result = '-' + result
print(result)

# Conver floats in binary
    # Convert to integer by miltiplying, apply same code and convert back 
    # by dividing by same number
x = float(input("Give me a decimal number between 0 and 1 to convert in binary form: "))

p = 0
while ((2**p)*x)%1 != 0:
    print("Remainder = " + str((2**p)*x - int((2**p)*x)))
    p += 1

num = int(x*(2**p))

result = ''
if num == 0:
    result = '0'
while num > 0:
    result = str(num%2) + result
    num = num//2

for i in range(p - len(result)):
    result = "0" + result

result = result[0:-p] + "." + result[-p:]
print("The binary representation of the decimal " + str(x) + " is " + str(result))


# Newton-Raphson
    # Another way of generating guesses
    # If g is a good guess of a square root, you can get an even better guess
    # by substracting that guess by the polynomial of g divided by the derivative
    # of the polynomial of g
epsilon = 0.01
y = 54.0
guess = y/2.0
numGuesses = 0

while abs(guess*guess - y) >= epsilon:
    numGuesses += 1
    guess = guess - (((guess**2) - y) / (2*guess))
print("numGuesses = " + str(numGuesses))
print("Square root of " + str(y) + " is about " + str(guess))