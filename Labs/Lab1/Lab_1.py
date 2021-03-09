from pprint import pprint
import csv

schedule_reader = open('/Users/tkmuro/PycharmProjects/tkProgramming/Labs/Lab1/my_schedule.csv', 'r')
dict_reader = csv.DictReader(schedule_reader)
schedule_list = list(csv.DictReader(schedule_reader))

print("Check 1 ", schedule_list)

new_start = ""
conflict_list = []


def conflict_check(date):
    global conflict_list
    for i in range(len(schedule_list)):
        start_time = schedule_list[i]['Start Time']
        conflict_list.append(start_time)
        if schedule_list[i]['Date'] == str(date):
            if conflict_list.count(start_time) >= 2:
                print("{0} is not available.".format(start_time))
                res_not_done = True
                while res_not_done:
                    reschedule = input("Would you like to cancel or reschedule {0}? (r/c) ".format(schedule_list[i]['Event']))
                    if reschedule.lower() == "r":
                        res_not_done = False
                        global new_start
                        global new_end
                        new_start = input("New start time: ")
                        schedule_list[i]["Start Time"] = new_start
                        new_end = input("New end time: ")
                        schedule_list[i]["End Time"] = new_end
                        break
                    elif reschedule.lower() == "c":
                        res_not_done = False
                        schedule_list[i].remove()


print("Check 2 ", schedule_list)

# date = input("What row do you want to check? ")
# check_time = input("What time do you want to check? ")
# if schedule_list[int(date)]['Start Time'] == check_time:
#     print("No")
# else:
#     print("Yes")
# print(schedule_list[0]['Start Time'])
# print(dict_reader["03/08/2021"])

conflict_check('03/08/2021')
# print(schedule_list)
# print(new_start)

schedule_csv = open('/Users/tkmuro/PycharmProjects/tkProgramming/Labs/Lab1/my_schedule.csv', 'w')
writer = csv.writer(schedule_csv)
writer.writerow(["Date", "Event", "Start Time", "End Time"])
for x in range(len(schedule_list)):
    # print(schedule_list[x]["Event"])
    writer.writerow([schedule_list[x]["Date"], schedule_list[x]["Event"], schedule_list[x]["Start Time"], schedule_list[x]["End Time"]])
