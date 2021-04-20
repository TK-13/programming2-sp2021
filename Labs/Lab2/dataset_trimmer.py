import csv

data_raw = open("/Users/tkmuro/PycharmProjects/tkProgramming/Labs/Lab2/gdelt_conflict_1_0.csv")
data_reader = csv.DictReader(data_raw)
conflict_dataset = list(data_reader)
data_raw.close()

data_raw = open("/Users/tkmuro/PycharmProjects/tkProgramming/Labs/Lab2/suicides.csv")
data_reader = csv.DictReader(data_raw)
suicide_dataset = list(data_reader)
data_raw.close()

countries_s = {}
for s in suicide_dataset:
    if s["year"] == "2014":
        if s["\ufeffcountry"] not in countries_s:
            countries_s[str(s["\ufeffcountry"])] = s['suicides_no']
            # countries_s.append(s["\ufeffcountry"])
        else:
            countries_s[str(s["\ufeffcountry"])] += s['suicides_no']

for c in countries_s:
    print(c)

# output_file = open('gdelt_trimmed', 'w')
# output_writer = csv.writer(output_file)
# output_writer.writerow(['Year', 'Country', 'Total Events', 'Total Suicides'])
# for row in conflict_dataset:
#     if row["Year"] == 2014:
#         output_writer.writerow()
#
#
# output_file.close()
