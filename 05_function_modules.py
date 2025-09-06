"""Today(5 september 2025) we will discuss some baisc to advanced python programs based on:
- function
- Recursion
- modules & pip
- lambda
"""
# Q1: Write a function greet(name) that prints: Hello, [name].
def greet(name):
    print(f"Hello {name}")
greet("anuj pal")    


# Add a docstring explaining what the function does.
def greet(s):
    """this function will greet the user based on input given by the user"""
    print(f"Hello {s}")
greet("anuj")    

# Q2: Write a function add(a, b) that returns the sum of two numbers.
def add(a,b):
    return a+b
print(add(5,3))


# Q3: Create a global variable x = 10, and a function that prints x. Then create a local variable with 
# the same name inside the function and print both.
x = 10
def local_variable():
    x = 24
    print(x)
print(x)
local_variable()


# Q4: Write a function square(n) that returns the square of a number. Call it for 5 different inputs.
def square(n):
    return n ** 2
print(square(2))
print(square(6))
print(square(9))
print(square(15))
print(square(1))


# Q5: Write a function is_even(n) that returns True if a number is even, else False.
def is_even(n):
    if n % 2 == 0:
        print(f"yes {n} is an even number")
    else:
        print(f"{n} is not an even number")
is_even(5)        


# Q6: Use a lambda function to get the square of a number.
square = lambda x: x ** 2
print(square(5))


# Q7: Use a lambda function with map() to return the squares of numbers in a list.
list1 = [1,2,3,4,5]
result = map(lambda x: x**2,list1)
print(list(result))


# Q8: Use a lambda with filter() to get only the even numbers from a list.
list1 = [2,3,4,5,6,66,54,34,4,4,5,55]
result = filter(lambda x: x % 2 == 0,list1)
print(list(result))


# Q9: Import the math module and use it to calculate the square root of a number.
from math import sqrt
print(sqrt(16))

import math
print(math.sqrt(25))

import math as m
# print(m.sqrt(36))


# Q10: Use the random module to generate a random number between 1 and 100.
import random
print(random.randint(1,100))


# Q11: Write a recursive function to calculate the factorial of a number.
def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n-1)
print(fact(5))


# Q12: Write a recursive function to print the Fibonacci sequence up to n terms.
def fab(n):
    if n == 0 or n == 1:
        return n
    return fab(n-2) + fab(n-1)
for i in range(5):
    print(fab(i),end=",")


# Q13: Write a function reverse_string(s) using recursion (without slicing or loops).
def reverse_string(s):
    if len(s) <= 1:
        return s
    return reverse_string(s[1:]) + s[0]
print(reverse_string("anuj"))


# Q14: Create a small calculator module (say mycalc.py) with functions: add, subtract, multiply, divide. Then import it in another Python file and use it.
import mycalc #written in another file called mycalc.py
print("Addition:",mycalc.add(5,3))
print("Subtraction:",mycalc.sub(5,3))
print("Multiplication:",mycalc.multi(5,3))
print("Divion:",mycalc.div(5,3))


# Q15: Install an external module with pip (like pyfiglet) and write a program that prints your name in ASCII art.
import pyfiglet
ascii = pyfiglet.figlet_format("anuj pal")
print(ascii)