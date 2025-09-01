"""Today(1 september 2025) we will discuss some baisc to advanced python programs based on (Syntax + Input/Output) using only:
- print()
- input()
- variables
- basic math operators
"""

#Q1: Take your name and print a greeting
name = input("Enter your name:")
print("Hello",name,"welcome to this python course")

#Q2: Take two numbers and print their sum
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
print("Sum of",num1,"and",num2,"is:",num1+num2)

#Q3: Ask age and print message
age = int(input("Enter your age:"))
print("Hey you are",age,"years old!")

#Q4: Take a number and print its double
num = int(input("Enter a number:"))
print(2*num,"is double of",num)
          
#Q5: Take two words and join them
word1 = input("Enter first word:")
word2 = input("Enter second word:")
print(word1+" "+word2)

#Q6: Take two numbers and print sum,difference,product,quotient
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
sum = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1 / num2
print("Sum is:",sum)
print("Difference is:",difference)
print("Product is:",product)
print("Quotient is:",quotient)

#Q7: Reactangle Area (length * breadth)
length = int(input("Enter length of Reactangle:"))
breadth = int(input("Enter breadth of Reactangle:"))
print("Area of Reactangle is:",length * breadth)

#Q8: Circle area (πr², π=3.14)
r = int(input("Enter radius of circle:"))
π = 3.14
Area = π * (r * r)
print("Area of cirlce is:",Area)

#Q9: Average of 3 marks
mark1 = int(input("Enter your 1st marks:"))
mark2 = int(input("Enter your 2nd marks:"))
mark3 = int(input("Enter your 3rd marks:"))
print("Average marks are:",(mark1+mark2+mark3)/3)

#Q10: Full name from first and last
first = input("Enter your first name:")
last = input("Enter your last name:")
print("Your full name is:",first+" "+last)

#Q11: Simple interest (P×R×T / 100)
p = int(input("Enter total money:"))
r = int(input("Enter total rate:"))
t = int(input("Enter total time:"))
print("Simple interest is:",(p*r*t)/100)

#Q12: Perimeter of rectangle (2 × (L + B))
length = int(input("Enter length of Reactangle:"))
breadth = int(input("Enter breadth of Reactangle:"))
perimeter = 2 * (length + breadth)
print("Perimeter is:",perimeter)

#Q13: Convert Celsius to Fahrenheit
celsius = float(input("enter celsius value"))
fahrenheit = (celsius*9/5) + 32
print("fahrenheit is:",fahrenheit)

#Q14: Swap two numbers (using a third variable)
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
temp = a
a = b
b = temp
print("After swapping:first number=",a,"second number=",b)

#Q15: Volume of a cube (side³)
side = int(input("Enter the side of Cube:"))
volume = side * side * side 
print("Volume of cube is:",volume)
