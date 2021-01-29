"""
Fibonacci Sequence
Below, have the user enter a number and have your code generate the Fibonacci sequence to that number.
If you complete that, also give them the option to input a number N, and generate the sequence to the Nth number.
"""

# 0, 0, 1, 2,

# there was an attempt

number = int(input("Enter a number: "))
fibonacci = 0
interval = 1

for i in range(0, 10):
    fibonacci += interval
    print(fibonacci)
    # interval += fibonacci