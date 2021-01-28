# variables

# https://www.python.org/dev/peps/pep-0008/#naming-conventions

# can't start with a number or symbol
# can't contain symbols
# can contain numbers
# no whitespaces

is_snowing = True
print(type(is_snowing))

# types: strings, floats, ints, booleans

# user input

# without converting, it is always a string
variable_name = input("Your prompt")

my_age = int(input("What is your age: "))

print(int("10"))
print(str(10))
print(float("4.4"))

# truthy vs. falsey

# False:
bool(False)
bool(0)
bool([])
bool("")
bool({})

# True
bool(True)
bool(3)
bool([6])
bool("g")
bool({6, 5})

# example of using name as a truthy or falsey value
name = input("What is your name?")
if name:
    print("Your name is " + name)
else:
    print("You didn't enter a name!!")

# loops

# for: use when the number of times you want to do something is predetermined
# while: use when you want to do something while a condition is true

# range(4) -> [0, 1, 2, 3] with one number, it starts at 0, and goes up to, but does not include the number you passed in

# range(5, 8) -> [5, 6, 7] with two numbers, it starts at the first number, and goes up to, but does not include the
# second number you passed in

# range(1, 10, 2) -> [1, 3, 5, 7, 9] with three numbers, it starts at the first number, goes up to
# (but does not include) the second number and goes up by step sizes of the third number


# for loop
for i in range(2):
    try:
        x = int(input("Number 1: "))
        break
    except ValueError:
        print("the value was not a number")


# while loop
number = int(input("What is your number? "))
while number < 10:
    number = int(input("What is your number? "))

# lists

# how to create a list
# how to loop through a list
# how to check if something is in a list

# functions
