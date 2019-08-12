# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 11:40:51 2019

@author: Emiel
"""
# Type of object
type(5)
type(3.5)

# Convert int to float and vice versa
int(5.8)
int(5.2)
float(3)
float(5)

# Arithmetic Operations
6+5 # sum
5-6 # difference
9*7 # product
2/5 # division
6//4 # int division, result is int, quotient without remainder
6%4 # the remainder when i (6) is divided by j (4)
9**2 # to the power

# Operations precedece
    # ( ) Parentheses
    # ** to the power
    # * multiplication
    # / division
    # + and -
    # left to right execution as appears in expression
    
    
# Binding Variables and Values using =
pi = 3.14159
pi_approx = 22/7

# Shorthanding incrementing
radius = 2.2
radius = radius +1
    # is the same as
radius += 1

# Comparison Operators
5>2
4>=8
2<4
4<=9
5==5
4==5
4!=9

# Logic Operators on Bools
not 
and
or

# Example of a test
x = int(input('Enter an integer'))
if x%2 == 0:
    print('')
    print('even')
else:
    print('')
    print('Odd')
print('Done with conditional')

# Nested Conditionals
x = int(input('Enter an integer'))
if x%2 == 0:
   if x%3 == 0:
       print ('Divisable by 2 and 3')
   else:
       print('Divisable by 2 and not by 3')
elif x%3 == 0:
    print('Divisible by 3 and not by 2')

# Compound Booleans
x = int(input('Enter an integer'))
y = int(input('Enter an integer'))
z = int(input('Enter an integer'))
if x < y and x < z:
    print('x is least')
elif y < z:
    print('y is least')
else:
    print('z is least')
    
    
x = float(input('Enter a number for x: '))
y = float(input('Enter a number for y: '))
if x == y:
    print("x and y are equal")
    if y != 0:
       print ('therefore, x / y is ', x/y)
elif x < y:
    print('x is smaller')
else:
       print("y is smaller")
print("Thanks!")