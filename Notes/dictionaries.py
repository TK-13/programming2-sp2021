# this will be a self-guided exploration of dictionaries
# feel free to comment/uncomment as you go to only run certain parts of the code
# please feel free to ask questions though to one another or to Ms. Ifft as you're going through

from pprint import pprint
import csv


# this will create a list of dictionaries
print("\n\nPrinting a dictionary per row of roster.csv: ")
class_data = open('../Resources/roster.csv')
dict_reader = csv.DictReader(class_data)
for row_dict in dict_reader:
    pprint(row_dict)

"""
Question: From this print statement, what do you think a dictionary is?

Answer: <insert your answer here>

"""

# let's create an example dictionary

pet_dict = {
    "Name": "Forrest",
    "Animal": "Cat",
    "Favorite Food": "Chicken",
    "Hours of Sleep": 16,
    "Best Friend": "Ainsley"
}

print(pet_dict)
pprint(pet_dict)

"""
Question: What does pprint do? Why might you use it? What do you notice about key order, and
what does that tell you?

Answer: <insert your answer here>

"""

# to retrieve a value from a dictionary, you can use [] with the key name

# Example:
print("\n")
print('pet_dict["Name"]:', pet_dict["Name"])

"""
Question: Knowing this, how could you add code starting at line 15 to store the
dictionary that corresponds to your information to a variable named my_dict?

Answer: add your code above instead of answering here.

"""

# let's see what happens when we try to access the Age of my pet
# (feel free to comment this out later to not break your code--or fix it!)

print('pet_dict["Age"]:', pet_dict["Age"])

"""
Question: What happens, and what do you think it means?

Answer: <insert your answer here>

"""

# we might not know for sure if a key exists in a dictionary, and we want to handle it more gracefully

print("\nUsing .get():")
print(pet_dict.get("Age"))
print(pet_dict.get("Age", "This key doesn't exist!!"))

"""
Question: What do you think .get() does? What happens if we do or don't specify a second parameter?

Answer: <insert your answer here>

"""

# similar to the way we access elements we know exist, we can add new elements to our dictionary with []

# Example:

pet_dict["Age"] = 2

print("\n")
print(pet_dict["Age"])

"""
Question: What can you gather about the types of variables within a dictionary?

Answer: <insert your answer here>

"""

# let's pretend Forrest had a birthday!
pet_dict["Age"] = 3

print("\n")
pprint(pet_dict)

"""
Question: What do you notice about the Age value(s) in the dict, and what does this tell you
about how many entries per key a dictionary can have? What might you do if you want to store
multiple entries under one key?

Answer: <insert your answer here>

"""


"""
okay, you learned a lot! now complete the following steps:
1. print my_dict with print and with pprint
2. print a statement that includes your first name and last name, taken from my_dict
3. add your age to my_dict and print my_dict again
4. let's pretend you had a birthday! update your age in my_dict and print my_dict again
5. try to access a key that doesn't exist, and print a joke if/when the code can't find it
6. try out or add anything else to my_dict that would help you in understanding dictionaries
"""

# erase this and insert your code for steps 1 through 5 here :)


# the last thing we need to learn is how to iterate over dictionaries
# spend some time understanding what the following code blocks do, and how they differ

print("\nIterating over dictionaries\n")

for key in pet_dict:
    print(key, ":", pet_dict[key])

print()

for key in pet_dict.keys():
    print(key, ":", pet_dict[key])

print()

for value in pet_dict.values():
    print(value)

print()

for key, value in pet_dict.items():
    print(key, ":", value)

print()


"""
Question: What are the different ways for iterating over a dictionary, and when might each
one be useful?

Answer: <insert your answer here>

"""

# now write some code below to iterate over my_dict




