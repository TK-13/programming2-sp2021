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

Answer: A dictionary is a way of reading csv's/sorting information by set categories.

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

Answer: pprint prints dictionaries vertically, rather than horizontally like a normal print 
statement. It seems to differentiate each line by the preestablished categories of the dictionary,
and sorts them alphabetically.

"""

# to retrieve a value from a dictionary, you can use [] with the key name

# Example:
print("\n")
print('pet_dict["Name"]:', pet_dict["Name"])

# My Code
print()
my_dict = {}
class_data = open('../Resources/roster.csv')
dict_reader = csv.DictReader(class_data)
for row_dict in dict_reader:
    if row_dict["First Name"] == "TK":
        my_dict = row_dict
pprint(my_dict)

"""
Question: Knowing this, how could you add code starting at line 15 to store the
dictionary that corresponds to your information to a variable named my_dict?

Answer: add your code above instead of answering here.
"""


# let's see what happens when we try to access the Age of my pet
# (feel free to comment this out later to not break your code--or fix it!)

print()
print('pet_dict["Age"]:', pet_dict.get("Age"))

"""
Question: What happens, and what do you think it means?

Answer: Because age isn't a specified category, there is no value associated with it, so python
will throw an error.

"""

# we might not know for sure if a key exists in a dictionary, and we want to handle it more gracefully

print("\nUsing .get():")
print(pet_dict.get("Age"))
print(pet_dict.get("Age", "This key doesn't exist!!"))

"""
Question: What do you think .get() does? What happens if we do or don't specify a second parameter?

Answer: .get() seems similar to the try/except system, where it behaves like the code normally would
without .get, but adds an extra countermeasure in case the code (or in this case, dictionary value access)
doesn't work. Without a specified error message, it will just print "None."

"""

# similar to the way we access elements we know exist, we can add new elements to our dictionary with []

# Example:

pet_dict["Age"] = 2

print("\n")
print(pet_dict["Age"])

"""
Question: What can you gather about the types of variables within a dictionary?

Answer: The keys seem to need to be strings, but the associated values can be strings or integers.

"""

# let's pretend Forrest had a birthday!
pet_dict["Age"] = 3

print("\n")
pprint(pet_dict)

"""
Question: What do you notice about the Age value(s) in the dict, and what does this tell you
about how many entries per key a dictionary can have? What might you do if you want to store
multiple entries under one key?

Answer: Dictionaries can only have one entry per key. If a key's value is re-declared as something else, it changes
the original value rather than adding a new key. To store multiple entries under one key, we could probably use a list
or even another dictionary.
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

print()
print()
print("Step 1: ")
print(my_dict)
print()
pprint(my_dict)

print()
print("Step 2:")
print(my_dict["First Name"], my_dict["Last Name"])

print()
print("Step 3:")
my_dict["Age"] = 18
print(my_dict)

print()
print("Step 4:")
my_dict["Age"] = 19
print(my_dict)

print()
print("Step 5:")
print(my_dict.get("Birthday", "That key does not exist. *insert joke here*"))

print()
print("Step 6:")
my_dict["Favorite Animals"] = ["Red Panda", "Tardigrade", "Cat"]
print("First favorite: ", my_dict["Favorite Animals"][0])
for item in my_dict["Favorite Animals"]:
    print(item)


# the last thing we need to learn is how to iterate over dictionaries
# spend some time understanding what the following code blocks do, and how they differ

print("\nIterating over dictionaries\n")

# Iterates through every key in the dictionary.
for key in pet_dict:
    print(key, ":", pet_dict[key])
print()

# Ditto, but maybe the search is more efficient?
for key in pet_dict.keys():
    print(key, ":", pet_dict[key])
print()

# Iterates through all entry values in dictionary.
for value in pet_dict.values():
    print(value)
print()

# Iterates through every key-value pair in the dictionary.
for key, value in pet_dict.items():
    print(key, ":", value)
print()


"""
Question: What are the different ways for iterating over a dictionary, and when might each
one be useful?

Answer: Dictionaries can be iterated over by their keys, their values, or both. 

Iterating over each key could be useful when you only need to know the sorting categories, maybe if you need to reset 
all the values in a dictionary. 

Alternatively, iterating over each value could be useful if you don't know/need the categories (not sure what scenario 
would require that). 

Using .items() to iterate through each key-value pair seems to be the most efficient option; even
if you want to find a specific value and replace it, using .values() would't tell you which key contains the desired
value, so you would have to use .items() or .keys().

"""

# now write some code below to iterate over my_dict
for k, v in my_dict.items():
    if k == "Favorite Animals":
        print("Their", k, "are", v)
    else:
        print("Their", k, "is", v)
