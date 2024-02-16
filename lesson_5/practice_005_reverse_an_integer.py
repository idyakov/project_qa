# Given an integer, return the integer with reversed digits.
#
# Note:
# The integer could be either positive or negative.
#
# Example:
# -876 -> -678

n = -546
s = str(n)

if s[0] == '-':
    print("-" + s[:0:-1])
else:
    print(s[::-1])