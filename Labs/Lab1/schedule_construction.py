import csv


''' This file will create the starter schedule, which can then be manipulated as necessary. I had to make it a separate
file because, whenever I ran this code in Lab_1.py, the schedule_list would just be blank. '''

schedule_dict = {
    "03/08/2021": [{"Event Name": "Comedy and Literature",
                    "Start Time": "08:10",
                    "End Time": "09:00"},
                    {"Event Name": "dummy conflict",
                    "Start Time": "08:10",
                    "End Time": "09:00"},
                   {"Event Name": "Calculus",
                    "Start Time": "10:05",
                    "End Time": "10:55"},
                   {"Event Name": "Programming II",
                    "Start Time": "12:30",
                    "End Time": "13:20"},
                   {"Event Name": "Computer Animation",
                    "Start Time": "14:25",
                    "End Time": "15:15"},
                   {"Event Name": "dummy conflict 2",
                    "Start Time": "14:25",
                    "End Time": "15:15"},
                   {"Event Name": "Senior Seminar",
                    "Start Time": "15:20",
                    "End Time": "16:10"}
                   ],
    "03/09/2021": [{"Event Name": "Programming II",
                    "Start Time": "08:10",
                    "End Time": "09:00"},
                   {"Event Name": "Computer Animation",
                    "Start Time": "10:05",
                    "End Time": "10:55"},
                   {"Event Name": "Calculus",
                    "Start Time": "12:30",
                    "End Time": "13:20"},
                   {"Event Name": "Comedy and Literature",
                    "Start Time": "13:25",
                    "End Time": "14:15"}
                   ],
    "03/10/2021": [{"Event Name": "Gym D",
                    "Start Time": "08:45",
                    "End Time": "09:00"},
                   {"Event Name": "Student Government",
                    "Start Time": "10:00",
                    "End Time": "10:45"},
                   {"Event Name": "Graderoom",
                    "Start Time": "13:05",
                    "End Time": "13:45"},
                   {"Event Name": "Advisory",
                    "Start Time": "13:50",
                    "End Time": "14:30"},
                   {"Event Name": "Robotics",
                    "Start Time": "15:45",
                    "End Time": "16:35"}
                   ],
    "03/11/2021": [{"Event Name": "Calculus",
                    "Start Time": "08:10",
                    "End Time": "09:00"},
                   {"Event Name": "Comedy and Literature",
                    "Start Time": "09:05",
                    "End Time": "09:55"},
                   {"Event Name": "Advanced Topics in Physics",
                    "Start Time": "11:00",
                    "End Time": "11:50"},
                   {"Event Name": "Computer Animation",
                    "Start Time": "13:25",
                    "End Time": "14:15"},
                   {"Event Name": "Programming II",
                    "Start Time": "14:25",
                    "End Time": "15:20"}
                   ],
    "03/12/2021": [{"Event Name": "Computer Animation",
                    "Start Time": "09:05",
                    "End Time": "09:55"},
                   {"Event Name": "Programming II",
                    "Start Time": "11:00",
                    "End Time": "11:50"},
                   {"Event Name": "Comedy and Literature",
                    "Start Time": "13:25",
                    "End Time": "14:15"},
                   {"Event Name": "Calculus",
                    "Start Time": "14:25",
                    "End Time": "15:20"}
                   ]
}

schedule_csv = open('/Users/tkmuro/PycharmProjects/tkProgramming/Labs/Lab1/my_schedule.csv', 'w')
writer = csv.writer(schedule_csv)
writer.writerow(["Date", "Event", "Start Time", "End Time"])
for k, v in schedule_dict.items():
    for event in range(len(schedule_dict[k])):
        writer.writerow([k, schedule_dict[k][event]["Event Name"], schedule_dict[k][event]["Start Time"], schedule_dict[k][event]["End Time"]])
    writer.writerow("")