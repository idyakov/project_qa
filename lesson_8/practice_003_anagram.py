# Given two words, check if both are anagrams.
# An anagram of a string is another string that contains the same characters, only the order
# of characters can be different.
# For example:
# is_anagram('cat', 'act') => should return True
# is_anagram('bus', 'sub') => should return True
# is_anagram('map', 'cap') => should return False

str_1 = ('cat', 'act')
str_2 = ('bus', 'sub')
str_3 = ('map', 'cap')
if len(str_1) != len(str_2):
    print(False)
elif sorted(str_1) == str_2:
    print(True)
else:
    print(False)


def is_anagram(x, y):
    return sorted(x) == sorted(y)
print(is_anagram('cat', 'act'))
print(is_anagram('bus', 'sub'))
print(is_anagram('map', 'cap'))