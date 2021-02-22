'''
Inauguration Speeches (25 pts)
This lab is largely review of: lists, comprehensions, and string methods.
The new items here are reading and writing to files, and using a dictionary (dict).
We will use list, dictionary, and string skills to do a basic comparison of the Trump and Biden inauguration speeches.
Your job will be to find the 25 most common words in each speech (disregarding stop words), and then do a comparison of words that appear in one but not the other, and vice versa.
Then you'll write your results to a txt file (see format below).
A common Python pattern to count objects, produce histograms, or update stats is to make calls to a dictionary as you iterate through a list.
For example, given a list of words, you can create a dictionary to store word counts and then iterate through the list of words, updating the dictionary count for each word each time you've seen it.
'''


# PSEUDO CODE
# Get text from biden.txt and trump.txt and
# split the transcripts into words - Use split and strip methods and store results in lists.
# Remove the stop words from the transcripts by checking if the transcript words are in stop_words (8 pts)
# Create dictionary objects to store the word counts
# Iterate through the list/text of each speech and
# update word counts on your dicts (7 pts)  {'word1': 5, 'word2': 2 ...}
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

