import csv
from time import sleep

''' The section above uses the csv module to read from my_schedule.csv, and appends each sub-dictionary (the data for 
each day) to schedule_list. '''
schedule_reader = open('./my_schedule.csv', 'r')
dict_reader = csv.DictReader(schedule_reader)
schedule_list = list(csv.DictReader(schedule_reader))

# Globals
conflict_list = []
removed_tally = 0


# This function takes user input, loops if the input is not in the list of valid answers, and returns their answer.
def user_input(message, param_list):
    user_entry = ""
    while user_entry not in param_list:
        user_entry = input(message)
    return user_entry


# This runs through all events on a date, detects if any events have the same start time, and asks the user if
# they would like to reschedule or cancel.
def conflict_check(date):
    global conflict_list
    global removed_tally
    event_names = []
    print()
    for i in range(len(schedule_list)):
        start_time = schedule_list[i - removed_tally]['Start Time']
        conflict_list.append(start_time)
        if schedule_list[i - removed_tally]['Date'] == str(date):
            if conflict_list.count(start_time) >= 2:
                print("\n{0} is not available.".format(start_time))
                print("Events during {0}: ".format(start_time))
                for w in range(len(schedule_list)):
                    if schedule_list[w - removed_tally]['Date'] == str(date) and conflict_list.count(schedule_list[w - removed_tally]['Start Time']) >= 2:
                        print(schedule_list[w - removed_tally]['Event'])
                        event_names.append(schedule_list[w - removed_tally]['Event'])
                target_event = user_input("Which event would you like to change? ", event_names)
                choice = user_input("Would you like to cancel or reschedule {0}? (r/c) ".format(target_event),
                                    ['r', 'c'])

                if choice.lower() == "r":  # check if entered new start time conflicts with something else.
                    reschedule(i)
                    print("{0} has been rescheduled.".format(target_event, date))
                    conflict_list.clear()
                    event_names.clear()

                elif choice.lower() == "c":
                    cancel_v1(date, target_event)
                    removed_tally += 1
                    conflict_list.clear()
                    event_names.clear()


def book(date="", name="", start="20", end=""):
    events_in_day = []
    if not date and not name and start == "20" and not end:
        date = input("New event date: ")
        name = input("New event title: ")

        while start[0] == "2" or start == "no":  # This prevents the user from starting events after 8:00 pm
            start = input("New event start time: ")
            if start[0] == "2":
                print("Please do not schedule events after 20:00")
                print()
            continue

        end = input("New event end time: ")  # I couldn't do a duration system, sorry.
        for d in range(len(schedule_list)):
            if schedule_list[d]["Date"] == str(date):
                insert_point = d
                events_in_day.append(schedule_list[d])
        schedule_list.insert(insert_point-1, {'Date': date, 'Event': name, 'Start Time': start, 'End Time': end})
    else:
        schedule_list.append({'Date': date, 'Event': name, 'Start Time': start, 'End Time': end})


# In progress, currently doesn't work.
def reschedule(location, date=None, name=False, s_time=None):  # can it work on its own?
    global removed_tally
    if location:
        reschedule_manual(location)
    else:
        for j in range(len(schedule_list)):
            if schedule_list[j]["Date"] == date:
                if schedule_list[j]["Event"] == name:
                    reschedule_manual(j)
                # elif schedule_list[j]["Start Time"] == s_time:
                #     print(conflict_list)
                #     target = input("Which event do you want to alter at {0}? ".format(s_time))
                #     if schedule_list[j]["Event"] == target:
                #         new_date = input("New date: ")
                #         schedule_list[j]["Date"] = new_date
                #         new_start = input("New start time: ")
                #         schedule_list[j]["Start Time"] = new_start
                #         new_end = input("New end time: ")
                #         schedule_list[j - removed_tally]["End Time"] = new_end


def reschedule_manual(place):
    new_date = input("New date: ")
    schedule_list[place]["Date"] = new_date
    new_start = input("New start time: ")
    schedule_list[place]["Start Time"] = new_start
    new_end = input("New end time: ")
    schedule_list[place - removed_tally]["End Time"] = new_end

    '''
    if schedule_list[location]['Date'] == str(date):
        schedule_list[location]["Date"] = date
        schedule_list[location]["Start Time"] = s_time
        new_end = input("New end time: ")
        schedule_list[location - removed_tally]["End Time"] = new_end
    '''


''' def sub_reschedule(abcde, date, time, name):
    # if not date and not time and not name:
    #     if schedule_list[abcde - removed_tally]['Date'] == str(date):
    #         if schedule_list[abcde - removed_tally]['Event'] == str(name) or schedule_list[abcde - removed_tally]['Start Time'] == str(time):
    if not date and not time and not name:
        new_date = input("New date: ")
        schedule_list[abcde]["Date"] = new_date
        new_start = input("New start time: ")
        schedule_list[abcde]["Start Time"] = new_start
        new_end = input("New end time: ")
        schedule_list[abcde - removed_tally]["End Time"] = new_end
    else: '''


# this is a basic cancellation system. It actually works.
def cancel_v1(date, name, time=False):  # this one works
    global removed_tally
    for i in range(len(schedule_list)):
        start_time = schedule_list[i - removed_tally]['Start Time']
        event_title = schedule_list[i - removed_tally]['Event']
        if schedule_list[i - removed_tally]['Date'] == str(date):
            if event_title == str(name):
                del schedule_list[i - removed_tally]
                removed_tally += 1
            elif start_time == str(time) and str(time):
                del schedule_list[i - removed_tally]
                removed_tally += 1
    print("{0} has been cancelled on {1}.".format(name, date))


# This is a more nuanced event cancellation system, which asks the user whether they want to default to the entered
# values for date, time, and name; or if they would like to enter them manually (the former option is for use within
# another function, like conflict_check). It also asks the user whether they want to cancel an event (on the specified
# date), by it's name versus its' start time.
# Currently, it's a hot mess.

# A good idea. Break it down into more functions for clarity. make some parameters have defaults (date, name, and time can
# have defaults, which should work if user enters nothing. date = None, name = None, check "if name" to see if
# user passed in something. When someone reads that, they automatically realize it could do more than one thing.
def cancel(user_entry_mode, name_v_time_mode, date, name, time):  # this one does not work
    global removed_tally
    valid_dates = [schedule_list[r]["Date"] for r in range(len(schedule_list))]
    valid_events = [schedule_list[r]["Event"] for r in range(len(schedule_list))]
    valid_starts = [schedule_list[r]["Start Time"] for r in range(len(schedule_list))]
    if user_entry_mode:
        date = user_input("Enter target date for event cancellation: ", valid_dates)
        mode = user_input("Do you cancel an event by it's name, or it's time? (enter name or time) ", ['name', 'time'])
        if mode == 'name':
            name = user_input("Enter event name: ", valid_events)
        elif mode == 'time':
            time = user_input("Enter event start time: ", valid_starts)

        for i in range(len(schedule_list)):
            start_time = schedule_list[i - removed_tally]['Start Time']
            event_title = schedule_list[i - removed_tally]['Event']
            if schedule_list[i - removed_tally]['Date'] == str(date):
                if event_title == str(name) and name_v_time_mode == 'name':
                    del schedule_list[i - removed_tally]
                    removed_tally += 1
                    print("post-function: ", removed_tally)
                elif start_time == str(time) and name_v_time_mode == 'time':
                    del schedule_list[i - removed_tally]
                    removed_tally += 1
                    print("post-function: ", removed_tally)
    else:
        cancel_v1(date, name, time)

        for i in range(len(schedule_list)):
            start_time = schedule_list[i - removed_tally]['Start Time']
            event_title = schedule_list[i - removed_tally]['Event']
            if schedule_list[i - removed_tally]['Date'] == str(date):
                if event_title == str(name) and name_v_time_mode == 'name':
                    del schedule_list[i - removed_tally]
                    removed_tally += 1
                    print("post-function: ", removed_tally)
                elif start_time == str(time) and name_v_time_mode == 'time':
                    del schedule_list[i - removed_tally]
                    removed_tally += 1
                    print("post-function: ", removed_tally)

                    # Make more compact.


# This function prints all the events on a certain date, with the event name and start time formatted for
# easy reading.
def days_events(date):
    print("On {0}, you have the following events: ".format(date))
    for d in range(len(schedule_list)):
        if schedule_list[d]['Date'] == str(date):
            print("   {0} at {1}.".format(schedule_list[d]['Event'], schedule_list[d]['Start Time']))
            sleep(0.5)
            ''' advice from  Ms. Ifft: I could add duration. if i want, I can try to use python date-time to make 
            these into a format that's helpful. Don't try until done with everything.'''


# Next three (this will hopefully print the next three upcoming events, but I'm not going to work on it until after
# the other tasks are functional).
# Feel free to ignore this one, it's broken af.
''' def next_three(date, current_time):  # Get everything else working first, before coming back to this. It can be cut out if necessary.
    hour_check = int(current_time[0])
    print("Your next three events are: ")
    for d in range(len(schedule_list)):
        if schedule_list[d]['Date'] == str(date):
            print("   {0} at {1}.".format(schedule_list[d]['Event'], schedule_list[d]['Start Time'])) '''
'''
# this works, but its tedious. Before Ms. Ifft mentioned a python library for handling dates and times, I tried parsing
# through the Start times of an event to evaluate its' time as an integer. 
# print(schedule_list[0]["Start Time"])
# for char in range(len(schedule_list[0]["Start Time"])):
#     if schedule_list[0]["Start Time"][char] == "8" and schedule_list[0]["Start Time"][char + 1] == ":":
#         print("found")
'''

''' Testing Zone '''

# for i in range(len(schedule_list)):
#     print(schedule_list[i])

book()
book("03/08/2021", 'Manual', "50000", "201050")

# conflict_check('03/08/2021')
# days_events('03/08/2021')
# cancel_v1("03/08/2021", "dummy conflict 2", "14:25")
# cancel(False, 'name', "03/08/2021", "dummy conflict", "14:25")
# reschedule(None, "03/08/2021", "dummy conflict b", "08:10")

# for i in range(len(schedule_list)):
#     for k, v in schedule_list[i].items():
#         if schedule_list[i]["Date"] == '03/08/2021':
#             print(k, v)
#             conflict_check_dict[schedule_list[i]["Start Time"]] = i
#     print()
# print(conflict_check_dict)


def conflict_check_2(date):
    conflict_check_dict = {}
    index_list = []
    time_list = []
    for c in range(len(schedule_list)):
        if schedule_list[c]["Date"] == date:
            if schedule_list[c]["Start Time"] not in time_list:
                # print(schedule_list[c]["Start Time"])
                time_list.append(schedule_list[c]["Start Time"])
            if schedule_list[c]["Start Time"] in time_list:
                index_list.append(schedule_list.index(schedule_list[c]))

            for t in time_list:
                conflict_check_dict[t] = index_list

        # index_list.clear()
            # if schedule_list[c]["Start Time"] in time_list:
            #     index_list.append(schedule_list.index(schedule_list[c]))

            # conflict_check_dict[schedule_list[c]["Start Time"]] = index_list

    for k, v in conflict_check_dict.items():
        print(k, v)
    print("Time list: ", time_list)
    print("Index list: ", index_list)


# conflict_check_2('03/08/2021')

'''
times = []
indexes = []

for r in range(len(schedule_list)):
    if schedule_list[r]["Date"] == '03/08/2021':
        # print(schedule_list[r])
        if schedule_list[r]["Start Time"] not in times:
            times.append(schedule_list[r]["Start Time"])
        for ts in times:
            if schedule_list[r]["Start Time"] == ts:
                indexes.append(schedule_list.index(schedule_list[r]))
            conflict_check_


for r in range(len(schedule_list)):
    if schedule_list[r]["Date"] == '03/08/2021':
        for ts in times:
            if schedule_list[r]["Start Time"] == ts:
                indexes.append(schedule_list.index(schedule_list[r]))

print(times)
print()
print(indexes)

print()


def mini(place):
    print("name: ", schedule_list[place]['Event'])
    print("time: ", schedule_list[place]["Start Time"])
    print("index: ", schedule_list.index(schedule_list[place]))


mini(1)

# print()
# for i in schedule_list:
#     print(i)
#     print(schedule_list.index(i))
'''

# Updating the CSV: this section rewrites the contents of schedule_list (which has been modified by each of these
# functions), back to my_schedule.csv.
schedule_csv = open('./my_schedule.csv', 'w')
writer = csv.writer(schedule_csv)
writer.writerow(["Date", "Event", "Start Time", "End Time"])
for x in range(len(schedule_list)):
    writer.writerow([schedule_list[x]["Date"], schedule_list[x]["Event"], schedule_list[x]["Start Time"],
                     schedule_list[x]["End Time"]])
