# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 11:14:27 2018

@author: Leonavicius
"""

# This function adds two numbers 
def add(x, y):
   return x + y

# This function subtracts two numbers 
def subtract(x, y):
   return x - y

# This function multiplies two numbers
def multiply(x, y):
   return x * y

# This function divides two numbers
def divide(x, y):
   return x / y

def power(x, y):
    z = x
    for i in range(1, y):
        z = z*x
    return z

def printHi():
  print("Hi")
        
def printhello(boolean):
  if boolean == True:
    print('Hello')
  else:
    print('Goodbye')

#ThugLyfe
print('boop')

print("ByeBye")


print("----------- HelloWord - QUICK MATHS SOFTWARE -----------")

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Divide")

# Take input from the user 
choice = input("Enter choice(1/2/3/4/5):")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
   
elif choice == '5':
   print(num1,"/",num2,"=", power(num1,num2))
   
else:
   print("Invalid input")