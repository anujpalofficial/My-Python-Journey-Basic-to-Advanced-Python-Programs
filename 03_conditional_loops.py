"""Today(3 september 2025) we will discuss some baisc to advanced python programs based on (Syntax + Input/Output) using only:
- if/elif/else (conditional branching)
- match case
- Loops (for,while)
- break,continue & pass
"""

#Q1: Write a program to check if a number is even or odd
num = int(input("Enter a number:"))
if num %2 == 0:
    print(num,"is an even number.")
else:
    print(num,"is an odd number.")    


#Q2: Take marks as input and print the grade:
"""
   * 90+ → A
   * 75–89 → B
   * 50–74 → C
   * <50 → Fail
   """
marks = int(input("Enter your marks:"))
if marks >= 90 and marks <=100:
    print("Grade A")
elif marks >= 75 and marks <= 89:
    print("Grade B")
elif marks >= 50 and marks <= 74:
    print("Grade C")
elif marks < 50:
    print("Fail!")
else:
    print("please enter vaild marks value.")    


#Q3: Ask the user for a number (1–7) and print the corresponding day of the week using match case
day = int(input("Enter a number between (1-7):"))
match day:
    case 1:
        print(day,"stand for Sunday")
    case 2:
        print(day,"stand for Monday")
    case 3:
        print(day,"stand for Tuesday")
    case 4:
        print(day,"stand for Wednesday")
    case 5:
        print(day,"stand for Thursday")
    case 6:
        print(day,"stand for Friday")
    case 7:
        print(day,"stand for Saturday")
    case _:
        print("please enter a valid value")                            

#Q4: Take age as input and check:
"""
   * age < 13 → Child
   * 13–19 → Teen
   * 20+ → Adult
   """
age = int(input("Enter your age:"))
if age <= 13 and age > 0:
    print("child")
elif age > 13 and age < 19:
    print("teen")
elif age >= 20:
    print("adult")
else:
    print("please enter a valid value")     
       

#Q5: Print numbers from 1 to 10 using a for loop.
for i in range(1,11):
    print(i)


#Q6: Print the multiplication table of a number.
number = int(input("enter a number:"))
for i in range(1,11):
    print(number,"X",i,"=",number*i)


#Q7: Take a number and print its factorial using a while loop.
sum = 1
i = 1
num = int(input("enter a number:"))
while i < num + 1:
    sum *= i
    i += 1
print("Factorial of",num,"is:",sum)


#Q8: Ask the user for 10 numbers, print the sum of only even numbers.
sum = 0
for i in range(1,11):
    if i % 2 != 0 or i == 1:
        continue
    sum += i
    print(i,end="+")
print("=",sum)



#Q9: Use match case to build a basic calculator: (+, -, \*, /).
num1 = int(input("enter first number:"))
num2 = int(input("enter second number:"))
operator = input("input operator:")
match operator:
    case "+":
        print("sum of",num1,"and",num2,"is:",num1+num2)
    case "-":
        print("difference of",num1,"and",num2,"is:",num1-num2)
    case "*":
        print("product of",num1,"and",num2,"is:",num1*num2)
    case "/":
        print("divison of",num1,"and",num2,"is:",num1/num2)
    case _:
        print("please enter a valid value")                


#Q10: Take a number n and print all numbers from 1 to n except multiples of 3 (use continue).
n = int(input("please a enter a number:"))
for i in range(1,n+1):
    if i % 3 == 0:
        continue
    print(i)    


#Q11: Keep asking the user for numbers until they enter 0, then stop (use while + break).
while True:
    num = int(input("enter a number:"))
    if num == 0:
        break
    print(num)


#Q12: Print all prime numbers between 1 and 100.
for i in range(2,101):
    for j in range(2,int(i**0.5)+1):
        if i % j == 0:
            break
    else:
        print(i)


#Q13: Create a simple guess the number game:
"""
    * Secret number = 7
    * User keeps guessing until correct (use while + break)
    """
while True:
    num = int(input("please the number between 1 to 10:"))
    if num == 7:
        break
    print(num)


#Q14: Print this pattern using loops:
"""
    *
    **
    ***
    ****
    *****  
    """
for i in range(1,6):
    print("*"*i)


#Q15: Build a menu-driven ATM program using match case:
"""
    * 1 → Check balance
    * 2 → Deposit
    * 3 → Withdraw
    * 4 → Exit
    """
amount = 0
menu = int(input("Enter what you want:1 for balance check,2 for deposit,3 for withdraw,4 for exit:"))
if menu == 3 or menu == 2:
    amount = int(input("please enter amount:"))
total = 0
match menu:
    case 1:
        print("your balance is:",total)
    case 2:
        print("your deposited:",amount)
        print("Total balance:",total+amount)
    case 3:
        print("your withdraw,:",amount)
        print("Total balance:",total-amount)
    case 4:
        print("Thanks for your services,if you wanna service please enter a valid value")            
