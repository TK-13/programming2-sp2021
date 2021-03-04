"""
Inauguration Speeches (25 pts)
This lab is largely review of: lists, comprehensions, and string methods.
The new items here are reading and writing to files, and using a dictionary (dict).
We will use list, dictionary, and string skills to do a basic comparison of the Trump and Biden inauguration speeches.
Your job will be to find the 25 most common words in each speech (disregarding stop words), and then do a comparison of words that appear in one but not the other, and vice versa.
Then you'll write your results to a txt file (see format below).
A common Python pattern to count objects, produce histograms, or update stats is to make calls to a dictionary as you iterate through a list.
For example, given a list of words, you can create a dictionary to store word counts and then iterate through the list of words, updating the dictionary count for each word each time you've seen it.
"""

# PSEUDO CODE
# Get text from biden.txt and trump.txt and
# split the transcripts into words - Use split and strip methods and store results in lists.
# Remove the stop words from the transcripts by checking if the transcript words are in stop_words (8 pts)

# Create dictionary objects to store the word counts
# Iterate through the list/text of each speech and update word counts on your dicts (7 pts)
#    {'word1': 5, 'word2': 2 ...}
# Sort words by counts in descending order (5 pts)  stackoverflow probably?
# Create a text file with the following format:
'''
Top 25 Trump words:
america: 18
american: 11
...

Top 25 Biden words:
us: 25
america: 17
...

Words in Trump, but not Biden:
clinton
bush
obama
...

Words in Biden, but not Trump:
vice-president
harris
speaker
...
'''

# Write this file to the FilesAndDictionaries folder with the name inaugural_counts.txt (5 pts)


# 2 points extra credit --------------------------------------------------------------------------
# Create a csv file with your word counts named inaugural_counts.csv in the following format:
"""
Word,Biden Count,Trump Count
america,17,18
us,25,2
...
"""
# The file should be ordered by the sum of times seen in Trump's speech + times seen in Biden's speech
# in descending order
# You will likely need to use stackoverflow to do this ^
# --------------------------------------------------------------------------------------------------

import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
stop_words = stopwords.words()

complete_list = []
sorted_dict = {}

# Used this: https://python-reference.readthedocs.io/en/latest/docs/str/rstrip.html


def thresh(abs_path):
    transcript = open(abs_path)
    reading = transcript.read()
    punct_filter = [item.strip("', .?:!- ") for item in reading.split()]
    apostrophe_filter = []
    for words in punct_filter:
        for letters in range(len(words)):
            words = words.replace("'s", "")\
                .replace("'ve", "")\
                .replace("'ll", "")\
                .replace("'re", "")\
                .replace("'t", "")\
                .replace("'m", "")\
                .replace(" ", "")
        apostrophe_filter.append(words)
    for item in apostrophe_filter:
        if item.isnumeric():
            apostrophe_filter.remove(item)

    stop_word_filter = [words for words in apostrophe_filter if
                        words.lower() not in stop_words and words.lower() != '-']
    global complete_list
    complete_list = [words.lower() for words in stop_word_filter]

    # print("{0} List:".format(name), complete_list)

    # Appends each word and it's count to a dictionary, without redundant key entries.
    tracking = []
    counting_dictionary = {}
    for item in complete_list:
        if item not in tracking:
            counting_dictionary[item] = complete_list.count(item)
            tracking.append(item)

    ''' For this section, I had to consult stackabuse
    https://stackabuse.com/how-to-sort-dictionary-by-value-in-python/ '''
    sorted_values = sorted(counting_dictionary.values())  # Sort the values
    sorted_values.reverse()  # since the instructions call for descending order, the order of this
    # list had to be reversed.
    global sorted_dict
    sorted_dict = {}
    for i in sorted_values:
        for k in counting_dictionary.keys():
            if counting_dictionary[k] == i:
                sorted_dict[k] = counting_dictionary[k]
                # break
                ''' this break value caused there to only be one key in sorted_dict with the associated
                count, so that had to be removed. '''
    print()


thresh("/Users/tkmuro/PycharmProjects/tkProgramming/Assignments/FilesAndDictionaries/biden.txt")
biden_sorted = sorted_dict
thresh("/Users/tkmuro/PycharmProjects/tkProgramming/Assignments/FilesAndDictionaries/trump.txt")
trump_sorted = sorted_dict

word_counts = open('/Users/tkmuro/PycharmProjects/tkProgramming/Assignments/FilesAndDictionaries/inaugural_counts.txt', 'w')


def top_25(which_sorted):
    key_list = []
    value_list = []
    for k, v in which_sorted.items():
        key_list.append(k)
        value_list.append(v)

    for i in range(25):
        word_counts.write(str(i+1) + ". " + key_list[i] + " : " + str(value_list[i]) + "\n")


def compare(target, comparison):
    target_list = [item for item in target]
    comp_list = [item for item in comparison]
    for item in target_list:
        if item not in comp_list:
            word_counts.write(item + "\n")


word_counts.write("Top 25 Trump Words:\n")
top_25(trump_sorted)
word_counts.write("\n")
word_counts.write("Top 25 Biden Words:\n")
top_25(biden_sorted)
word_counts.write("\n")
word_counts.write("\n")

word_counts.write("Words used by Trump, but not Biden:\n")
compare(trump_sorted, biden_sorted)
word_counts.write("\n")
word_counts.write("Words used by Biden, but not Trump:\n")
compare(biden_sorted, trump_sorted)


"""
Resources Used:
https://docs.python.org/3/tutorial/datastructures.html?highlight=dictionary#dictionaries
https://stackoverflow.com/questions/423379/using-global-variables-in-a-function
https://docs.python.org/3/tutorial/datastructures.html#dictionaries
https://stackabuse.com/how-to-sort-dictionary-by-value-in-python/
"""
