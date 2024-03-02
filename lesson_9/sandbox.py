# def value_min(a, b, c):
#     num = min(a, b, c)
#     return num
# numbers = value_min(13.4, 25, 34.3)
# print("Your smallest number is:", numbers)

def value_min(numbers):
    num = min(numbers)
    return num
numbers = [3, 1.99, 2, 1.98, 15]
minimum_number = value_min(numbers)
print(f"Your smallest number is:, {minimum_number}")




def greeting(value):
    if value == '':
        print('Hello, stranger!')
    else:
        print(f'Hello {value}')

# Ask for user input if no value is provided
def get_name():
    return input('Hey Gringo, please input your original name: ')

# Call the function with user input


# Call the function with a specific name
def greeting(value):
greeting('Tom')