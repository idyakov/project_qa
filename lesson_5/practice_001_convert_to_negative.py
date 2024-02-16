# Create a variable called number. Set it to any number.

# Convert the number to negative and print it.
# Keep the number as is, if the number is already negative.

# 5 => -5
# -1 => -1


number = int(input('Input the number which you are going to make it negative: '))
if number > 0:
    print(number * -1)
elif number < 0:
    print(number)


