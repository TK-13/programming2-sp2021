import csv


# This function is just mean to make it easier to put the datasets into a string.
def read_data(path):
    file_for_read = open(path)
    content = file_for_read.read()
    file_for_read.close()
    return content


tally = read_data('/Users/tkmuro/PycharmProjects/tkProgramming/FinalProject/testtest')
print(tally)