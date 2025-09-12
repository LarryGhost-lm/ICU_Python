# -*- coding: utf-8 -*-
"""
Created on Sat Sep  6 20:06:42 2025

@author: Larry muchimba
"""

#************INFORMATION AND COMMUNICATION UNIVERSITY***************
#********************ENGINEERING DEPARTMENT*************************


#PROGRAM: ELECTRICAL AND ELECTRONICS ENGINEERING
#COURSE: FOUNDAMENTALS OF PROGRAMING
#STUDENT NAME:Larry Muchimba
#SIN: 2502100895
#TASK: Lab Exercise 1, Create a program that asks the user for their name 
#...and birth year. Calculate their age andprint the correct age.

#EXERCISE

#Get the User's Name
#Uses the input() function to get the user's name as a string.
name = input("Enter your name: ")

#Get the User's Birth Year
#Uses input() to read a string, then converts it to an integer using int(), since you'll need to do arithmetic.
birth_year = int(input("Enter your birth year: "))

#Calculate the Age
#Subtracts the birth year from the current year (2025 in this case) to compute the user's age.
current_year = 2025
age = current_year - birth_year

#Display the Result
#Combines text and variables to output a greeting and the age.
print("Hello", name + "! You are", age, "years old.")


#POSSIBLE IMPROVEMNTS:
    #The code can utilize the inbuit module to call current date to determine age.
    #Because manually inputing date will require the current year to be edited.
    #There for the following line can be used to call date module:
        #from datetime import datetime
#current_year = datetime.now().year

#Below are the resouses used for this Task:
    #| Function         | Description                     | Link                                                                                            |
    #| ---------------- | ------------------------------- | ----------------------------------------------------------------------------------------------- |
    #| `input()`        | Reads input from the user       | [input() - Python docs](https://docs.python.org/3/library/functions.html#input)                 |
    #| `int()`          | Converts a string to an integer | [int() - Python docs](https://docs.python.org/3/library/functions.html#int)                     |
    #| `print()`        | Prints output to the console    | [print() - Python docs](https://docs.python.org/3/library/functions.html#print)                 |
    #| `datetime.now()` | Gets the current date and time  | [datetime - Python docs](https://docs.python.org/3/library/datetime.html#datetime.datetime.now) |

#******************END OF TASK********************************
#****************I ENJOYED THANK YOU**************************

