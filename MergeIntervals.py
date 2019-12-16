# Given a list of intervals, merge all the overlapping intervals to produce a list that has only mutually exclusive intervals.
# Time: O(NlogN), Space: O(N)

def merge(intervals):
    if not intervals or not intervals[0]:
        return intervals
    
    intervals.sort()
    res = [intervals[0]]
    for i in range(len(intervals)):
        temp = intervals[i]
        if temp[0] <= res[-1][1]:
            res[-1][1] = max(res[-1][1], temp[1])
        else:
            res.append(temp)
    return res
    

# Given a list of non-overlapping intervals sorted by their start time,
# insert a given interval at the correct position and merge all necessary intervals to produce a list that has only mutually exclusive intervals.
# O(N)

def insert(intervals, new_interval):
    i, start, end = 0, 0, 1
    res = []

    while i < len(intervals) and intervals[i][end] < new_interval[start]:
        res.append(intervals[i])
        i += 1
    
    res.append([min(intervals[i][start], new_interval[start]), max(intervals[i][end], new_interval[end])])

    for j in range(i+1, len(intervals)):
        temp = intervals[j]
        if temp[0] <= res[-1][1]:
            res[-1][1] = max(res[-1][1], temp[1])
        else:
            res.append(temp)
    return res


# Given two lists of intervals, find the intersection of these two lists. Each list consists of disjoint intervals sorted on their start time.
# Time: O(M+N)

def merge(intervals_a, intervals_b):
    res = []
    i, j, start, end = 0, 0, 0, 1
    while i < len(intervals_a) and j < len(intervals_b):
        a_over_b = intervals_a[i][start] >= intervals_b[j][start] and intervals_a[i][start] <= intervals_b[j][end]

        b_over_a = intervals_b[j][start] >= intervals_a[i][start] and intervals_b[j][start] <= intervals_a[i][end]

        if a_over_b or b_over_a:
            res.append([max(intervals_a[i][start], intervals_b[j][start]),
                        min(intervals_a[i][end], intervals_b[j][end])])
        
        if intervals_a[i][end] < intervals_b[j][end]:
            i += 1
        else:
            j += 1
    return res

# Given an array of intervals representing ‘N’ appointments, find out if a person can attend all the appointments.
# Time: O(NlogN)

def can_attend_all_appointments(intervals):
    if len(intervals) <= 1:
        return True
    intervals.sort()
    cur_end = intervals[0][1]
    for elem in intervals[1:]:
        if elem[0] < cur_end:
            return False
        else:
            cur_end = elem[1]
    return True

# Given a list of appointments, find all the conflicting appointments.

def find_conlict(intervals):
    if len(intervals) <= 1:
        return []
    intervals.sort()
    res = []
    for i in range(len(intervals)-1):
        for j in range(i+1, len(intervals)):
            if intervals[j][0] < intervals[i][1]:
                res.append([intervals[i], intervals[j]])
            else:
                break
                    
    return res


# Given a list of intervals representing the start and end time of ‘N’ meetings, find the minimum number of rooms required to hold all the meetings.
# Given a list of intervals, find the point where the maximum number of intervals overlap.
# Time: O(NlogN)

from heapq import *
def min_meeting_rooms(meetings):
    meetings.sort()
    minRooms = 0
    minHeap = []
    for meeting in meetings:
        while len(minHeap) > 0 and meeting[0] >= minHeap[0][0]:
            heappop(minHeap)
        heappush(minHeap, [meeting[1], meeting[0]]) # Need to switch the start and end, cause we sort by end time in minHeap.
        minRooms = max(minRooms, len(minHeap))
    return minRooms
            
    
# We are given a list of Jobs. Each job has a Start time, an End time, and a CPU load when it is running. Our goal is to find the maximum CPU load at any time if all the jobs are running on the same machine.
# Time: O(NlogN)


def find_max_cpu_load(jobs):
    jobs.sort()
    maxLoad, curLoad = 0, 0
    minHead = []
    for job in jobs:
        while len(minHead) > 0 and job[0] >= minHead[0][0]:
            curLoad -= minHead[0][2]
            heappop(minHead)
        heappush(minHead, [job[1], job[0], job[2]]) # Need to switch the start and end, cause we sort by end time in minHeap.
        curLoad += job[2]
        maxLoad = max(curLoad, maxLoad)
    return maxLoad


# For ‘K’ employees, we are given a list of intervals representing the working hours of each employee.
# Our goal is to find out if there is a free interval that is common to all employees. 
# You can assume that each list of employee working hours is sorted on the start time.

# 1. put all intervals together and then sort. Finally try to merge the intervals
# Time: O(NlogN)

# 2. Use minHeap
# Time: O(N*logK)
class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    

class EmployeeInterval:
    def __init__(self, interval, employeeIndex, intervalIndex):
        self.interval = interval
        self.employeeIndex = employeeIndex
        self.intervalIndex = intervalIndex
    
    def __lt__(self, other):
        return self.interval.start < other.interval.start


def find_employee_free_time(schedule):
    n = len(schedule)
    res = []
    if not schedule or n == 0:
        return res
    minHeap = []
    for i in range(n):
        heappush(minHeap, EmployeeInterval(schedule[i][0], i, 0))
    
    preInterval = minHeap[0].interval
    while minHeap:
        queueTop = heappop(minHeap)
        if preInterval.end < queueTop.interval.start:
            res.append(Interval(preInterval.end, queueTop.interval.start))
            preInterval = queueTop.interval
        else:
            if preInterval.end < queueTop.interval.end:
                preInterval = queueTop.interval
        employeeSchedule = schedule[queueTop.employeeIndex]
        if len(employeeSchedule) > queueTop.intervalIndex + 1:
            heappush(minHeap, EmployeeInterval(employeeSchedule[queueTop.intervalIndex+1], queueTop.employeeIndex, queueTop.intervalIndex+1))
    return res