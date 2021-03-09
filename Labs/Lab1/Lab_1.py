from pprint import pprint
import csv

schedule_reader = open('/Users/tkmuro/PycharmProjects/tkProgramming/Labs/Lab1/my_schedule.csv', 'r')
dict_reader = csv.DictReader(schedule_reader)
schedule_list = []
for row in dict_reader:
    # print(row)
    schedule_list.append(row)

# for i in schedule_list:
#     print(i)
#     print(type(i))

# print(schedule_list[1])
# for k, v in schedule_list[1].items():
#     print(k, v)

def conflict_check(date, time):
    for row in range(len(schedule_list)):
        if schedule_list[row]['Date'] == str(date):
            if schedule_list[row]['Start Time'] == time:
                print("That time is not available.")
            else:
                print("That time is open.")

# date = input("What row do you want to check? ")
# check_time = input("What time do you want to check? ")
# if schedule_list[int(date)]['Start Time'] == check_time:
#     print("No")
# else:
#     print("Yes")
# print(schedule_list[0]['Start Time'])
# print(dict_reader["03/08/2021"])


conflict_check('03/08/2021', '8:10')
