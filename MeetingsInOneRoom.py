def canAttendMeetings(intervals):
    intervals.sort(key=lambda x: x[0])
    for i in range(len(intervals) - 1):
        if intervals[i][1] > intervals[i + 1][0]:
            return False
    return True

Intervals1 = [(0,30),(5,10),(15,20)]
Intervals2 = [(5,8),(2,4)]
print(canAttendMeetings(Intervals1))
print(canAttendMeetings(Intervals2))