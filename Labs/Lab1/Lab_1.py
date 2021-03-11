from pprint import pprint
import csv

schedule_reader = open('/Users/tkmuro/PycharmProjects/tkProgramming/Labs/Lab1/my_schedule.csv', 'r')
dict_reader = csv.DictReader(schedule_reader)
schedule_list = list(csv.DictReader(schedule_reader))

# print("Check 1 ", schedule_list)
# for j in range(len(schedule_list)):
#     print(j, schedule_list[j]["Start Time"])

new_start = ""
conflict_list = []


def conflict_check(date):
    global conflict_list
    removed_tally = 0
    for i in range(len(schedule_list)):
        start_time = schedule_list[i - removed_tally]['Start Time']
        conflict_list.append(start_time)
        if schedule_list[i - removed_tally]['Date'] == str(date):
            if conflict_list.count(start_time) >= 2:
                print("{0} is not available.".format(start_time))
                print("Events during {0}: ".format(start_time))
                res_not_done = True
                for w in range(len(schedule_list)):
                    if schedule_list[w - removed_tally]['Date'] == str(date) and conflict_list.count(schedule_list[w - removed_tally]['Start Time']) >= 2:
                        print(schedule_list[w - removed_tally]['Event'])

                while res_not_done:
                    target_event = input("Which event would you like to change? ")
                    reschedule = input("Would you like to cancel or reschedule {0}? (r/c) ".format(target_event))
                    if reschedule.lower() == "r":
                        res_not_done = False
                        global new_start
                        global new_end
                        new_start = input("New start time: ")
                        schedule_list[i]["Start Time"] = new_start
                        new_end = input("New end time: ")
                        schedule_list[i - removed_tally]["End Time"] = new_end
                        break
                    elif reschedule.lower() == "c":
                        res_not_done = False
                        print(schedule_list[i - removed_tally])
                        crosshair = schedule_list.index(target_event) # TODO: this doesn't work. How can I work backwards from target_event to the list index containing the correct dictionary?
                        schedule_list.remove(crosshair)
                        removed_tally += 1
                        

def days_events(date):
    print("On {0}, you have the following events: ".format(date))
    for d in range(len(schedule_list)):
        if schedule_list[d]['Date'] == str(date):
            print("   {0} at {1}.".format(schedule_list[d]['Event'], schedule_list[d]['Start Time']))


def next_three(date, current_time):
    print("Your next three events are: ")
    for d in range(len(schedule_list)):
        if schedule_list[d]['Date'] == str(date):
            print("   {0} at {1}.".format(schedule_list[d]['Event'], schedule_list[d]['Start Time']))


# next_three_date = input("What is today's date? ")
# next_three_time = input("What is the current time? ")
# next_three(next_three_date, next_three_date)

# conflict_check('03/08/2021')

print(schedule_list[5]["Event"])
print(schedule_list)
print()
test_time = "09:20"
for item in range(len(schedule_list)):
    if schedule_list[item]['Date'] == '03/08/2021':
        print(schedule_list[item])

'''schedule_csv = open('/Users/tkmuro/PycharmProjects/tkProgramming/Labs/Lab1/my_schedule.csv', 'w')
writer = csv.writer(schedule_csv)
writer.writerow(["Date", "Event", "Start Time", "End Time"])
for x in range(len(schedule_list)):
    # print(schedule_list[x]["Event"])
    writer.writerow([schedule_list[x]["Date"], schedule_list[x]["Event"], schedule_list[x]["Start Time"], schedule_list[x]["End Time"]])
'''