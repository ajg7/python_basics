# This is a comment
# how to "console.log" in python
print("hello World")

# White Space

school = "Lambda"
if school == "Lambda":
    # indentation of four spaces
    print("school is 'Lambda'.")
    
# Integers, floats, and strings

my_int = 3

my_int = int(3.0) # 3

my_float = 4.3
my_float = float(3) # 3.0

a_float = 5.4
new_int = int(5.4)
print(new_int)

my_string = "I don't have to worry about apostrophes with my double-quotes."

# List Operations

my_list = [] # empty list literal
my_list.append(1) # add 1 to end of list
my_list.append(2) # add 2 to end of list
my_list.append(3) # add 3 to end of list
print(my_list[0]) # prints 1
print(my_list[1]) # prints 2
print(my_list[2]) # prints 3

# For loop
for item in my_list:
    print(item)
    

# Basic Operators

my_number = 2 + 2 * 8 / 5.0
print(my_number) # 5.2

my_remainder = 9 % 4
print(my_remainder) # 1

two_squared = 2 ** 2
print(two_squared)    # 4
two_cubed = 2 ** 3
print(two_cubed)      # 8

# Concatenation
string_one = "Hello,"
string_two = " World!"
combined = string_one + string_two
print(combined) # Hello, World!

lst_one = [1,2,3]
lst_two = [4,5,6]
big_lst = lst_one + lst_two
print(big_lst) # [1, 2, 3, 4, 5, 6]

# Repeating a Sequence
my_string = "Bueller"
repeated = my_string * 3
print(repeated) # BuellerBuellerBueller

# Formatted Strings
#use %s for strings, %d for ints, %f for floats, & %x for ints in hexadecimal
name = "Austen"
year = 2020
print("Hey %s! It's the year %d." % (name, year))
# Hey Austen! It's the year 2020.

# String Operations

#len() prints out the number of characters in a string
my_second_string = "Neeee"
print(len(my_second_string)) #5

#index prints out the index of the substring argument's first occurence
my_string = "Hello, world!"
print(my_string.index("o"))   # 4
print(my_string.index(", w")) # 5

#count returns the number of occurrences of the substring argument
my_string = "Hello, world!"
print(my_string.count("o"))  # 2
print(my_string.count("ll")) # 1

# Slicing a string ([start:stop:step])
my_string = "Hello, world!"
print(my_string[3:7])   # lo,
print(my_string[3:7:2]) # l,

# Reverse a string's order
print(my_string[::-1])  #!dlrow ,olleH

#Convert a string to Uppercase or Lowercase
my_string = "Darkness"
my_string.upper()
my_string.lower()

#Determine if a string starts with or ends with a specific sequence
my_string = "Hello, world!"
print(my_string.startswith("Hello")) # True
print(my_string.endswith("globe!"))  # False

#Splitting a string into a list
my_string = "Hello, world!"
print(my_string.split())    # ['Hello,', 'world!']
print(my_string.split(",")) # ['Hello', ' world!']
print(my_string.split("l")) # ['He', '', 'o, wor', 'd!']

# Conditionals and Booleans 
# ==, <, >, <=, >=, !=

my_name = "AJ"
my_last_name = "Gebara"

if name == "AJ" and my_last_name == "Brown":
    print("Darkness")
elif name == "Gebara" or my_last_name == "Kevin":
    print("Darkness")
else:
    print("python is cool")
    
# Using a conditional in an interable object
years = [2018, 2019, 2020, 2021]
year = 2020

if year in years:
    print("%s is in the years collection" % year)

# 2020 is in the years collection

# not Operator
print(not (1 == 1)) # False because 1 == 1 is True and then is inverted by not

# While Loop

count = 2
while count < 7:
    print(count)
    count += 1
    
# break allows you to exit a loop
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

#continue allows you to skip the current block but not exit the loop entirely
for x in range(8):
    # if x is even, skip this block and do not print
    if x % 2 == 0:
        continue
    print(x)
    
# List Comprehensions
sentence = "Every moment is a fresh beginning."
words = sentence.split()
word_lengths = [len(word) for word in words]

print(word_lengths)


numbers = [1,2,3,4,5,6,7,8,9,10]
even_numbers = [number for number in numbers if number % 2 == 0]

print(even_numbers)

# Functions and Encapsulation
def example(input):
    print(input)

example("Straight outta Compton")

def another_example(input1, input2):
    print("I am %s %s" % (input1, input2))
    
another_example("AJ", "Gebara")

#Classes
class MyFirstClass:
    variable = "data"
    
    def function(self):
        return "Printing from a MyFirstClass object"
    
a_class_object = MyFirstClass()
print(a_class_object.variable)

class Animal:
    name = "Kangaroo"
    kind = "Marsupial"
    color = "Pink"
    
    def description(self):
        return "%s is a %s %s." % (self.name, self.color, self.kind)
    
animal_object = Animal()
print(animal_object.name, animal_object.kind, animal_object.color)

#Basic Dictionary Operations
# Key/value pair
# Essentially dictionary is to object as list is to array

phonebook = {}
phonebook["Ryan"] = 2345432
phonebook["Mary"] = 9992234
# or
phonebook = {
    "Ryan": 5678923,
    "Mary": 2345678
}

#iterate through dictionary
for name, number in phonebook.items():
    print("Name: %s, Number: %s" % (name, number))

# Name: Abe, Number: 4569874321
# Name: Bill, Number: 7659803241
# Name: Barry, Number: 6573214789

#Remove item
del phonebook["Ryan"]
#or
phonebook.pop("Mary")
#pop returns the deleted value unlike del

#Importing in Python
#Any file that ends in .py is considered a module

import math

print(math.factorial(5))

#Importing a specific file
from math import factorial

print(factorial(5))
# 120

#import all the names from a module
from math import *

print(factorial(5))
# 120
print(pow(2, 3))
# 8.0

#To find out which names a module defines when imported you can use the dir()