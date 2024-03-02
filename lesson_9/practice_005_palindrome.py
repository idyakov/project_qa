# Create a program that prints whether a given word is a palindrome.
# Palindrome: A word that is the same both ways, like tacocat, racecar, madam.

# The word should be provided by the user using input()
# Your function should take one argument.
# Your function should return True / False.
# You should use the return value of the function to print out if the word
# is a palindrome or not.

# Hint: The following code might be useful to determine if a word is a palindrome.

def reversed_word = word[::-1]

    if word == reversed_word:
        print("True")
   # Word IS a palindrome
    else:
        print("False")
    print(reversed_word)
   # Word is NOT a palindrome

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
