# dataset from https://www.kaggle.com/prateekmaj21/disney-movies

"""
I'm curious ...
- if more movies are released in certain months?
- if month released correlates to how much a movie grosses?
- if genre or rating are correlated to how much a movie makes?
- if amount grossed has increased as time has progressed?
"""

import csv
import matplotlib.pyplot as plt
import pandas as pd


# import our file with csv

rows = []
adjusted_grosses = []
column_names = None

with open('disney_movies.csv') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i == 0:
            column_names = row
        else:
            rows.append(row)
            adjusted_grosses.append(int(row[5]))

# print the first five rows, and first five adjusted grosses
print(rows[:5])
print(adjusted_grosses[:5])

# print the max adjusted gross
print(max(adjusted_grosses))

# --------------------------------------------------------------------------------------------------------

# import our file with pandas

df = pd.read_csv('disney_movies.csv')
print(df.head())

# print some quick stats
print(df.describe())

# get all the drama films
genre_groups = df.groupby('genre')
print(genre_groups.get_group('Drama'))

# add release month and year to dataframe
release_dates = df['release_date'].to_list()
release_months = [int(date.split("-")[1]) for date in release_dates]
release_years = [int(date.split("-")[0]) for date in release_dates]

df['release_month'] = release_months
df['release_year'] = release_years

# plot some stuff
plt.subplot(2, 2, 1)  # rows, columns, plot number
df["release_year"].value_counts(sort=False).plot(kind="bar")

plt.subplot(2, 2, 2)  # rows, columns, plot number
df["release_month"].value_counts(sort=False).plot(kind="bar")

plt.subplot(2, 2, 3)  # rows, columns, plot number
df["genre"].value_counts().plot(kind="pie")

plt.subplot(2, 2, 4)  # rows, columns, plot number
df["mpaa_rating"].value_counts().plot(kind="pie")

plt.show()

