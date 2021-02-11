# String Concatenation
# Strings are immutable (cannot change a letter in a string, but you can replace a whole string)
test = "test"
print(test[0])

test = "test2"
print(test)
print()

first_name = "Asher"
last_name = "Mir"
print()
full_name = first_name + " " + last_name
print(full_name)
print()

# Must convert ints to strings to concatenate, or use commas.
num_plants = 42
print("I have " + str(num_plants) + " plants.")
print("I have", str(num_plants), "plants.")
print()

print("hi " * 10)
print()


# Upper and lowercase:
test = "test string"
print(test.lower())
print(test.upper())
print(test.isupper())
print(test.islower())
print(test.capitalize())
print("tPYE".swapcase())
print()

# Substrings
our_string = "The quick brown fox jumps over the lazy dog."
print(our_string[4:9])
print(our_string[-4:-1])

# check for a word:
print("jump" in our_string)
print("jumped" in our_string)

# looping through characters:
for char in our_string:
    print(char)
print()

print(our_string.count("e"))
print()

# .join (important)
test_sentence = ["this", "is", "a", "sentence"]
print(" ".join(test_sentence))
print()

our_string = "The quick brown fox jumps over the lazy dog."
print(our_string.endswith("dog"))
print(our_string[:-1].endswith("dog"))
print()

our_sentence = "I dont want to go outside"
new_sent = our_sentence.replace("dont", "don't")
print(new_sent)
new_sent = our_sentence.replace("dont", "don't").replace("o", "OO")
print(new_sent) # can chain replacements
print()

print("     s p a c i o u s      ".strip())
print("www.example.com".strip("wocm."))
print()

# String formatting with .format()
name = input("What's your name? ")
age = int(input("What's your age? "))
print("Their name is {0} and their age is {1}. {2}".format(name.lower().capitalize(), age, "test addition"))