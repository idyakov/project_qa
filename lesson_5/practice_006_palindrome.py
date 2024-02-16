# A palindrome is a word, number, phrase, or other sequence of symbols
# that reads the same backwards as forwards:
#
# madam -> madam
# racecar -> racecar
# tacocat -> tacocat
#
# Write a program that will print True if the word is a palindrome
# and False if it is not.

word = input('Enter the word tacocat or something else: ')
reversed_word = word[::-1]
if word == reversed_word:
    print("True")
else:
    print("False")
print(reversed_word)

