import csv

def read_data(path):
    data_raw = open(path)
    data_reader = csv.DictReader(data_raw)
    file = list(data_reader)
    data_raw.close()
    return file


new_suicide_dataset = read_data("/Users/tkmuro/PycharmProjects/tkProgramming/Labs/Lab2/Age-standardized suicide rates.csv")
coordinate_dataset = read_data("/Users/tkmuro/PycharmProjects/tkProgramming/Labs/Lab2/countries.csv")
conflict_dataset = read_data("/Users/tkmuro/PycharmProjects/tkProgramming/Labs/Lab2/gdelt_processor_friendly.csv")


def read_country_names(dataset, key):
    name_list = []
    for row in dataset:
        name = row[key]
        # print(name)
        if name not in name_list:
            name_list.append(name)
    # print()
    name_list.sort()
    return name_list


countries_suicide = read_country_names(new_suicide_dataset, 'Country')
countries_gdelt = read_country_names(conflict_dataset, 'CountryName')
countries_coords = read_country_names(coordinate_dataset, 'name')
print()

# Filtering
gdelt_not_in_suicides = []
gdelt_not_in_coords = []
dunce_list = []
for country in countries_gdelt:
    if country in countries_suicide and country in countries_coords:
        print(country, " confirmed.")
        print()
    elif country not in countries_suicide:
        gdelt_not_in_suicides.append(country)
    elif country not in countries_coords:
        gdelt_not_in_coords.append(country)
    else:
        print('!!! ', country, " is weird !!!")
        dunce_list.append(country)

print()
print("gdelt not in coords:")
for x in gdelt_not_in_coords:
    print(x)


def country_rename(target_dataset, key, target_name, replacement_name):
    for row in target_dataset:
        if row[key] == target_name:
            row[key] = replacement_name


# Attempt 1
# for row in conflict_dataset:
#     if row['CountryName'] == "Bahamas, The":
#         print(row)
#
# print()
#
# country_rename(conflict_dataset, 'CountryName', 'Bahamas, The', 'Bahamas')


# for row in conflict_dataset:
#     if row['CountryName'] == "Bahamas, The":
#         row['CountryName'] = "Bahamas"

# Attempt 2
# for row in conflict_dataset:
#     if row['CountryName'] == "Bahamas":
#         print(row)

# for row in new_suicide_dataset:
#     if row['Country'] == 'Bahamas':
#         print(row)

'''
Fixable gdelt not in suicides:
Bahamas, The - Bahamas
Bolivia - Bolivia (Plurinational State of)
Brunei - Brunei Darussalam
Cape Verde - Cabo Verdo
!!! Congo, (Democratic) Republic of the - Congo + Democratic Republic of the Congo
Cote d'Ivoire - Côte d'Ivoire
Czech Republic - Czechia
Iran - Iran (Islamic Republic of)
Laos - Lao People's Democratic Republic
Syria - Syrian Arab Republic
Swaziland - Eswatini
United Kingdom - United Kingdom of Great Britain and Northern Ireland
Tanzania - United Republic of Tanzania
United States - United States of America
Venezuela - Venezuela (Bolivarian Republic of)
Vietnam - Viet Nam

Korea, South
Korea, North, Democratic People's Republic of Korea + Republic of Korea
'''


'''
Fixable gdelt not in coords:
Myanmar - Myanmar [Burma]
Sao Tome and Principe - S?o Tom? and Pr?ncipe
'''




'''
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

'''