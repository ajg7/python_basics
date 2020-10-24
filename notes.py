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