import csv

pdf_tally_path = '/Users/tkmuro/PycharmProjects/tkProgramming/FinalProject/testtest.txt'

# This function is just mean to make it easier to put the datasets into a string.
def read_data(path):
    file_for_read = open(path)
    content = file_for_read.read()
    file_for_read.close()
    return content


tally = int(read_data(pdf_tally_path))
print(tally)
tally += 1
print(tally)

tally_rewrite = open(pdf_tally_path, 'w')
tally_rewrite.write(str(tally))
tally_rewrite.close()
