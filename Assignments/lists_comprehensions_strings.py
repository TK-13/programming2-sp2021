# import some text we'll use later
import nltk
nltk.download('gutenberg')
nltk.download('genesis')
nltk.download('inaugural')
nltk.download('webtext')
nltk.download('treebank')
nltk.download('nps_chat')
from nltk.book import text6
monty_python = list(text6)

# import a number list
from Assignments import number_list
num_list = number_list.num_list
print(num_list)

# ____________________________________________________________________________________________________________________ #

# LISTS, LIST COMPREHENSIONS & STRING OPERATIONS (32 pts)

# PROBLEM 1 (Basic list operations - 4 pts)
my_family = ["Steven", "Julie", "Chantel", "Autumn", "Joel"]
our_pets = ["Marshmallow", "Kitty", "Rylee", "Forrest", "Eleanor"]
# Create a copy of our_pets, and add "Ainsley" to it (1 pt)
# Use two different list slicings to print ['Steven', 'Julie'] (1 pts)
# Merge the two lists together and store it in our_big_family (1 pt)
# Merge the two lists together in a way such that the merged list ends up in my_family (1 pt)


# PROBLEM 2 (List functions and methods - 8 pts)
# Find and print the highest number in num_list (1 pt)
# Find and print the lowest number in num_list (1 pt)
# Find and print the average of num_list (2 pts)
# Remove the lowest number from num_list (2 pts)
# Create and print a new list called top_ten which contains only the 10 highest numbers in num_list (2 pts)


# PROBLEM 3 (Using list comprehensions with numbers - 8 pts)
# Use list comprehensions to do the following:
# a) Make a list of numbers from 1 to 100 (2 pts)
# b) Make a list of even numbers from 20 to 40 (2 pts)
# c) Make a list of squares from 1 to 100 (1 ** 2 to 100 ** 2) (2 pts)
# d) Make a list of all positive numbers in my_list below. (2 pts)
my_list = [-77, -78, 82, 81, -40, 2, 62, 65, 74, 48, -37, -52, 90, -84, -79, -45, 47, 60, 35, -18]


# PROBLEM 4 (4 pts)
# Find the number which appears most often in num_list?


# PROBLEM 5 (Text manipulation - 8 pts)
# a) Create one string of the first 75 elements of monty_python separated by a space (2 pts)
# b) Using your string from part a) remove erroneous spaces before (and after) punctuation (2 pts)
# Use list comprehensions to do the following with monty_python:
# c) Make a list of the words in monty_python that are 12 or 13 characters long (2 pts)
# d) Make a list of the lowercase version of the words in monty_python that appear in all caps (2 pts)

# ____________________________________________________________________________________________________________________ #