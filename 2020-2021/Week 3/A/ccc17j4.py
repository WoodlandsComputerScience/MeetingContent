duration=int(input())
hours = 12
minutes = 0
ans = duration//720*31
duration = duration % 720
 
for i in range(duration):
    minutes = int(minutes)+1
    if(minutes == 60):
        if(hours == 12):
            hours = 1
        else:
            hours = hours + 1
        minutes = 0
    if(len(str(minutes)) < 2):
        minutes = "0"+str(minutes)
    time = []
    for num in str(hours):
        time.append(int(num))
    for num in str(minutes):
        time.append(int(num))
 
    if(len(time) == 3):
        if(time[1]-time[0] == time[2]-time[1]):
            ans += 1
    else:
        if(time[1]-time[0] == time[2]-time[1] and (time[2]-time[1] == time[3]-time[2])):
            ans += 1
print(ans)
