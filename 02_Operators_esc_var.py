"""Today(2 september 2025) we will discuss some baisc to advanced python programs based on (Syntax + Input/Output) using only:
- operators
- escape sequence characters
"""
#Q1:Store your college name in a variable and print it inside double quotes using escape sequence. 
#Example → "Government Polytechnic Mawana Khurd"
college = str(input("Enter your college name:"))
print("\""+ college +"\"")

#Q2:Print the sentence using escape sequences exactly like this:
""" Python\tBasics
    Line1\nLine2 """
print("Python\\tBasics\nLine1\\nLine2")

#Q3:Print this pattern (use \t and \n smartly, no loops):
""" A	B	C
    D	E	F
    G	H	I  """
print("A\tB\tC\nD\tE\tF\nG\tH\tI")

#Q4:Take two numbers and print result of floor division (//) and power ()**.
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
floor = num1 // num2
power =  num1 ** num2
print(floor)
print(power)

#Q5:Print this exact output using escape sequences (no multiple print statements):
"""
I am learning "Python"
It is fun!\nReally fun
"""
print("I am learning \"Python\"\nIt is fun!\\nReally fun")

#Q6:Take a 4-digit number as input and print it like this (using indexing + \n):
""" Digit1: x
    Digit2: y
    Digit3: z
    Digit4: w """
num = input("Enter a 4 digit number:")
print("Digit1:",num[0],"\nDigit2:",num[1],"\nDigit3:",num[2],"\nDigit4:",num[3])

#Q7:Ask the user for name and marks, and print a formatted certificate:
""" -----------------------
    \tStudent Report Card
    Name: Rahul Kumar
    Marks: 88
    ----------------------- """
name = input("Enter your name:")
marks = int(input("Enter your marks:"))
print("-----------------------\n\\tStudent Report Card\nName:",name,"\nMarks:",marks,"\n-----------------")

#Q8: Ask for age and print whether the person is an adult (age >= 18).
age = int(input("Enter your age:"))
print("Adult:",age >= 18)

#Q9: Store three numbers in variables and print their average.
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
num3 = int(input("Enter three number:"))
average = (num1+num2+num3)/3
print("Average:",average)


#Q10: Take a number and print: Double,Triple,Half
num = int(input("Enter first number:"))
print("Double:",num*2,"\nTriple:",num*3,"\nHalf:",num/2)


#Q11: Calculate the result of this expression: (10 + 5) * 3 - 8 / 2.
print((10+5)*3-8/2)

#Q12: Take two numbers and print:
"""
(a > 10) and (b < 5)

(a == b) or (a != b)
"""
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
print((a>10) and (b<5),"\n",(a==b) or (a!=b))


#Q13: Take two numbers and print whether the first is greater than or equal to the second. (without if else)
a = int(input("Enter first number:"))
b = int(input("Enter seconf number:"))
print("a>=b:",a>=b)


#Q14: Take two numbers and print whether they are equal.(without if else)
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
print("a=b:",a==b)


#Q15: Take one number and print the result of not(number > 0)
number = int(input("Enter first number:"))
print("number>0:",not(number>0))