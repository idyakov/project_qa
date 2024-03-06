# HOMEWORK: Functions
# Read carefully until the end before you start solving the exercises.

# Basic Function
# Define a basic function that only prints Hello. Create the definition using def and the call that executes it.

# ----------------------------------------------------------------------------------------------------------------------

# Basic Function with Parameters
# Define a basic function that prints a greeting taking a given name.

# ----------------------------------------------------------------------------------------------------------------------

# Basic Function with Default Values
# Define a basic function that prints a greeting for a name, but if none is given, use stranger instead of the name,
# so it behaves like this:

# Prints: Hello, stranger!
# greeting()

def greeting():
    name = input('Hey Gringo, please input your original name : ')
    if name == '':
        print('Hello, stranger!')
    else:
        print(f'Hello {name}')


greeting()


# Prints: Hello, Tom!
# greeting('Tom')
def greeting(value):
    print(f"Hello {value}")


greeting('Tom')


# ----------------------------------------------------------------------------------------------------------------------

# Multiple Parameters
# Define a function that takes two parameters, add them up and prints the sum.

# Prints: The sum of 1 + 2 = 3
# add(1, 2)

def value(a, b):
    c = a + b
    return c


sum_val = value(1, 2)
print(f'The sum of 1 + 2 = {sum_val}')


# Prints (default values might be useful): The sum of 1 + 0 = 1
# add(1)
def add(a, b):
    c = a + b
    return c


a = 1  # default values
b = 0  # default values
sum_val = add(a, b)
print(f'The sum of {a} + {b} = {sum_val}')


# ----------------------------------------------------------------------------------------------------------------------

# Parameters out of order
# Define a function that takes a first_name and a last_name and prints a full_name. Define the function and create
# the function call in such a way that first_name and last_name can be given in any order and the printed full_name
# would still be correct.

# Prints: Nelson Mandela
def full_name():
    a = input('Please enter the name - Nelson ')
    b = input('Please enter the lastname - Mandela')
    c = f' Hello Mr. {a} {b}'
    print(c)


full_name()


#############other way
def full_name(fname, lname):  # paramaters of the functions
    print(f'Hello Mr. {fname} {lname}')  # Calling the value of parameters


a = input('Please enter the name: ')
b = input('Please enter the lastname: ')

full_name(a, b)  # Depends on the value of your input a and b
full_name('Nelson', 'Mandela')  # Directly gives a value of paramaters fname and lname


# Is there anything you can add to the line below, so the function also prints "Nelson Mandela"?
# full_name("Mandela", "Nelson")
def full_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    print(full_name)


full_name("Nelson", "Mandela")


# ----------------------------------------------------------------------------------------------------------------------

# Returning Values
# Define a validator function that you can use to determine if a word is longer than 8 characters.
# After creating the function, make sure to test it. Create a list of words and iterate over this
# list using a for loop.
def is_longer_than_8_chaaracters(word):
    return len(word) > 8


words = ['test', 'Validation', 'TestValidation', 'DataValidation8', 'te']

for word in words:
    if is_longer_than_8_chaaracters(word):
        print(f"'{word} is longer than 8 characters. (strong)'")
    elif len(word) > 5:
        print(f"'{word} is not longer than 5 characters. (medium)'")
    else:
        print(f"'{word} is 5 or less characters. (short)")

# Tip: Validator functions return True / False which we can use in conditionals to do things like print a message.

# ----------------------------------------------------------------------------------------------------------------------

# You're going to revisit some of the algorithms you've already solved. But this time, there's a twist! Your challenge
# is to solve and encapsulate each algorithm into its own Python function. This will not only help you review these
# algorithms but also give you valuable practice in defining and using functions.

# FizzBuzz
# You remember FizzBuzz, right?
# You print Fizz for multiples of 3, Buzz for multiples of 5, and FizzBuzz for multiples of both 3 and 5.

# Now, your task is to take your existing FizzBuzz code and wrap it into a function called fizzbuzz.

# Requirements:
# - Create a function named fizzbuzz that takes a single argument, number.
# - If the number is a multiple of both 3 and 5, the function should return: FizzBuzz
# - If the number is a multiple of 3, the function should return: Fizz
# - If the number is a multiple of 5, the function should return: Buzz
# - Otherwise, the function should return the number.


number = int(input())

if number % 3 == 0 and number % 5 == 0:
    print('FizzBuzz')
elif number % 3 == 0:
    print('Fizz')
elif number % 5 == 0:
    print('Buzz')

else:
    print(number)
# Call the function here

ArithmeticError


def fizzbuzz(number):
    pass


number = 25


#################################################################################

def fizzbuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        print('Fizzbuzz')
    elif number % 3 == 0:
        print('Fizz')
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)


fizzbuzz(number)


# ----------------------------------------------------------------------------------------------------------------------

# Anagram
# Your next challenge is to implement a function that checks if two given strings are anagrams of each other.
# An anagram is a word or phrase formed by rearranging the letters of a different word or phrase. For example,
# "listen" is an anagram of "silent".

# What You Need to Check
# - The two strings must have the same length.
# - The sorted form of the first string must be equal to the sorted form of the second string.

# Approach
# - Create a function that takes two strings as arguments.
# - Check if the lengths are equal. If they're NOT equal, return False (anagrams are always same length).
# - Sort both strings. If the sorted versions are equal, they're anagrams!
def check_word(test_str1, test_str2):
    if (sorted(test_str1) == sorted(test_str2)) and len(test_str1) == len(test_str2):
        print("This word is anagram.")
    else:
        print("This word is not anagram.")


test_str1 = 'listen'
test_str2 = 'silent'
# Test your function with these strings

check_word(test_str1, test_str2)


# ----------------------------------------------------------------------------------------------------------------------

# Find Max number
# Create a function to find the largest number in a list without using the built-in max() function.

# - Define a function called find_max that takes a list of numbers as an argument.
# - Initialize a variable result and set it to the 1st item of the list using [0]
#   - This variable will hold the largest number as we iterate through the list.
# - Loop through each number in the list.
# - Check if number > result
#   - If it is, update result with the new greater number.
# - return result

# Define your function here

# Test the function with a sample list of numbers.

def max_number():
    number = my_list
    x = sorted(number, reverse=True)
    print(x[0])
    # Output should be the maximum number in the list.


my_list = [1, 7, 2, 4, 14, 3, 12]
max_number()


# other way
def find_number(numbers):
    result = numbers[0]
    for number in numbers:
        if number > result:
            result = number
    return result


my_list = [1, 7, 2, 4, 14, 3, 12]
print(find_number(my_list))


# ----------------------------------------------------------------------------------------------------------------------

# Even/Odd Checker Function
# Your task is to write a function that determines if a given integer is even or odd. The function should
# print Even for even numbers and Odd for odd numbers.

# What You Need to Check
# - Determine whether the input number is even or odd.
# - An even number can be exactly divided by 2 without a remainder.
# - An odd number leaves a remainder of 1 when divided by 2.

# Define a function is_even_odd(number) here

def is_even_odd(number):
    if number % 2 == 0:
        print("Even number")
    else:
        print("odd number")

number = float(input("Enter the number please: "))

is_even_odd(number)
# Test the function calling it using a variety of numbers like: 1, 10, 5.5, 9
