# Homework Lesson 2 - Strings

# READ CAREFULLY THE EXERCISE DESCRIPTION AND SOLVE IT RIGHT AFTER IT

# ---------------------------------------------------------------------
# Exercise 1: Personalized Greeting
# Write a program that takes a user's name as input
# and then greets them using an f-string: "Hello, [name]!"
#
# Example Input: "Alice"
# Example Output: "Hello, Alice!"
name = input("Enter yor name: ")
print("Hello",name)

# ---------------------------------------------------------------------
# Exercise 2: Greeting with User's Favorite Activity
# Write a program that takes a user's name and their
# favorite activity as input, and then greets them
# using the formatting method of your choice as:
# "Hello, [name]! Enjoy [activity]!"

# Example Input:
# Name: Emily
# Favorite Activity: hiking
# Example Output: "Hello, Emily! Enjoy hiking!"
name = input("Enter your name please: ")
activity = input("Tell us about your activity: ")
print("Hello,", name,"! You can join to our club of",activity," any time")

result = f"Hello {name}!. You can join to our club of,{activity}!"
print(result)


#another exemple with
activity = input ("What is the best your activity: ")
name = input("Enter your name here ")
result = f"Hello {name}!. You can join to our club of {activity}!"
print(result)

# ---------------------------------------------------------------------
# Exercise 3: Membership Cards
# You are designing a simple registration system for a club.
# When new members sign up, you want to ensure their names
# are displayed in uppercase on their membership cards.
# Write a program that takes the new member's name as
# input and prints it in uppercase and prints a welcome message
# using .format()
# Example Input:
# Name: Emily
# Example Output: "Welcome, Emily! Your name in uppercase is: EMILY!"
text = input("Please enter your registered name:")
result = f'Welcome {text}! Your name in uppercase is: {text.upper()}'
print(result)

# ---------------------------------------------------------------------
# Exercise 4: User Profile Creation
# Build a user profile generator. Ask
# the user for their first name, last name, and age. Create
# a profile summary using .title(), .upper(), and .format().
#
# Example Input:
# First name: john
# Last name: smith
# Age: 28
#
# Example Output:
# Name: John Smith
# Age: 28
#Upper Formatting
#Input
f_name = input("Input your first name in lowercase format: ")
l_name = input("Input you last name in lowercase format: ")
Age = input("Input your a year of your birthday please: ")
text_age = 2024 - int(Age)
print("First name: ", f_name.upper())
print("Last naem: ", l_name.upper())
print("Your Age is:", text_age)

#Title Formatting
#Input
f_name = input("Input your first name in lowercase format: ")
l_name = input("Input you last name in lowercase format: ")
Age = input("Input your a year of your birthday please: ")
text_age = 2024 - int(Age)
print("First name: ", f_name.title())
print("Last naem: ", l_name.title())
print("Your Age is:", text_age)

#Title Formatting
#Input
f_name = input("Input your first name in lowercase format: ")
l_name = input("Input you last name in lowercase format: ")
Age = input("Input your a year of your birthday please: ")
text_age = 2024 - int(Age)
print("First name:", format(f_name.title()))
print("Last name:", format(l_name.title()))
print("Your Age is:", format(text_age))

# ---------------------------------------------------------------------
# Exercise 5: Text message limits
# You are developing a text messaging application that limits the
# number of characters in a single message. Your task is to create
# a Python program that takes a message as input from the user.
# The program should calculate and display the number of characters
# in the message, including spaces, and format the output using
# an f-string. This character count will help users ensure their
# messages fit within the allowed limit.
message = str(len(input('Please input your message: ')))
name = str(len(input('Please input your name: ')))
print(f'The number of character in your message are: {message} and your name charactes are: {name}')

# ---------------------------------------------------------------------
# Exercise 6: Text Transformation Game
# Create a text transformation game. Ask the user
# to enter a sentence. Replace all vowels with '*'. Display the
# modified sentence.
#
# Example Input: "Hello, world!"
# Example Output: "H*ll*, w*rld!"
message = input("Enter a sentence: ")
transformed_sentence = message.replace('o', '*')
transformed_sentence_q = transformed_sentence.replace('a', '*')
print(transformed_sentence_q)


# ------------------------------# ---------------------------------------------------------------------
# Exercise 7: Extracting Information
# The variable 'data' is a student record in the format "name:age"
# Use string slicing and string methods to extract the name and the age
# and print the result formatted.
#
# data = "lucy smith:28"
#
# Expected output:
# Name: Lucy Smith
# Age: 28

data = "lucy smith:28"
sliced_text = data[0:4]
sliced_text_q = data[11:13]
print("Name: ", sliced_text.title())
print("Age: ", sliced_text_q.format())

# ---------------------------------------------------------------------
# Exercise 8: Miles to Kilometers Conversion
# Write a program that converts a distance in miles to kilometers.
# Take the distance in miles as input, convert it to kilometers
# using the formula miles * 1.6, and display the
# result using f-strings.

# Example Input: 10
# Example Output: 10 miles is approximately 16.0 kilometers.

# We are converting the input string to float:
# Input: float("1.23")
# Output: 1.23
distance = float(input("Please input your number of miles: "))
miles = distance * 1.6
print(f' The numbers of miles is: {distance} and this is approximatly amount of kilometers: {miles}' )

# ---------------------------------------------------------------------
# Exercise 9: Workouts calculator
# Write a Python program that asks the user to input the number
# of minutes spent on three different exercises: cardio, strength
# training, and yoga using the input() function. Convert the input
# strings to integers using the int() function. Calculate the
# total time spent on workouts by summing up the minutes from all
# three activities. Based on the total workout time, provide a
# motivational message using an f-string that encourages the user
# to stay consistent and reach their fitness goals. Display the
# motivational message to the user.
name = input("Please input your name: ")
cardio = int(input("Please input the number of minutes in cardio: "))
strenght = int(input("Please input the number of minutes in strenght training: "))
yoga = int(input("Please input the number of minutes in yoga: "))
activities = int(cardio+strenght+yoga)
goal = 120 - activities
print(f'Hello {name}, you are the best memeber in our fitness clus, your current number of activities is: {activities}.Please keep going and do not stop, to reach the best number of activity left {goal}. The goal is 120 minutes for today!')


# ---------------------------------------------------------------------
# Challenge 1 (OPTIONAL!): Reverse the negative integer -324 and keep
# the negative symbol. Expected output: -423


# Convert the integer to a string to handle the negative symbol separately
num_str = str(input_number)

# Reverse the digits (excluding the negative symbol) using slicing [::-1]
# Use this simple guide to help you slice the reversed string:
# http://bit.ly/3siP47n

# (ADD YOUR CODE BELOW)

# Add the negative symbol back to the reversed string
reversed_num = int(num_str[0] + reversed_str)

# Output the result
# (ADD YOUR CODE BELOW)
input_number = -324
output_number=int(str(input_number)[0] + str(input_number)[:0:-1])
print(output_number)


# ---------------------------------------------------------------------
# Challenge 2 (OPTIONAL!): Formatting Average Speed
# In this exercise, we're developing a program to determine the
# average speed of a truck based on the distance traveled in miles
# and the total time taken in hours. Your task is to format and display
# this average speed accurately.
# Task:
# Your program should take the number of miles and the total number
# of hours traveled as input and calculate the average speed. Then,
# present the average speed in a user-friendly format, rounded to one
# decimal place.
#
# Example:
# If the driver covered 60 miles in 3 hours, the calculated average
# speed is 20.0 miles per hour. However, we want to display it as
# 'The average speed is 20.0 miles per hour'.
##
# Similarly, for 55 miles and 3 hours, the calculated speed is
#  approximately 18.33333333332, but we want to format and display
#  it as 'The average speed is 18.3 miles per hour'.
#
# Hints:##
# Refer to the "Format examples" section in the official Python
# documentation for string formatting techniques:
# https://docs.python.org/3/library/string.html#format-examples
# Experiment with different formatting options to achieve the
# desired presentation of the average speed.
#
# Taking input for miles and hours
miles = int(input("Enter the number of miles: "))
hours = int(input("Enter the total number of hours: "))
#
# Calculating average speed
average_speed = miles / hours
#
# Formatting and displaying the result
# (Your code here)
rounded_speed = ????
#
print(f"The average speed is {rounded_speed} miles per hour")

# Output the result
miles = float(input("Please input the number of miles: "))
hours = int(input("Please input the number of hours: "))
average = miles / hours
rounded_speed  = round(average, 1)
print(f'The average speed is {rounded_speed} mi les per hour')
#