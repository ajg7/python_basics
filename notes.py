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

