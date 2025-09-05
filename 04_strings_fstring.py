"""Today(4 september 2025) we will discuss some baisc to advanced python programs based on (Strings) using only:
- Strings indexing
- Strings methods
- String formatting
- f-Strings
"""
#Q1: Take your name as input and print:
"""Hello, [name]! Welcome to Python. (using f-string)"""
name = input("Enter your name:")
print(f"{name}! Welcome to Python.")


#Q2: Ask for a word and print its length.
word = input("Enter a word:")
print(len(word))


#Q3: Take a string and print the first character and last character.
str = input("Enter a string:")
print(f"first character is:{str[0]}, last character is:{str[len(str)-1]}")


#Q4: Ask the user for two strings and concatenate them with a space in between.
str1 = input("Enter first string:")
str2 = input("Enter second string:")
final = str1 +" "+ str2
print(final)


#Q5: Take a sentence and print it in uppercase and lowercase.
sentence = input("Enter a sentence:")
print(sentence.lower())
print(sentence.upper())


#Q6: Ask the user for a sentence and count how many times the letter 'a' appears.
sentence = input("Enter a sentence:")
final = sentence.lower()
print(final.count("a"))


#Q7: Take a string and print it reversed (using slicing).
str = input("Enter a string:")
print(str[::-1])


#Q8: Input a name and print only the first three characters.
name = input("Enter your name:")
print( name[0:3])


#Q9: Ask for a sentence and replace all spaces " " with "-".
sentence = input("Enter a sentence:")
print(sentence.replace(" ","-"))


#Q10: Take a string and check if it starts with "Hello" and ends with "bye".
str = input("Enter a string:")
print("starts with hello:",str.startswith("Hello"))
print("starts with hello:",str.endswith("bye"))


#Q11: Format this sentence using .format() →
"""\"My name is Rahul, I am 18 years old and I live in Meerut."
(values should come from user input)."""
name = input("Enter your name:")
age = int(input("Enter your age:"))
city = input("Enter your city name:")
sentence = "My name is {}, I am {} years old and I live in {}."
print(sentence.format(name,age,city))


#Q12: Do the same sentence but using an f-string.
name = input("Enter your name:")
age = int(input("Enter your age:"))
city = input("Enter your city name:")
print(f"My name is {name}. I am {age} years old. I live in {city}")


#Q13: Ask the user for a string and check if it is a palindrome (same forward and backward).
str = input("Enter a string:")
if str == str[::-1]:
    print("its a palindrome")
else:
    print("its not a palindrome.")    

#Q14: Take an email address and extract the username (before @).
#Example: anuj123@gmail.com → anuj123
email = input("Enter your email address.")
print(email[0:email.find("@")])


#Q15: Build a mini program that takes:
"""
Name
Age
City
and prints this formatted certificate (use f-strings + \n):
--------------------------
     Student Details
Name : Rahul Sharma
Age  : 18
City : Meerut
--------------------------
"""
name = input("Enter your name:")
age = int(input("Enter your age:"))
city = input("Enter your city name:")
print(f"--------------------------\n\tStudent Details\nName : {name}\nAge : {age}\nCity : {city}\n--------------------------")