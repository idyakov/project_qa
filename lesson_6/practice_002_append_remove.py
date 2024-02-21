# Create an empty list and add the following elements about your location, in this order:
# - City
# - State or Province
# - A list with the temperatures the last three days
# - Your favorite animal

my_list = []
my_list.append('City')
my_list.append('California')
my_list.append('shark')
print(my_list)
# Then, remove the State, without using the indexes.
#.remove('California')

# Bonus: Remove the last element, using a negative index.
del my_list[-1]
print(my_list)

my_list = []
my_list.append('City')
my_list.append('California')
my_list.append('shark')
print(my_list)
# Then, remove the State, without using the indexes.
#.remove('California')

# Bonus: Remove the last element, using a negative index.
del my_list[-1]
print(my_list)


if "TOM" not in my_friends:
    print("YES HE IS")
else:
    print("NO HE IS NOT")