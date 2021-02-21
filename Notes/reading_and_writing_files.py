from pprint import pprint
import csv

# https://automatetheboringstuff.com/2e/chapter9/

# FILE PATHS ---------------------------------------------------------

# absolute vs. relative

# ABSOLUTE -> /Users/bifft/PycharmProjects/programming2-sp2021/Notes/test_file.txt
# RELATIVE -> ./test_file.txt or just test_file.txt

# . = this directory and .. = parent directory

# ABSOLUTE -> /Users/bifft/PycharmProjects/programming2-sp2021/Resources/courses.txt
# RELATIVE -> ../Resources/courses.txt

# TODO: show how refactor works with test_file.txt


# READING A TEXT FILE ------------------------------------------------

# you can only use read or readlines once...
# then you will have to re-open the file

# read the whole file into one string
courses_file_for_read = open('../Resources/courses.txt')
courses_content = courses_file_for_read.read()
print(courses_content)

# read the file into a list, one list element for each line in the file
courses_file_for_readlines = open('../Resources/courses.txt')
courses = courses_file_for_readlines.readlines()
print(courses)


# WRITING TO A TEXT FILE ----------------------------------------------

# open a file in write or append mode

names_file_for_writing = open('../Resources/names.txt', 'w')  # overrides whatever is currently in the file
names_file_for_writing.write('Ms. Ifft\n')
names_file_for_writing.write('Adrian\n')
names_file_for_writing.write('Dale\n')
names_file_for_writing.write('Lorenzo\n')
names_file_for_writing.write('Rebecca\n')
names_file_for_writing.write('Ryan\n')
names_file_for_writing.close()

names_file_for_appending = open('../Resources/names.txt', 'a')  # appends to the end of the file
names_file_for_appending.write('\n')
names_file_for_appending.write('Aaron\n')
names_file_for_appending.write('Alex\n')
names_file_for_appending.write('Ryan\n')
names_file_for_appending.write('Tk\n')
names_file_for_appending.close()



# https://automatetheboringstuff.com/2e/chapter16/

# READING A CSV FILE (LISTS) ------------------------------------------

# reading the data into a list of lists
roster_data = open('../Resources/roster.csv')
reader = csv.reader(roster_data)
roster_data_lists = list(reader)
print(roster_data_lists)
roster_data.close()

# reading in the data via a for loop
roster_data = open('../Resources/roster.csv')
reader = csv.reader(roster_data)
for row in reader:
    print('Row #' + str(reader.line_num) + ' ' + str(row))

# remember you can only use a reader once! This won't work.
roster_data_lists = list(reader)
print(roster_data_lists)

roster_data.close()


# WRITING TO A CSV FILE -----------------------------------------------

output_file = open('my_output.csv', 'w')
output_writer = csv.writer(output_file)
output_writer.writerow(['First Name', 'Last Name', 'Grade', 'Email Address'])
output_writer.writerow(['Aaron', 'Rothman', 12, 'arothman@fwparker.org'])
output_writer.writerow(['Alex', 'Schapiro', 12, 'aschapiro@fwparker.org'])
output_writer.writerow(['Ryan', 'Kershner', 10, 'rKershner@fwparker.org'])
output_writer.writerow(['TK', 'Muro', 12, 'tmuro@fwparker.org'])
output_file.close()


# READING A CSV FILE (DICTS) ------------------------------------------

class_data = open('my_output.csv')
dict_reader = csv.DictReader(class_data)
for row_dict in dict_reader:
    pprint(row_dict)

