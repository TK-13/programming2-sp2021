import csv
from time import sleep

''' The section above uses the csv module to read from my_schedule.csv, and appends each sub-dictionary (the data for 
each day) to schedule_list. '''
schedule_reader = open('./my_schedule.csv', 'r')
dict_reader = csv.DictReader(schedule_reader)
schedule_list = list(csv.DictReader(schedule_reader))


# REFACTOR: Functions now ordered by appearance.

# While the program is active, this function will prompt the user to decide what to do.
def main_interface():
    # Refactor 2: Successfully passed the former "globals" into each function without having to use the global label.
    done = False
    conflict_list = []
    removed_tally = 0
    date_list = []
    command_list = ["1. Check for schedule conflicts.", "2. Reschedule an event.", "3. Cancel an event",
                    "4. Book an event.", "5. List today's events.", "13. End."]

    while not done:
        print()
        for act in command_list:
            print(act)
        print()
        action = user_input("Select the number of the action you would like to perform: ",
                            ["1", "2", "3", "4", "5", "13"],
                            response='Invalid command. ')
        if action == "1":
            list_of_dates(date_list)
            check_date = user_input("What date would you like to check? ", date_list, response='Date not found. ')
            conflict_check(check_date, conflict_list, removed_tally)
        elif action == "2":
            print("Unfortunately, I was unable to complete a manual reschedule system.")
        elif action == "3":
            list_of_dates(date_list)
            cancel_date = user_input("What date would you like to modify? ", date_list, response='Date not found. ')
            manual_cancel(cancel_date, removed_tally)
        elif action == "4":
            book()
        elif action == "5":
            list_of_dates(date_list)
            list_date = user_input("What date would you like to view? ", date_list, response='Date not found. ')
            days_events(list_date)
            print()
        elif action == "13":
            print("Bye!")
            update()
            done = True


# This function takes user input, loops if the input is not in the list of valid answers, and returns their answer.
# REFACTOR: Taking inspiration from your version of a user_input function, I improved this function to use more
# default values, and give an 'error message' when the user enters an invalid option.
def user_input(message, options_list, response="", options_message="Valid Inputs: ", print_options=False):
    if print_options:
        print(options_message)
        for option in options_list:
            print(option)
    entry = input(message)
    while entry not in options_list:
        print(response)
        entry = input(message)
    return entry


# For easy access in the main interface, this function just finds all the different dates in my_schedule.csv, and
# prints those options for the user to decide which date to work with.
def list_of_dates(dates):
    for d in range(len(schedule_list)):
        if schedule_list[d]["Date"] not in dates:
            dates.append(schedule_list[d]["Date"])
    print("Available dates:")
    for date in dates:
        print(date)
    return dates


# Updating the CSV: this function rewrites the contents of schedule_list (which has been modified by cancel, reschedule,
# or conflict_check), back to my_schedule.csv.
def update():
    schedule_csv = open('./my_schedule.csv', 'w')
    writer = csv.writer(schedule_csv)
    writer.writerow(["Date", "Event", "Start Time", "End Time"])
    for x in range(len(schedule_list)):
        writer.writerow([schedule_list[x]["Date"], schedule_list[x]["Event"], schedule_list[x]["Start Time"],
                         schedule_list[x]["End Time"]])


# This runs through all events on a date, detects if any events have the same start time, and asks the user if
# they would like to reschedule or cancel.
# Unfortunately, I wasn't able to check whether rescheduled times conflicted with other events, or parse through the
# new date and time to put the rescheduled event in chronological order.
def conflict_check(date, conflict_list, removed_tally):
    # REFACTOR 2: as per your instructions, I passed date_list, conflict_list, and removed_tally through each
    # function in this manner.
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
                    tally_shifted = w - removed_tally
                    if schedule_list[tally_shifted]['Date'] == str(date) and conflict_list.count(
                            schedule_list[tally_shifted]['Start Time']) >= 2:
                        print(schedule_list[tally_shifted]['Event'])
                        event_names.append(schedule_list[tally_shifted]['Event'])
                target_event = user_input("Which event would you like to change? ", event_names,
                                          response="Event not found. ", print_options=False)
                choice = user_input("Would you like to cancel or reschedule {0}? (r/c) ".format(target_event),
                                    ['r', 'c'], response="Invalid command. ")
                if choice.lower() == "r":  # check if entered new start time conflicts with something else.
                    reschedule(i, conflict_list, removed_tally)
                    print("{0} has been rescheduled.".format(target_event, date))
                    conflict_list.clear()
                    event_names.clear()
                elif choice.lower() == "c":
                    cancel(removed_tally, date, target_event)
                    removed_tally += 1
                    conflict_list.clear()
                    event_names.clear()
    print()
    update()


# REFACTOR 2: Removed the reschedule function I wasn't able to finish, just to clear up space.


# This function just takes new inputs for an event's new start time, end time, and date, and sets their values in
# schedule_list accordingly.
# These are probably throwing "Unexpected type" errors. Since the
# keys for the dictionaries in schedule_list are strings, I'm not sure why this is happening.
def reschedule_manual(place, removed_tally):
    new_date = input("New date: ")
    schedule_list[place]["Date"] = new_date
    new_start = input("New start time: ")
    schedule_list[place]["Start Time"] = new_start
    new_end = input("New end time: ")
    schedule_list[place - removed_tally]["End Time"] = new_end


# This function is the basic form of my cancellation system. If given a name, or a date and a name, it will remove the
# event from schedule_list and notify the user. It can take either manual inputs (see manual_reschedule), or date, time,
# and name values from conflict_check.
def cancel(removed_tally, date, name, time=""):
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
def manual_cancel(date, removed_tally):
    name = ""
    time = ""
    valid_events = [schedule_list[r]["Event"] for r in range(len(schedule_list))]
    valid_starts = [schedule_list[r]["Start Time"] for r in range(len(schedule_list))]
    mode = user_input("Do you cancel an event by it's name, or it's time? (enter name or time) ", ['name', 'time'],
                      response="Invalid mode entry. ")
    if mode == 'name':
        name = user_input("Enter event name: ", valid_events, response="Event not found. ")
    elif mode == 'time':
        time = user_input("Enter event start time: ", valid_starts, response="Start time not found. ")
        print()
        print("Events during {0}: ".format(time))
        for w in range(len(schedule_list)):
            if schedule_list[w - removed_tally]['Date'] == str(date) and schedule_list[w - removed_tally]["Start Time"] == time:
                print(schedule_list[w - removed_tally]['Event'])
        name = user_input("Which event would you like to change? ", valid_events, response="Event not found. ")
    cancel(removed_tally, date, name, time)
    print()
    update()


def book(date="", name="", start="20", end=""):
    open_times = []

    # REFACTOR: makes a list of available times for booking appointments, leaving out anything after 20:00
    # I didn't use list comprehension because of all the different conditions and string manipulations needed to make
    # each option in the right format.
    for h in range(20):
        if h <= 9:
            hour = ("0" + str(h))
        else:
            hour = str(h)
        for m in range(59):
            if m <= 9:
                open_times.append(hour + ":0" + str(m))
            else:
                open_times.append(hour + ":" + str(m))

    if not date and not name and start == "20" and not end:
        date = input("New event date: ")
        name = input("New event title: ")
        insert_point = 0
        # REFACTOR: I (sort of) improved the filtering system which prevents booking events after 20:00.
        # this is only sort of an improvement because although it uses the user_input function, more work had to be
        # done above to make a list filtering out all options before 20:00.
        start = user_input("New event start time: ", open_times, response="Please do not schedule events after 20:00.")
        end = input("New event end time: ")
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


# This function prints all the events on a certain date, with the event name and start time formatted for
# easy reading.
def days_events(date):
    print("On {0}, you have the following events: ".format(date))
    for d in range(len(schedule_list)):
        if schedule_list[d]['Date'] == str(date):
            print("   {0} at {1}.".format(schedule_list[d]['Event'], schedule_list[d]['Start Time']))
            sleep(0.5)


# Here is the "game loop", where users are continuously prompted to use the different functions at their disposal.
# Code "13" sets done = True, ending the program.
# REFACTOR: added the if __name__ statement, since there was already kind of a main function.
if __name__ == '__main__':
    main_interface()
