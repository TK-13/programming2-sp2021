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
done = False
date_list = []


# For easy access in the main interface, this function just finds all the different dates in my_schedule.csv, and
# prints those options for the user to decide which date to work with.
def list_of_dates():
    global date_list
    for d in range(len(schedule_list)):
        if schedule_list[d]["Date"] not in date_list:
            date_list.append(schedule_list[d]["Date"])
    print("Available dates:")
    for date in date_list:
        print(date)
    return date_list


# Updating the CSV: this function rewrites the contents of schedule_list (which has been modified by cancel, reschedule,
# or conflict_check), back to my_schedule.csv.
def update():
    schedule_csv = open('./my_schedule.csv', 'w')
    writer = csv.writer(schedule_csv)
    writer.writerow(["Date", "Event", "Start Time", "End Time"])
    for x in range(len(schedule_list)):
        writer.writerow([schedule_list[x]["Date"], schedule_list[x]["Event"], schedule_list[x]["Start Time"],
                         schedule_list[x]["End Time"]])


# While the program is active, this function will prompt the user to decide what to do.
def main_interface():
    global done
    global date_list
    act_list = ["1. Check for schedule conflicts.",
                "2. Reschedule an event.",
                "3. Cancel an event",
                "4. Book an event.",
                "5. List today's events.",
                "13. End."
                ]
    print()
    for act in act_list:
        print(act)
    print()
    action = user_input("Select the number of the action you would like to perform: ", ["1", "2", "3", "4", "5", "13"])
    if action == "1":
        list_of_dates()
        check_date = user_input("What date would you like to check? ", date_list)
        conflict_check(check_date)
    elif action == "2":
        # list_of_dates()
        # res_date = user_input("What date would you like to modify? ", date_list)
        # reschedule(None, res_date)
        print("Unfortunately, I was unable to complete a manual reschedule system.")
    elif action == "3":
        list_of_dates()
        cancel_date = user_input("What date would you like to modify? ", date_list)
        manual_cancel(cancel_date)
    elif action == "4":
        book()
    elif action == "5":
        list_of_dates()
        list_date = user_input("What date would you like to view? ", date_list)
        days_events(list_date)
        print()
    elif action == "13":
        print("Bye!")
        update()
        done = True


# This function takes user input, loops if the input is not in the list of valid answers, and returns their answer.
def user_input(message, param_list):
    user_entry = ""
    while user_entry not in param_list:
        user_entry = input(message)
    return user_entry


# This runs through all events on a date, detects if any events have the same start time, and asks the user if
# they would like to reschedule or cancel.
# Unfortunately, I wasn't able to check whether rescheduled times conflicted with other events, or parse through the
# new date and time to put the rescheduled event in chronological order.
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
                    if schedule_list[w - removed_tally]['Date'] == str(date) and conflict_list.count(
                            schedule_list[w - removed_tally]['Start Time']) >= 2:
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
                    cancel(date, target_event)
                    removed_tally += 1
                    conflict_list.clear()
                    event_names.clear()
    print()
    update()


def book(date="", name="", start="20", end=""):
    if not date and not name and start == "20" and not end:
        date = input("New event date: ")
        name = input("New event title: ")
        insert_point = 0
        while start[0] == "2" or start == "no":  # This prevents the user from starting events after 8:00 pm
            start = input("New event start time: ")
            if start[0] == "2":
                print("Please do not schedule events after 20:00")
                print()
            continue

        end = input("New event end time: ")  # I couldn't do a duration system, sorry.
        for d in range(len(schedule_list)):
            if schedule_list[d]["Date"] == str(date):
                if int(schedule_list[d]["Start Time"][0]) == int(start[0]) and int(schedule_list[d]["Start Time"][1]) <= int(start[1]):
                    # This can parse the entered start time by the hour, to insert it in roughly the right chronological position.
                    # I didn't have time to parse down to minutes, sorry.
                    print(schedule_list[d]["Event"], ":", schedule_list[d]["Start Time"][0], ":", d)
                    print()
                    insert_point = d + 1
                else:
                    schedule_list.append({'Date': date, 'Event': name, 'Start Time': start, 'End Time': end})
        schedule_list.insert(insert_point, {'Date': date, 'Event': name, 'Start Time': start, 'End Time': end})
    else:
        schedule_list.append({'Date': date, 'Event': name, 'Start Time': start, 'End Time': end})
    print()
    update()


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
                elif schedule_list[j]["Start Time"] == s_time:
                    print(conflict_list)
                    target = input("Which event do you want to alter at {0}? ".format(s_time))
                    if schedule_list[j]["Event"] == target:
                        reschedule_manual(j)


# This function just takes new inputs for an event's new start time, end time, and date, and sets their values in
# schedule_list accordingly.
# These are probably throwing "Unexpected type" errors. Since the
# keys for the dictionaries in schedule_list are strings, I'm not sure why this is happening.
def reschedule_manual(place):
    new_date = input("New date: ")
    schedule_list[place]["Date"] = new_date
    new_start = input("New start time: ")
    schedule_list[place]["Start Time"] = new_start
    new_end = input("New end time: ")
    schedule_list[place - removed_tally]["End Time"] = new_end


# This function is the basic form of my cancellation system. If given a name, or a date and a name, it will remove the
# event from schedule_list and notify the user. It can take either manual inputs (see manual_reschedule), or date, time,
# and name values from conflict_check.
def cancel(date, name, time=""):
    global removed_tally
    for i in range(len(schedule_list)):
        start_time = schedule_list[i - removed_tally]['Start Time']
        event_title = schedule_list[i - removed_tally]['Event']
        if schedule_list[i - removed_tally]['Date'] == str(date):
            if event_title == str(name):
                del schedule_list[i - removed_tally]
                removed_tally += 1
            elif start_time == str(time) and str(time) and event_title == name:
                del schedule_list[i - removed_tally]
                removed_tally += 1
    print("{0} has been cancelled on {1}.".format(name, date))


# This cancellation system asks for the user's input, rather than relying on date, name, and time values derived from the
# conflict_check function. It also asks the user whether they want to cancel an event (on the specified
# date), by it's name versus its' start time.
# At last, it works.
def manual_cancel(date):
    global removed_tally
    name = ""
    time = ""
    valid_events = [schedule_list[r]["Event"] for r in range(len(schedule_list))]
    valid_starts = [schedule_list[r]["Start Time"] for r in range(len(schedule_list))]
    mode = user_input("Do you cancel an event by it's name, or it's time? (enter name or time) ", ['name', 'time'])
    if mode == 'name':
        name = user_input("Enter event name: ", valid_events)
    elif mode == 'time':
        time = user_input("Enter event start time: ", valid_starts)
        print()
        print("Events during {0}: ".format(time))
        for w in range(len(schedule_list)):  # Yeah, this was pulled from conflict_check. Sorry I didn't have time to make it a separate function.
            if schedule_list[w - removed_tally]['Date'] == str(date) and schedule_list[w-removed_tally]["Start Time"] == time:
                print(schedule_list[w - removed_tally]['Event'])
        name = user_input("Which event would you like to change? ", valid_events)
    cancel(date, name, time)
    print()
    update()


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


# Here is the "game loop", where users are continuously prompted to use the different functions at their disposal.
# Code "13" sets done = True, ending the program.
while not done:
    main_interface()


''' Junk: here are most of the things I started, but was unable to finish. The main example is your idea for a 
conflict_check dictionary, to replace the removed_tally system. Feel free to ignore this, since it's not part of my
main program.


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

# Next three: not much here, just my attempts at the "next three events" system.
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