# Homework: Classes
# Read carefully until the end before you start solving the exercises.

# Practice the Basics

# Basic Class

# - Create an empty class HouseForSale
# - Create two instances.
# - Add number_of_rooms and price as instance attributes.
# - Create print statements that show the attribute values for the instances.

class HouseForSale:
    pass
HouseForSale1=HouseForSale() #instance 2
HouseForSale1.number_of_rooms = 8
HouseForSale1.price = 340000

HouseForSale2=HouseForSale() #instance 2
HouseForSale2.number_of_rooms = 9
HouseForSale2.price = 450000

print(f'The number of rooms {HouseForSale1.number_of_rooms}, and the price is {HouseForSale1.price} and on the different address the number of room is {HouseForSale2.number_of_rooms} and the price is {HouseForSale2.price}')

# ----------------------------------------------------------------------------------------------------------------------

# Instance Methods

# - Create a Computer class.
# - Create method:
#   - turn_on that prints Computer has Turned On
#   - turn_off that prints Computer has Turned Off
# - Create an instance of the Computer class then call each method.
class Computer: #class Computer
    def turn_on(self): # Instance method turn_on
        print('Turned On')
    def turn_off(self): # Instance method turn_off
        print('Turn Off')

    #Create instance of Computer
pc = Computer()

#To do things of instances
pc.turn_on()
pc.turn_off()

# ----------------------------------------------------------------------------------------------------------------------

# Constructor with Parameters

# - Create a Dog class.
# - Dog should have a constructor with a name parameter.
# - Dog should have a method say_name that prints the name of the dog.

class Dog:
    def __init__(self, say_name, breed_of_dog):
        self.name = say_name
        self.breed_of_dog = breed_of_dog
        print(f'The name of the Dog is {self.name} and the breed of dog is {self.breed_of_dog}')

say_name = Dog("Sherlock", 'Saint Bernard')




# ----------------------------------------------------------------------------------------------------------------------

# Inheritance

# Create the classes that would make the following code possible, with the caveat that
# both Dog and Cat must inherit from Animal.
class Animal:
    def __init__(self, name=None):
        self.name = name

    def say_name(self):
        if self.name:
            print(self.name)
        else:
            print("I don't have a name yet.")

    def speak(self):
        print("I can't speak!")


class Dog(Animal):
    def __init__(self, name=None):
        super().__init__(name)

    def speak(self):
        print("Woof!")


class Cat(Animal):
    def __init__(self, name=None):
        super().__init__(name)

    def speak(self):
        print("Meow!")


# Testing the classes
animal = Animal()
animal.say_name()  # Prints: I don't have a name yet.
animal.speak()     # Prints: I can't speak!

dog = Dog('Fido')
dog.say_name()     # Prints: Fido
dog.speak()        # Prints: Woof!

cat = Cat('Max')
cat.say_name()     # Prints: Max
cat.speak()        # Prints: Meow!




# animal = Animal()
# animal.say_name()   # Prints: I don't have a name yet.
# animal.speak()      # Prints: I can't speak!
#
# dog = Dog('Fido')
# dog.say_name()      # Prints: Fido
# dog.speak()         # Prints: Woof!
#
# cat = Cat('Max')
# cat.say_name()      # Prints: Max
# cat.speak()         # Prints: Meow!

# THE CODE HERE

class Animal:
    def __init__(self, name = None):
        self.name = name

    def say_name(self):
        if self.name:
            print(self.name)
        else:
            print('I do not have a name yet')
    def speak(self):
        print('I can not speak')
animal = Animal()
animal.say_name()

class Dog(Animal):
    def __init__(self, name = None):
        super().__init__(name)
    def speak(self):
        print("Woof!")
dog = Dog('Fido')
dog.speak()
dog.say_name()

class Cat(Animal):
    def __init__(self, name = None):
        super().__init__(name)
    def speak(self):
        print('Meow')
cat = Cat('Max')
cat.speak()
cat.say_name()

# ----------------------------------------------------------------------------------------------------------------------

# Exercises
# Exercise 1: Books and Authors

# Create an empty class called Book. Then create three instances.
# Add the following attributes for each of the instances: title, author, and publication_year.
# Create print statements to display the attributes of each one of the instances.

# Pre-code:


# Your code here
class Book:
   pass

book1 = Book()
book1.title = 'To Kill a Mockingbird'
book1.author = 'Harper Lee'
book1.publication_year = 1960

book2 = Book()
book2.title = 'Napoleon'
book2.author = 'Yuri Lermontov'
book2.publication_year = 1812

book3 = Book()
book3.title = 'The Jungle Book'
book3.author = 'Kipling'
book3.publication_year = 1894

print(f'The book of {book1.title} wrote down by {book1.author} in {book1.publication_year}')
print(f'The book of {book2.title} wrote down by {book2.author} in {book2.publication_year}')
print(f'The book of {book3.title} wrote down by {book3.author} in {book3.publication_year}')
# ----------------------------------------------------------------------------------------------------------------------

# Exercise 2. Vehicle and Types of Vehicles

# Create a Vehicle class.
# - Its constructor should take the name and type of the vehicle and store them as instance attributes.
# - This Vehicle class should also have a show_type() instance method that prints out the
#   message: "<NAME_OF_VEHICLE> is a <TYPE_OF_VEHICLE>"
# - Create Car and Bike classes that inherit from Vehicle.
# - Create instances of Car and Bike and make them show their types.

class Vehicle:
    def __init__(self, name, type, year):
        self.name = name
        self.type = type
        self.year = year
        print(f"{name} is a {type} and made in {year}")
    def show_type(self):
        print(f'{self.name} is a {self.type} and made in {self.year}' )

#Class car inheritance by Vehicle
class Car(Vehicle):
    pass
#Class bike inheritance by Vehicle
class Bike(Vehicle):
    pass
car = Car("Toyota", "SURV", 1988)
bike = Bike("Suzuki", "sport", 1988)

car.show_type()
bike.show_type()


# ----------------------------------------------------------------------------------------------------------------------

# Exercise 3. Spot and correct the mistakes

# - You are given a task to create a Car class.
# - Each car will have attributes for model and year.
# - Unfortunately, the given code below contains several mistakes.
# - Your task is to find and correct these mistakes to make the code run successfully.
# - Please include a comment in the code explaining the corrections you made and why.

#Pre-code
class Car: # correct
   def __init__(self, model, year):  # on this Constructor Method - SELF represents the instance of class  - was missed
       self.model = model #attribute was missed before "self"
       self.year = year #"self" for missed before attribute

my_car = Car("Toyota", 1988) #   In this instance, the year attribute was missed
print(my_car.model) # correct
print(my_car.year) # correct
# No inheritance

# ----------------------------------------------------------------------------------------------------------------------

# Exercise 4. SmartHome with Constructor

# Create a SmartHome class that has a constructor __init__ and a send_notification() method.
#
# The constructor should initialize the attributes:
# - home_name
# - location
# - number_of_devices
#
# send_notification() should print a notification including the home_name and location.

# Create instances for the following:
# Home Name      Location      Number of Devices
# Villa Rosa     New York      15 devices
# Green House    California    10 devices
# Sea View       Florida       20 devices

# Call the send_notification() method for each instance, 
# passing a message reminding to turn off the lights.
class SmartHome:
    def __init__(self, home_name, location, number_of_devices):
        self.home_name = home_name
        self.location = location
        self.number_of_devices = number_of_devices
    def send_notification(self, home_name, location):
        self.home_name = home_name
        self.location = location
notification_1 = SmartHome("Villa Rosa   ", "New York   ","15 devices" )
notification_2 = SmartHome("Green House  ", "California ", "10 devices")
notification_3 = SmartHome("Sea View     ", "Florida    ", "20 devices")

print('Home name    ', 'Location   ', 'Number of Devices')
print(notification_1.home_name, notification_1.location, notification_1.number_of_devices)
print(notification_2.home_name, notification_2.location, notification_2.number_of_devices)
print(notification_3.home_name, notification_3.location, notification_3.number_of_devices)
# ----------------------------------------------------------------------------------------------------------------------

# Exercise 5. Inheritance. Spot and correct mistakes

# You should have the following hierarchy of classes:

 # Animal
 # │
 # ├── Mammal
 # │
 # ├── Bird
 # │
 # └── Fish

# Each class has the following attributes:

# - Animal name
# - Mammal name, age, number of legs
# - Bird name, age, can fly or not
# - Fish name, age, number of fins

# But, the provided code for these classes and their instances has several mistakes
# related to hierarchy, class attributes, and instance creation.

# Find and correct these mistakes to make the code work properly.
# Leave a comment in the code explaining what the problems were and why it wouldn't work.
# There are seven mistakes in the pre-code.

# Pre-code
class Animal:
    def __init__(self, name, age):
        self.name = name #self before attribute has missing
        self.age = age  # this attribute has not been diclared in the instruction

class Mammal(Animal): # wrong class name
    def __init__(self, name, age, num_legs):
        super().__init__(name, age)
        self.num_legs = num_legs

class Bird(Animal):
    def __init__(self, name, age, can_fly):
        super().__init__(name, age)
        self.can_fly = can_fly  #wrong diclared attribute

class Fish(Animal): # Fish should enheritance from Animal instead of Mammal
    def __init__(self, name, age, num_fins):
        super().__init__(name, age)
        self.num_fins = num_fins


sparrow = Bird('Crow', 2, True) # required arguments not passed
goldfish = Fish('Goldfish', 2, 2) #num fins should be the number instead of word "Many"

