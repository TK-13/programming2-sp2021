"""
Reverse a String - See if you can write a function that takes in a string, and returns the reversed version.
If you complete that, tell the user if their word is a palindrome.
A hint is that strings can be manipulated similarly to lists :)
"""


def reversal(enter):
    reversed_string = ""
    for i in range(len(enter)):
        reversed_string += enter[int(len(enter) - i)]
    print(reversed_string)


reversal("Hello")