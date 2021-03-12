import csv

schedule_reader = open('/Users/tkmuro/PycharmProjects/tkProgramming/Labs/Lab1/my_schedule.csv', 'r')
dict_reader = csv.DictReader(schedule_reader)
schedule_list = list(csv.DictReader(schedule_reader))
''' The section above uses the csv module to read from my_schedule.csv, and appends each sub-dictionary (the data for 
each day) to schedule_list. '''

# Globals
new_start = ""
conflict_list = []
removed_tally = 0
new_end = ""


# This function takes user input, loops if the input is not in the list of valid answers, and returns their answer.
# not super necessary, but I wanted to consolidate and make the taking-user-input process uniform and less tedious.
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
    # event_names = [schedule_list[n]["Event"] for n in range(len(schedule_list))]
    # print(event_names)
    print()
    for i in range(len(schedule_list)):
        start_time = schedule_list[i - removed_tally]['Start Time']
        conflict_list.append(start_time)
        if schedule_list[i - removed_tally]['Date'] == str(date):
            if conflict_list.count(start_time) >= 2:
                print()
                print("{0} is not available.".format(start_time))
                print("Events during {0}: ".format(start_time))
                for w in range(len(schedule_list)):
                    if schedule_list[w - removed_tally]['Date'] == str(date) and conflict_list.count(schedule_list[w - removed_tally]['Start Time']) >= 2:
                        print(schedule_list[w - removed_tally]['Event'])
                        event_names.append(schedule_list[w - removed_tally]['Event'])
                target_event = ""
                while target_event not in event_names:
                    target_event = input("Which event would you like to change? ")
                # Stylistically: there should be separate functions for rescheduling and cancelling.
                reschedule = ""
                while reschedule.lower() != 'r' or reschedule.lower() != 'c':
                    reschedule = input("Would you like to cancel or reschedule {0}? (r/c) ".format(target_event))
                    if reschedule.lower() == "r":
                        global new_start
                        global new_end
                        new_start = input("New start time: ")
                        schedule_list[i]["Start Time"] = new_start
                        new_end = input("New end time: ")
                        schedule_list[i - removed_tally]["End Time"] = new_end
                        conflict_list.clear()
                        break
                    elif reschedule.lower() == "c":
                        print(schedule_list[i - removed_tally])
                        target_in_list = schedule_list.index(target_event)  # TODO: this doesn't work. How can I work backwards from target_event to the list index containing the correct dictionary?
                        schedule_list.remove(target_in_list)
                        removed_tally += 1
                        conflict_list.clear()


# this is a basic cancellation system. It actually works.
def cancel_v2(date, name, time):  # this one works
    global removed_tally
    for i in range(len(schedule_list)):
        start_time = schedule_list[i - removed_tally]['Start Time']
        event_title = schedule_list[i - removed_tally]['Event']
        if schedule_list[i - removed_tally]['Date'] == str(date):
            if event_title == str(name):
                del schedule_list[i - removed_tally]
                removed_tally += 1
                print("post-function: ", removed_tally)
            elif start_time == str(time):
                del schedule_list[i - removed_tally]
                removed_tally += 1
                print("post-function: ", removed_tally)


# This is a more nuanced event cancellation system, which asks the user whether they want to default to the entered
# values for date, time, and name; or if they would like to enter them manually (the former option is for use within
# another function, like conflict_check). It also asks the user whether they want to cancel an event (on the specified
# date), by it's name versus its' start time.
# Currently, it's a hot mess.
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
                    del schedule_list[i-removed_tally]
                    removed_tally += 1
                    print("post-function: ", removed_tally)
    else:
        for i in range(len(schedule_list)):
            start_time = schedule_list[i - removed_tally]['Start Time']
            event_title = schedule_list[i - removed_tally]['Event']
            if schedule_list[i - removed_tally]['Date'] == str(date):
                if event_title == str(name) and name_v_time_mode == 'name':
                    del schedule_list[i - removed_tally]
                    removed_tally += 1
                    print("post-function: ", removed_tally)
                elif start_time == str(time) and name_v_time_mode == 'time':
                    del schedule_list[i-removed_tally]
                    removed_tally += 1
                    print("post-function: ", removed_tally)
                        

# This function prints all the events on a certain date, with the event name and start time formatted for
# easy reading.
def days_events(date):
    print("On {0}, you have the following events: ".format(date))
    for d in range(len(schedule_list)):
        if schedule_list[d]['Date'] == str(date):
            print("   {0} at {1}.".format(schedule_list[d]['Event'], schedule_list[d]['Start Time']))
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
# conflict_check('03/08/2021')
# days_events('03/08/2021')


cancel(True, 'name, ', "03/08/2021", "dummy conflict 2", "14:25")
# cancel_v2('03/08/2021', 'dummy conflict', '8:10')


# Updating the CSV: this section rewrites the contents of schedule_list (which has been modified by each of these
# functions), back to my_schedule.csv.
schedule_csv = open('/Users/tkmuro/PycharmProjects/tkProgramming/Labs/Lab1/my_schedule.csv', 'w')
writer = csv.writer(schedule_csv)
writer.writerow(["Date", "Event", "Start Time", "End Time"])
for x in range(len(schedule_list)):
    writer.writerow([schedule_list[x]["Date"], schedule_list[x]["Event"], schedule_list[x]["Start Time"], schedule_list[x]["End Time"]])
