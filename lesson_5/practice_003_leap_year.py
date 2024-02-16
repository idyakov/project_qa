# Your goal is to decide if a given year is a leap year.
# A leap year is divisible by 4, except for centuries (divisible by 100)
# which must also be divisible by 400.

year = int(input("Enter a year: "))
if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print(f"{year} if a leap year")
        else:
            print(f"{year} is no a leap year")
    else:
        print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")


example_list = [3, 7, 2, 8, 1, 12]
for value in example_list:
    if value % 2 == 0:
        print(value)


numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,     615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,     743, 527]

# your code goes here
for x in numbers:
    if x % 2 == 1:
        print(x)


