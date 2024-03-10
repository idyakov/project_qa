# Homework Lesson 10 - Workshop - Homework

# READ CAREFULLY THE EXERCISE DESCRIPTION AND SOLVE IT RIGHT AFTER IT

################################################################################
### When solving coding challenges, think about the time complexity (Big O). ###
################################################################################

# Challenge 1
# Multiplication of a three-digit number
#
# A program gets a three-digit number and has to multiply all its digits.
# For example, if a number is 349, the code has to print the number 108, because 3*4*9 = 108.
#
# Hints:
# Use the modulus operator % to get the last digit.
# Use floor division to remove the last digit

def multiplication_of_three(number):
    while number > 0:
        last_digit = number % 10
        x *= last_digit
        number //= 10
    print(x)

x = 1
number = int(input("Please enter your number: "))
multiplication_of_three(number)

# ---------------------------------------------------------------------

# Challenge 2
# Sum and multiplication of even and odd numbers.
#
# You are given an array of integers. Your task is to calculate two values: the sum of
# all even numbers and the product of all odd numbers in the array. Please return these
# two values as a list [sum_even, multiplication_odd].
#
# Example
# For the array [1, 2, 3, 4]:
#
# The sum of all even numbers is 2 + 4 = 6.
# The product of all odd numbers is 1 * 3 = 3.
# The function should return the list [6, 3].

def sum_even_and_product_odd(my_list):
    sum_even = 0
    odd = 1
    for n in my_list:
        if n % 2 == 0:
            sum_even += n
        else:
            odd *= n
    return [sum_even, odd]

my_list = [1, 2, 3, 4]
result = sum_even_and_product_odd(my_list)
print(result)
# ---------------------------------------------------------------------

# Challenge 3
# Invert a list of numbers
#
# Given a list of numbers, return the inverse of each. Each positive becomes a negative,
# and the negatives become positives.
#
# Example:
# Input: [1, 5, -2, 4]
# Output: [-1, -5, 2, -4]

def invert_list(arr):
    return [-n for n in arr]

arr = [1, 5, -2, 4]
invert_list(arr)
print(invert_list(arr))
# Your code here

# ---------------------------------------------------------------------

# Challenge 4
# Difference between
#
# Implement a function that returns the difference between the largest and the
# smallest value in a given list.
# The list contains positive and negative numbers. All elements are unique.
#
# Example:
# Input: [3, 5, 7, 2]
# Output: 7 - 2 = 5

# If the list is not empty,
# proceed with the rest of the code.

# Your code here
def max_diff(arr):
    # Check if the list is empty
    # If it is, return 0 as there's no difference to be calculated
    if len(arr) == 0:
        return 0
    min_num = min(arr)
    max_num = max(arr)
    return max_num - min_num

arr = [3, 5, 8, 2]
result = max_diff(arr)
print(result)

# ---------------------------------------------------------------------

# Challenge 5
# Sum between range values
# You are given an array of integers and two integer values, min and max.
# Your task is to write a function that finds the sum of all elements in the
# array that fall within the range [min, max], inclusive.
#
# Example:
arr = [3, 2, 1, 4, 10, 8, 7, 6, 9, 5]
min_val = 3
max_val = 7
#
# Output: 25 (3 + 4 + 5 + 6 + 7)
#
# Hint:  Iterate through each number (num) in the array (arr) and check if the current number  falls within the range [min_val, max_val].

def diff_max_min(numbers):
    max_val = max(numbers)
    min_val = min(numbers)
    return  max_val - min_val
# Your code here

arr = [3, 2, 1, 4, 10, 8, 7, 6, 9, 5]

result = diff_max_min(arr)
print(result)