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
print()
print()

# ____________________________________________________________________________________________________________________ #

# LISTS, LIST COMPREHENSIONS & STRING OPERATIONS (32 pts)

# PROBLEM 1 (Basic list operations - 4 pts)
my_family = ["Steven", "Julie", "Chantel", "Autumn", "Joel"]
our_pets = ["Marshmallow", "Kitty", "Rylee", "Forrest", "Eleanor"]
# Create a copy of our_pets, and add "Ainsley" to it (1 pt)
pets2 = our_pets.copy()
print("Original:", pets2)
pets2.append("Ainsley")
print("New: ", pets2)
print()


# Use two different list slicings to print ['Steven', 'Julie'] (1 pts)
# Option 1:
print(my_family[:2])

# Option 2:
print(my_family[-5:-3])

# Merge the two lists together and store it in our_big_family (1 pt)
our_big_family = my_family + pets2
print("our_big_family: ", our_big_family)

# Merge the two lists together in a way such that the merged list ends up in my_family (1 pt)
my_family += pets2
print("my_family: ", my_family)
print()
print()


# PROBLEM 2 (List functions and methods - 8 pts)
# Find and print the highest number in num_list (1 pt)
print("Highest number in num_list", int(max(num_list)))

# Find and print the lowest number in num_list (1 pt)
print("Lowest number in num_list", int(min(num_list)))

# Find and print the average of num_list (2 pts)
print("Average of num_list: ", (sum(num_list) / len(num_list)))

# Remove the lowest number from num_list (2 pts)
print(num_list)
num_list.remove(min(num_list))
print(num_list)

# Create and print a new list called top_ten which contains only the 10 highest numbers in num_list (2 pts)
top_ten = []
ten_copy = num_list.copy()
ten_copy.sort()
ten_copy.reverse()

for r in range(10):
    top_ten.append(ten_copy[r])
print("Top 10 highest values:", top_ten)
print()


# PROBLEM 3 (Using list comprehensions with numbers - 8 pts)
# Use list comprehensions to do the following:
# a) Make a list of numbers from 1 to 100 (2 pts)
list_a = []
for i in range(100):
    list_a.append(int(i+1))
print("List of numbers from 1 to 100: ", list_a)

# b) Make a list of even numbers from 20 to 40 (2 pts)
list_b = []
for i in range(19, 42):
    if i % 2 == 0:
        list_b.append(i)
print("Even #'s from 20 to 40: ", list_b)

# c) Make a list of squares from 1 to 100 (1 ** 2 to 100 ** 2) (2 pts)
list_c = []
for i in range(100):
    list_c.append(int((i+1) ** 2))
print("List of squares from 1 to 100: ", list_c)

# d) Make a list of all positive numbers in my_list below. (2 pts)
my_list = [-77, -78, 82, 81, -40, 2, 62, 65, 74, 48, -37, -52, 90, -84, -79, -45, 47, 60, 35, -18]
print("my_list:", my_list)
list_d = []
for i in my_list:
    if i > 0:
        list_d.append(i)
print("Positive numbers in my_list:", list_d)

# PROBLEM 4 (4 pts)
# Find the number which appears most often in num_list?
print("num_list:", num_list)
count_test = 0
most_often = 0

for x in num_list:
    if num_list.count(x) > count_test:
        count_test = num_list.count(x)
        most_often = x
print("Number which appears most often in num_list:", most_often)
print("Frequency:", count_test)
print()

# PROBLEM 5 (Text manipulation - 8 pts)
# a) Create one string of the first 75 elements of monty_python separated by a space (2 pts)
elements = ""
for q in range(75):
    elements += monty_python[q]
    elements += " "
print("First 75 elements of monty_python:", elements)

# b) Using your string from part a) remove erroneous spaces before (and after) punctuation (2 pts)
print("Finish B !!!")
# Use list comprehensions to do the following with monty_python:
# c) Make a list of the words in monty_python that are 12 or 13 characters long (2 pts)
long_words = []
for c in monty_python:
    if len(c) == 12 or len(c) == 13:
        long_words.append(c)
        if long_words.count(c) > 1:
            long_words.remove(c)

print("Words in monty_python that are 12-13 characters long:", long_words)

# d) Make a list of the lowercase version of the words in monty_python that appear in all caps (2 pts)

# ____________________________________________________________________________________________________________________ #