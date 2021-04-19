import csv
import matplotlib.pyplot as plt
import numpy as np

data_raw = open("/Users/tkmuro/PycharmProjects/tkProgramming/Labs/Lab2/gdelt_conflict_1_0.csv")
data_reader = csv.DictReader(data_raw)
conflict_dataset = list(data_reader)
data_raw.close()

data_raw = open("/Users/tkmuro/PycharmProjects/tkProgramming/Labs/Lab2/suicides.csv")
data_reader = csv.DictReader(data_raw)
suicide_dataset = list(data_reader)
data_raw.close()

# years = []
# for yr in suicide_dataset:
#     if yr["year"] not in years:
#         years.append(yr["year"])
# years.sort()

# 2021:
country_names = []
total_events = []
for i in conflict_dataset:
    if i["Year"] == "2021" and i["CountryName"] not in country_names:
        country_names.append(i["CountryName"])
        total_events.append(i["TotalEvents"])

for s in suicide_dataset:
    if
