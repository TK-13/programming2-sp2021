"""
Below, create a function that takes in an age and returns that person's age in days.
(You can ignore the days since their last birthday)
If you finish that.... don't forget about leap years!
Hint: there may be a library to help you out on this.
"""


# user's age in years to days
def days(years):
    age = years * 365
    print("You are " + str(age) + " days old.")


# asks user to enter their age
enter = int(input("How old are you, in years? "))
days(enter)
