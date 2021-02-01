"""
Fibonacci Sequence
Below, have the user enter a number and have your code generate the Fibonacci sequence to that number.
If you complete that, also give them the option to input a number N, and generate the sequence to the Nth number.
"""

num = int(input("What number would you like your fibonacci sequence to go up to? "))

fib_1 = 0
fib_2 = 1

print(fib_1)
print(fib_2)

while fib_2 + fib_1 < num:
    print(fib_1 + fib_2)
    temp_fib_1 = fib_1
    fib_1 = fib_2
    fib_2 += temp_fib_1


n = int(input("How many fibonacci numbers would you like to see? "))

fib_1 = 0
fib_2 = 1

if n >= 1:
    print(fib_1)

if n >= 2:
    print(fib_2)

for i in range(n-2):
    print(fib_1 + fib_2)
    temp_fib_1 = fib_1
    fib_1 = fib_2
    fib_2 += temp_fib_1
