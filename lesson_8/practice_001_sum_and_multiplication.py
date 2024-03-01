# Given a list.
# Calculate sum and multiplication of all elements.
# Print the list, sum and multiplication of elements.
# For example:
# Input: [1, 2, 3, 4]
# Output sum: 10
# Output multiplication: 24
numbers = [1,2,3,4]
sum_result = 0
mult_result = 1

for x in numbers:
    sum_result += x
    mult_result *= x
print(sum_result)
print(mult_result)

