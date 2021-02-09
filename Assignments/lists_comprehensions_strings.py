# import some text we'll use later
import nltk
from nltk.book import text6
from Assignments import number_list

nltk.download('gutenberg')
nltk.download('genesis')
nltk.download('inaugural')
nltk.download('webtext')
nltk.download('treebank')
nltk.download('nps_chat')
monty_python = list(text6)

# import a number list
num_list = number_list.num_list
print(num_list)
print()
print()

# ____________________________________________________________________________________________________________________ #

# LISTS, LIST COMPREHENSIONS & STRING OPERATIONS (32 pts)

# PROBLEM 1 (Basic list operations - 4 pts)
print("PROBLEM 1 (Basic list operations - 4 pts)")
my_family = ["Steven", "Julie", "Chantel", "Autumn", "Joel"]
our_pets = ["Marshmallow", "Kitty", "Rylee", "Forrest", "Eleanor"]
# Create a copy of our_pets, and add "Ainsley" to it (1 pt)
pets2 = our_pets.copy()
print("Original:", pets2)
pets2.append("Ainsley")
print("New: ", pets2)
print()


# Use two different list slicing variations to print ['Steven', 'Julie'] (1 pts)
# Option 1:
print(my_family[:2])
print()

# Option 2:
print(my_family[-5:-3])
print()

# Merge the two lists together and store it in our_big_family (1 pt)
our_big_family = my_family + pets2
print("our_big_family: ", our_big_family)
print()

# Merge the two lists together in a way such that the merged list ends up in my_family (1 pt)
my_family += pets2
print("my_family: ", my_family)
print()
print()
print()


# PROBLEM 2 (List functions and methods - 8 pts)
# Find and print the highest number in num_list (1 pt)
print("PROBLEM 2 (List functions and methods - 8 pts)")
print("Highest number in num_list", int(max(num_list)))
print()

# Find and print the lowest number in num_list (1 pt)
print("Lowest number in num_list", int(min(num_list)))
print()

# Find and print the average of num_list (2 pts)
print("Average of num_list: ", (sum(num_list) / len(num_list)))
print()

# Remove the lowest number from num_list (2 pts)
print(num_list)
num_list.remove(min(num_list))
print(num_list)
print()

# Create and print a new list called top_ten which contains only the 10 highest numbers in num_list (2 pts)
top_ten = []
ten_copy = num_list.copy()
ten_copy.sort()
ten_copy.reverse()

for r in range(10):
    top_ten.append(ten_copy[r])
print("Top 10 highest values in num_list:", top_ten)
print()
print()
print()


# PROBLEM 3 (Using list comprehensions with numbers - 8 pts)
# Use list comprehensions to do the following:
# a) Make a list of numbers from 1 to 100 (2 pts)
print("PROBLEM 3 (Using list comprehensions with numbers - 8 pts)")
list_a = [i for i in range(1, 101)]
print("List of numbers from 1 to 100: ", list_a)
print()

# b) Make a list of even numbers from 20 to 40 (2 pts)
list_b = [i for i in range(19, 42) if i % 2 == 0]
print("Even #'s from 20 to 40: ", list_b)
print()

# c) Make a list of squares from 1 to 100 (1 ** 2 to 100 ** 2) (2 pts)
list_c = [q**2 for q in range(1, 100)]
print("List of squares from 1 to 100: ", list_c)
print()

# d) Make a list of all positive numbers in my_list below. (2 pts)
my_list = [-77, -78, 82, 81, -40, 2, 62, 65, 74, 48, -37, -52, 90, -84, -79, -45, 47, 60, 35, -18]
print("my_list:", my_list)
list_d = [item for item in my_list if item > 0]
print("Positive numbers in my_list:", list_d)
print()
print()
print()

# PROBLEM 4 (4 pts)
# Find the number which appears most often in num_list?
print("PROBLEM 4 (4 pts)")
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
print()
print()

# PROBLEM 5 (Text manipulation - 8 pts)
# a) Create one string of the first 75 elements of monty_python separated by a space (2 pts)
print("PROBLEM 5 (Text manipulation - 8 pts)")
elements = ""
for q in range(75):
    elements += monty_python[q]
    elements += " "
print("First 75 elements of monty_python:", elements)
print()

# b) Using your string from part a) remove erroneous spaces before (and after) punctuation (2 pts)
# Note: I used this site to find the right methods: https://www.w3schools.com/python/python_ref_string.asp
# Got help from Ms. Ifft on how to use replace()

# for future reference: replace() only prints automatically in console. Returns the new result, so you have
# to set the original equal to the replaced version (elements = elements.replace...)
targets = ["[ ", " ]", " .", " ,", " !", " ?", "# ", " :"]
replacements = ["[", "]", ".", ",", "!", "?", "#", ":"]
for p in range(len(targets)):
    elements = elements.replace(targets[p], replacements[p])
print(elements)
print()

# Use list comprehensions to do the following with monty_python:
# c) Make a list of the words in monty_python that are 12 or 13 characters long (2 pts)
long_words = [word for word in monty_python if (len(word) == 12 or len(word) == 13)]
print("Words in monty_python that are 12-13 characters long:", long_words)
print()

# d) Make a list of the lowercase version of the words in monty_python that appear in all caps (2 pts)
all_caps = [char.lower() for char in monty_python if char != char.lower()]
print("Words in monty_python in all-caps (made lowercase): ", all_caps)
