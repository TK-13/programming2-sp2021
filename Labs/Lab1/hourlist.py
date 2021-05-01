open_times = []

for h in range(20):
    if h <= 9:
        hour = ("0"+ str(h))
    else:
        hour = str(h)
    for m in range(59):
        if m <= 9:
            open_times.append(hour + ":0" + str(m))
        else:
            open_times.append(hour + ":" + str(m))

print(open_times)
# print((str(h) for h in range(20)) + ":" + (str(m) for m in range(59)))