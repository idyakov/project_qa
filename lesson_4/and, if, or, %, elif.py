temperature = float(input("Enter the temperature in Farenhite"))
#---------------------------------------------------------
if temperature > 0 and temperature <=15:
    print('It is a bit cold')
elif temperature < 0:
    print('It is really cold')
elif temperature >= 333 :
    print('It is temperature (F) in Mercury')
elif temperature >= 85 :
    print('It is temperature (F) in Mars')
elif temperature >= 867 :
    print('It is temperature (F) in Venus')
else:
    print('it is a good temperature')
#---------------------------------------------------------
age = int(input("Enter your age:"))
income = int(input("Enter your monthly income"))
if age >= 18 and income >= 1000:
    print("You qualify for the dicount!")
elif age < 18 or income == 0:
    print('You got a special discount')
else:
    print("Sorry, you are not eligible for any discount")
#---------------------------------------------------------
score = int(input('Enter your score: '))
if score > 90:
    print('Excellent!')
elif score > 70 and score < 90:
    print('Good job')
elif score < 70:
    print('Keep working hard!')
else:
    print('No test score avaiable')
#---------------------------------------------------------
number = int(input('Enter your number: '))
if number % 3 == 0 and number % 5 == 0:
    print('FizzBuzz')
elif number % 3 == 0:
    print('Fizz')
elif number % 5 == 0:
    print('Buzz')
else:
    print('no devided')