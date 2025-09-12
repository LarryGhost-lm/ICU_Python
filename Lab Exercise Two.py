# -*- coding: utf-8 -*-
"""
Created on Sat Sep  6 20:09:26 2025

@author: Larry muchimba
"""

#|************INFORMATION AND COMMUNICATION UNIVERSITY***************|
#|********************ENGINEERING DEPARTMENT*************************|


#PROGRAM: ELECTRICAL AND ELECTRONICS ENGINEERING

#COURSE: FOUNDAMENTALS OF PROGRAMING

#STUDENT NAME:Larry Muchimba

#SIN: 2502100895

#TASK:Lab Exercise 2, Create a simple chatbot program



#EXERCISE: # Simple chatbot program
#Description:
    #How It Works

    #Ask for user’s name → stored in name.

    #Greet the user → prints "Hello <name>! Nice to meet you.".

    # Ask about their feeling → stored in feeling.

    # Respond conditionally:

    # "good" → positive response.

    # "bad" → empathetic response.

    # Anything else → neutral acknowledgment.



# Step 1: Ask for the user's name
name = input("What is your name? ")

# Step 2: Greet them using their name
print("Hello", name + "! Nice to meet you.")

# Step 3: Ask how they are feeling today
feeling = input("How are you feeling today? ")

# Step 4: Respond differently based on their answer
if feeling.lower() == "good":
    print("That's great to hear! Keep smiling, " + name + "!")
elif feeling.lower() == "bad":
    print("I'm sorry to hear that, " + name + ". I hope things get better soon.")
else:
    print("Thank you for sharing, " + name + ".")

#Resources Used
# | Step | Code                                                                             | Explanation                    |
# | ---- | -------------------------------------------------------------------------------- | ------------------------------ |
# | 1    | `name = input("What is your name? ")`                                            | Gets the user’s name           |
# | 2    | `print("Hello", name + "! Nice to meet you.")`                                   | Greets the user                |
# | 3    | `feeling = input("How are you feeling today? ")`                                 | Asks about feeling             |
# | 4    | `if feeling.lower() == "good": ... elif feeling.lower() == "bad": ... else: ...` | Responds based on user’s input |

#*******************************END OF TASK***********************************
#LM.