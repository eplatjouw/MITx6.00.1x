# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 11:40:51 2019

@author: Emiel
"""
## Week 1: Part 1
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
    # not 
    # and
    # or

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


## Week 1: Part 2
#Strings
    # Single or Double Quotes
hi = "hello there"
greet = 'eric' 
foo = " This isn't right " # Double quotes handy if ' is used in string
greetings = hi + greet
greetings
greetings = hi + " " + greet
greetings

# Operations on strings
"hi" + " eric"
3 * "eric"
len("eric")
len("hi there")
"eric"[1]
"eric"[0] # starts at 0, first letter is found by using 0
greet[0]
greet[1:3] # starts and includes 1 (second char) but does not include 3th (4th char in the string)
greet[:3]
greet[1:]
greet[:]    # copy, not original


# Input/Output
x = 1
print(x)
x_string = str(x) # convert int into string
print("my fav num is", x , ".", " x =", x)
print("my fav num is "+ x_string + "." + " x = " + x_string)

text = input("Type anything... ")
print(text)
text
type(text)

num = int(input(" Type a number... "))
print(5*num)

# Loops
    # While loop
n = input("You are in the Lost Forest. Go left or right? ")
while n == "right":
    n = input("You are in the Lost Forest. Go left or right? ")
print("You got out of the Lost Forest")


n = 0
while n < 5:
    print(n)
    n = n + 1
    
n = 0
while n < 5:
    print(n)
    n += 1
    
    # For loop
for n in range(5):
    print(n)

mysum = 0
for i in range(7, 10): # from 7 until 10 including 7 but not including 10
    mysum += i
print(mysum)

mysum = 0
for i in range(5, 11, 2): # from 5 to 11 by increments of 2
    mysum += i
print(mysum)

    # Break
mysum = 0
for i in range(5, 11, 2): # from 7 until 10 including 7 but not including 10
    mysum += i
    if mysum == 5:
        break
print(mysum)


#Iterations
x = 3
ans = 0
itersLeft = x
while (itersLeft != 0):
    ans = ans + x
    itersLeft = itersLeft - 1
print(str(x) + '*' + str(x) + ' = ' + str(ans))


# Class of Algorithms
    # Guess and Check
        # Cube root
x = int(input("Enter an integer: "))
ans = 0
while ans**3 < x:
    ans += 1
if ans**3 !=x:
    print(str(x) + " is not a perfect cube")
else:
       print("Cube root of " + str(x) + " is " + str(ans))     


x = int(input("Enter an integer: "))
ans = 0
while ans**3 < abs(x): # abs() takes absolute value
    ans += 1
if ans**3 != abs(x):
    print(str(x) + " is not a perfect cube")
else:
    if x < 0:
        ans = -ans
    print("Cube root of " + str(x) + " is " + str(ans))  
    

cube = 28
for guess in range(cube+1):
    if guess**3 == cube:
        print("Cube root of " + str(cube) + " is " + str(guess))
        
cube = -27
for guess in range(abs(cube)+1):
    if guess**3 >= abs(cube):
        break
if guess**3 != abs(cube):
         print(str(cube) + " is not a perfect cube.")
else:
    if cube < 0:
        guess = -guess
    print("Cube root of " + str(cube) + " is " + str(guess))