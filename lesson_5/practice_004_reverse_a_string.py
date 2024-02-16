# The [::-1] slicing syntax starts from the end of the string
# (index -1) and goes backward with a step of -1, effectively
# reversing the string.

n = -546
s = str(n)

if s[0] == '-':
    print("-" + s[:0:-1])
else:
    print(s[::-1])