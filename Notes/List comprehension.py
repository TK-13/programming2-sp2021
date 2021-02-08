# Purpose of comprehension: create lists concisely


# Create list of squares from 1 to 10
squares = []
# Non-comprehension
for i in range(1, 11):
    squares.append(i**2)
print(squares)

# Comprehension
squares = [i**2 for i in range(1, 11)]
print(squares)
print()


# List of all possible die rolls with two six-sided die, then without doubles
# [(1, 1), (1, 2)... ]
# NC
rolls = []
for dice_one in range(1, 7):
    for dice_two in range(1, 7):
        if dice_one != dice_two:
            rolls.append((dice_one, dice_two))

print(rolls)

# Comprehension
rolls = [(dice_one, dice_two) for dice_one in range(1, 7) for dice_two in range(1, 7) if dice_one != dice_two]
print(rolls)
print()


# List of 10 random numbers, with list comprehension
import random
random_numbers = [random.randint(0, 20) for i in range(10)]
print(random_numbers)
print()

# List of even numbers
evens = [i for i in range(2, 11, 2)]
print(evens)
print()

n_squared = [(i, i**2) for i in range(10)]
n_squared1 = [(i, j**2) for i in range(10) for j in range(i, i+1)]
print(n_squared)
print(n_squared1)
print()

evens2 = [i for i in range(1, 11) if i % 2 == 0]
print(evens2)
