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



## Abstraction, decomposition and functions
# Decomposition: Break problem into different, self-contained pieces
# Abstraction: Suppress details of method to computesomething from use of that computation

# Functions:
    # Not run until they are called or invoked in a program
    # has a name
    # has parameters (0 or more)
    # has a docstring ( optional but recommended)
    # has a body

def is_even (i):
    """             
    Input: i, a positive int  
    Returns True if i is even, otherwise False
    
    """
    print("hi")
    return i%2 == 0 # return: ready to stop computation, give back value of following expressions

is_even(3)
is_even(2)


def f(x):
    x = x + 1
    print("in f(x): x =", x)
    return  x
x = 3
z = f(x)

    # If no return Python returns the value none
def is_even (i):
    """             
    Input: i, a positive int  
    Does not return anything
    
    """
    i%2 == 0

is_even(2)

# Return vs Print
# Return:
    # Only has meaning inside the function
    # Only one return function executed inside a function
    # code inside function but after return statement not executed
    # has a value associated with it, given to function caller
# Print:
    # Print can be used outside functions
    # can execute many print statements inside a functions
    # code inside function can be executed after a print statement
    # has a value associated with it, outputted to the console
    
def func_a():
    print("inside func_a")
def func_b(y):
    print("inside func_b")
    return y
def func_c(z):
    print("inside func_c")
    return z()
print(func_a())
print(5 + func_b(2))
print(func_c(func_a))

# Inside a function, can access a variable defined outside
# inside a function, cannot modify a variable defined outside
def f(y):
    x = 1
    x += 1
    print(x)
x=5
f(x) # prints 2 (function returns x from inside function env)
print(x) # prints 5 (prints x as defined in global env)

def g(y):
    print(x)
    print(x+1)
x = 5
g(x)
print(x)

def h(y):
    x = x + 1 # UnboundLocalError
x = 5
h(x)
print(x)


def g(x):
    def h():
        x = "abc"
    x = x + 1
    print("in g(x): x =", x)
    h()
    return x

x = 3
z = g(x)


# Keyword Arguments and Default Values
def printName(firstName, lastName, reverse):
    if reverse:
        print(lastName + ", "+ firstName)
    else:
        print(firstName, lastName)
        
printName("Eric", " Grimson", False)
printName("Eric", " Grimson", True)
printName("Eric", " Grimson", reverse = False)
printName("Eric", lastName = " Grimson", reverse = False)
printName( lastName = " Grimson",firstName = "Eric", reverse = False)
       
def printName(firstName, lastName, reverse = False): # Set Default Value
    if reverse:
        print(lastName + ", "+ firstName)
    else:
        print(firstName, lastName)  

printName("Eric", " Grimson")
printName("Eric", " Grimson", True)


# Specifications
# a contract between implementer of a function and the clients who will use it
    # Assumption: conditions must be met by client of function; typically constraints on values of parameters
    # Guarantees: conditions that must be met by function, providing assumptions met
# Implemented with docstring
def is_even (i):
    """             
    Input: i, a positive int  
    Returns True if i is even, otherwise False
    
    """
    print("hi")
    return i%2 == 0


# Recursion
    # a programming technique where a function calls itself
    # goal is not have infinite recursion
        # must have 1 or more base cases
        # must solve the same problem on some other input with the goal of simplifying the larger problem

def mult_iter(a,b):  # multiplication of integers, iterative way
    result = 0
    while b > 0:
        result += a
        b -= 1
    return result

def mult(a, b): # multiplication of integers, recursive way
    if b == 1 :         # base case
        return a
    else:               # recursive step
        return a + mult(a, b-1) 

mult_iter(3,6)
mult(3,6)


def fact(n):    # Factorials recursive way
    if n == 1:
        return 1
    else:
        return n*fact(n-1)

print(fact(4))


# Inductive Reasoning
    # Mathematical Induction
    # To prove a statement indexed on integers is true for all values of n:
        # Prove it is true when n is smallest value (e.g. n = 0 or n = 1)
        # Then prove if it is true for an arbitrary value of n, also must be true for n + 1


# Towers of Hanoi
    # Looking at it recursively easy to write code which would otherwise be very difficult to see
def printMove(fr, to):
    print("move from "+ str(fr) + " to "+ str(to))

def Towers(n, fr, to, spare):
    if n == 1:
        printMove(fr, to)
    else:
        Towers(n-1, fr, spare, to)
        Towers(1, fr, to ,spare)
        Towers(n-1, spare, to, fr)
        
print(Towers(4, "P1", "P2", "P3"))


# Fibonacci
    # Multiple base cases
def fib(x):
    """
    assumes x an int >= 0
    returns Fibonacci of x
    
    """
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)
fib(0)
fib(1)
fib(2)
fib(3)
fib(4)
fib(15)    


# Recursion on non-numerics
    # "Able was I, ere I saw Elba" -> "ablewasiereisawelba"
    # isPalindrome("ablewasiereisawelba")
    # is same as
        # "a" == "a" and
        # isPalindrome("blewasiereisawelb)
        
def isPalindrome(s):
    
    def toChars(s):
        s=s.lower()
        ans = ""
        for c in s:
            if c in "abcdefghijklmnopqrstuvwxyz":
                ans = ans + c
        return ans
    
    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])
    
    return isPal(toChars(s))

isPalindrome("eve")
isPalindrome("Able was I, ere I saw Elba")


# Files and  Modules
    # Module is a file with certain definitions, functions and more
import circle
print(pi)
pi = 3
print(pi)
print(circle.pi)
print(circle.area(3))
print(circle.circumference(3))

from circle import *
print(pi)
print(area(3))

    # Save work for later use
        # every OS own way of handling files; Python provides OS independant mean to access files
        # using a file handle
nameHandle = open("kids", "w")
        # creates file named kids and returns handle which we can name and thus reference
        # w indicates file is to opened for writing info
        
nameHandle = open("kids", "w")
for i in range(2):
    name = input("Enter name: ")
    nameHandle.write(name + '\n')
nameHandle.close()

nameHandle = open("kids", "r") # r for reading into file
for line in nameHandle:
   print(line)
nameHandle.close()