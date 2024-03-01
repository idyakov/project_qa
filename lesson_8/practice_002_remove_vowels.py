# Remove the lowercase vowels in a given string:
# str1 = ‘Hello, World!’
# The vowels are:
# vowels = "aeiou"
# “y” is not considered a vowel for this task. The input string is always in lowercase.
# Examples:
# "hello" --> "hll"
# "goodbye" --> "gdby"
s = 'Hello, World!'
c = "aeiou"
result = ''
for x in s:
    if x not in c:
        result += x
print(result)
print(len(result))