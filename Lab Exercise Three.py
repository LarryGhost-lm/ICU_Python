# -*- coding: utf-8 -*-
"""
Created on Fri Sep 12 20:03:03 2025

@author: muchi
"""

#|************INFORMATION AND COMMUNICATION UNIVERSITY***************|
#|********************ENGINEERING DEPARTMENT*************************|


#PROGRAM: ELECTRICAL AND ELECTRONICS ENGINEERING

#COURSE: FOUNDAMENTALS OF PROGRAMING

#STUDENT NAME:Larry Muchimba

#SIN: 2502100895

#TASK:Lab Exercise 3,Multiplication Table Program



#EXERCISE:
# Write a program that asks the userfor a number and prints its multiplication table up to 12.




# Ask the user for a number
#Get user input → input() reads a number as a string, int() converts it into an integer.
num = int(input("Enter a number: "))

# Print multiplication table up to 12
#Loop from 1 to 12 → for i in range(1, 13) generates numbers 1 through 12.
#Print formatted result → f"{num} x {i} = {num * i}" displays the multiplication in a clean format.
print(f"\nMultiplication Table for {num}:")
for i in range(1, 13):  # Loop from 1 to 12
    print(f"{num} x {i} = {num * i}")



#Below are the resouses used for this Task:
    #| Step | Code                                   | Explanation                  |
    #| ---- | -------------------------------------- | ---------------------------- |
    #| 1    | `num = int(input("Enter a number: "))` | Ask the user for a number    |
    #| 2    | `for i in range(1, 13):`               | Loop through numbers 1 to 12 |
    #| 3    | `print(f"{num} x {i} = {num * i}")`    | Print multiplication result  |

