"""
Activity 1 - all together

Read the courses from courses.txt in the Resources file.
Then, remove the courses titled Remotely Operated Vehicle Robotics
and Robotics, and replace them with a course called Engineering I: Introduction to Engineering.
Make sure the changes are saved back to courses.txt
"""

# erase this and write your code here!
courses_to_read = open('../Resources/courses.txt', "r")
courses = courses_to_read.readlines()
print(courses)
for i in range(len(courses)):
    if courses[i] == "Remotely Operated Vehicle Robotics" or courses[i] == "Robotics":
        courses[i] == ""

print(courses)


"""
Activity 2 - separate tasks, then merge together

A class of students have been studying the countries and their capitals.
There are 196 potential countries, but they will only be asked 25 at random.
Together, you and your partner are going to generate a quiz for a student to take. 

PARTNER 1:
Read the countries and capitals in from countries_and_capitals.csv in the Resources file.
Store it in a 2-dimensional list without the header row. For example:

[["Afghanistan", "Kabul"],
 ["Albania", "Tirana"],
 ...
 ["Zimbabwe", "Harare"]]


PARTNER 2:
Assume you will receive a 2-dimensional list similar to what's shown above.
Randomly select 25 Countries and their capitals. 
Write code that will loop through those countries and capitals, 
and ask the user which country has a capital of the given capital. 
Write their answers and the correct answer to a file called answers.csv in the following format:

User Answer,Correct Answer
Sweden, Sweden
Argentina, Colombia
...


TOGETHER:

!!!!! do not move onto this until both tasks above are completed !!!!!
!!!!! if you need to help each other out to finish those tasks first, please do so !!!!!

Merge your code, and then work on the final task:
Modify your code to read the countries and capitals into a dictionary instead of a list of lists.
For example:

{
    "Afghanistan": "Kabul",
    "Albania": "Tirana",
    ...
    "Zimbabwe": "Harare"
}

Although this is a structural change in your code, the functionality of your code should not change
as a results of this modification. Please make all the necessary modifications for your code to 
function the same as it did with the list of lists.

"""

# erase this and write your code here!

