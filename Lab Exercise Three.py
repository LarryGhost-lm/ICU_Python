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

#TASK:Lab Exercise 3,Program to Manage Favorite Movies



#EXERCISE:Write a program that:
# 1. Creates a list of your favorite movies.
# 2. Lets the user add a new movie.
# 3. Lets the user remove a movie.
# 4. Prints the final sorted list.




# Step 1: Create a list of favorite movies
movies = ["3 idiots", "The Gladiator", "Interstellar"]

# Step 2: Let the user add a new movie
new_movie = input("Enter a movie to add to the list: ")
movies.append(new_movie)

# Step 3: Let the user remove a movie
remove_movie = input("Enter a movie to remove from the list: ")
if remove_movie in movies:
    movies.remove(remove_movie)
else:
    print(remove_movie, "is not in the list.")

# Step 4: Print the final sorted list
movies.sort()
print("Here is your final movie list:", movies)


#Below are the resouses used for this Task:
    #| Step | Code                                                     | Explanation                        |
    #| ---- | -------------------------------------------------------- | ---------------------------------- |
    #| 1    | `movies = ["Inception", "The Matrix", "Interstellar"]`   | Start with favorite movies         |
    #| 2    | `movies.append(new_movie)`                               | Add a movie entered by the user    |
    #| 3    | `if remove_movie in movies: movies.remove(remove_movie)` | Remove a movie safely              |
    #| 4    | `movies.sort()`                                          | Sort the final list alphabetically |
