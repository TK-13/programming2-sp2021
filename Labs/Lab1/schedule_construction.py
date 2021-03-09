import csv

schedule_dict = {
    "03/08/2021": [{"Event Name": "Comedy and Literature",
                    "Start Time": "8:10",
                    "End Time": "9:00"},
                    {"Event Name": "dummy conflict",
                    "Start Time": "8:10",
                    "End Time": "9:00"},
                   {"Event Name": "Calculus",
                    "Start Time": "10:05",
                    "End Time": "10:55"},
                   {"Event Name": "Programming II",
                    "Start Time": "12:30",
                    "End Time": "1:20"},
                   {"Event Name": "Computer Animation",
                    "Start Time": "2:25",
                    "End Time": "3:15"},
                   {"Event Name": "dummy conflict 2",
                    "Start Time": "2:25",
                    "End Time": "3:15"},
                   {"Event Name": "Senior Seminar",
                    "Start Time": "3:20",
                    "End Time": "4:10"}
                   ],
    "03/09/2021": [{"Event Name": "Programming II",
                    "Start Time": "8:10",
                    "End Time": "9:00"},
                   {"Event Name": "Computer Animation",
                    "Start Time": "10:05",
                    "End Time": "10:55"},
                   {"Event Name": "Calculus",
                    "Start Time": "12:30",
                    "End Time": "1:20"},
                   {"Event Name": "Comedy and Literature",
                    "Start Time": "1:25",
                    "End Time": "2:15"}
                   ],
    "03/10/2021": [{"Event Name": "Gym D",
                    "Start Time": "8:45",
                    "End Time": "9:00"},
                   {"Event Name": "Student Government",
                    "Start Time": "10:00",
                    "End Time": "10:45"},
                   {"Event Name": "Graderoom",
                    "Start Time": "1:05",
                    "End Time": "1:45"},
                   {"Event Name": "Advisory",
                    "Start Time": "1:50",
                    "End Time": "2:30"},
                   {"Event Name": "Robotics",
                    "Start Time": "3:45",
                    "End Time": "4:35"}
                   ],
    "03/11/2021": [{"Event Name": "Calculus",
                    "Start Time": "8:10",
                    "End Time": "9:00"},
                   {"Event Name": "Comedy and Literature",
                    "Start Time": "9:05",
                    "End Time": "9:55"},
                   {"Event Name": "Advanced Topics in Physics",
                    "Start Time": "11:00",
                    "End Time": "11:50"},
                   {"Event Name": "Computer Animation",
                    "Start Time": "1:25",
                    "End Time": "2:15"},
                   {"Event Name": "Programming II",
                    "Start Time": "2:25",
                    "End Time": "3:20"}
                   ],
    "03/12/2021": [{"Event Name": "Computer Animation",
                    "Start Time": "9:05",
                    "End Time": "9:55"},
                   {"Event Name": "Programming II",
                    "Start Time": "11:00",
                    "End Time": "11:50"},
                   {"Event Name": "Comedy and Literature",
                    "Start Time": "1:25",
                    "End Time": "2:15"},
                   {"Event Name": "Calculus",
                    "Start Time": "2:25",
                    "End Time": "3:20"}
                   ]
}

schedule_csv = open('/Users/tkmuro/PycharmProjects/tkProgramming/Labs/Lab1/my_schedule.csv', 'w')
writer = csv.writer(schedule_csv)
writer.writerow(["Date", "Event", "Start Time", "End Time"])
for k, v in schedule_dict.items():
    for event in range(len(schedule_dict[k])):
        writer.writerow([k, schedule_dict[k][event]["Event Name"], schedule_dict[k][event]["Start Time"], schedule_dict[k][event]["End Time"]])
    writer.writerow("")