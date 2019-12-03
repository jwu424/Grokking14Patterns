# Design a class to calculate the median of a number stream. The class should have the following two methods:
# insertNum(int num): stores the number in the class
# findMedian(): returns the median of all numbers inserted in the class
# If the count of numbers inserted in the class is even, the median will be the average of the middle two numbers.

# Time: Insert: O(logN); Find: O(1)
from heapq import *
class MedianOfAStream():
    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def insert_num(self, num):
        if not self.maxHeap or -self.maxHeap[0] >= num:
            heappush(self.maxHeap, -num)
        else:
            heappush(self.minHeap, num)
        
        if len(self.maxHeap) > len(self.minHeap) + 1:
            heappush(self.minHeap, -heappop(self.maxHeap))
        elif len(self.maxHeap) < len(self.minHeap):
            heappush(self.maxHeap, -heappop(self.minHeap))

    def find_median(self):
        if len(self.minHeap) == len(self.maxHeap):
            return (self.minHeap[0] - self.maxHeap[0]) / 2.0
        elif len(self.maxHeap) > len(self.minHeap):
            return -self.maxHeap[0] / 1.0

# Given an array of numbers and a number ‘k’, find the median of all the ‘k’ sized sub-arrays (or windows) of the array.
# Time: O(N*log(K))

class SlidingWindowMedian():
    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
    
    def find_sliding_window_median(self, nums, k):
        if k == 1:
            return nums
        if k == 2:
            return [sum(a) / 2.0 for a in list(zip(nums, nums[1:]))]
        res = [0 for x in range(len(nums)-k+1)]
        for i in range(len(nums)):
            if not self.maxHeap or nums[i] <= -self.maxHeap[0]:
                heappush(self.maxHeap, -num[i])
            else:
                heappush(sefl.minHeap, num[i])
            self.rebalance_heaps()
            
            if i - k + 1 >= 0:
                if len(self.minHeap) == len(self.maxHeap):
                    res[i-k+1] = (self.minHeap[0] - self.maxHeap[0]) / 2.0
                else:
                    res[i-k+1] = -self.maxHeap[0] / 1.0
                
                elemToRemoved = nums[i-k+1]
                if elemToRemoved <= -self.maxHeap[0]:
                    self.remove(self.maxHeap, -elemToRemoved)
                else:
                    self.remove(self.minHeap, elemToRemoved)

                self.rebalance_heaps()
        return res

    def rebalance_heaps(self):
        if len(self.maxHeap) > len(self.minHeap) + 1:
            heappush(self.minHeap, -heappop(self.maxHeap))
        elif len(self.maxHeap) < len(self.minHeap):
            heappush(self.maxHeap, -heappop(self.minHeap))
    
    def remove(self, heap, elem):
        ind = heap.index(elem)
        heap[ind] = heap[-1]
        del heap[-1]
        if ind < len(heap):
            heapq._siftup(heap, ind)
            heapq._siftdown(heap, 0, ind)


# Given a set of investment projects with their respective profits, we need to find the most profitable projects. 
# We are given an initial capital and are allowed to invest only in a fixed number of projects. Our goal is to choose projects that give us the maximum profit.
# We can start an investment project only when we have the required capital. Once a project is selected, we can assume that its profit has become our capital.
# Time: O(NlogN + KlogN)

def find_maximum_capital(capital, profits, numberOfProjects, initialCapital):
    minCapitalHeap = []
    maxProfitHeap = []

    for i in range(len(capital)):
        heappush(minCapitalHeap, (capital[i], i))
    
    availableCapital = initialCapital

    for _ in range(numberOfProjects):
        while minCapitalHeap and minCapitalHeap[0] <= availableCapital:
            capital, i = heappop(minCapitalHeap)
            heappush(maxProfitHeap, (-profits[i], i))
        
        if not maxProfitHeap:
            break
        availableCapital += -heappop(maxProfitHeap)[0]
    return availableCapital

# Given an array of intervals, find the next interval of each interval. 
# In a list of intervals, for an interval ‘i’ its next interval ‘j’ will have the smallest ‘start’ greater than or equal to the ‘end’ of ‘i’.
# Write a function to return an array containing indices of the next interval of each input interval. 
# If there is no next interval of a given interval, return -1. It is given that none of the intervals have the same start point.

def find_next_interval(intervals):
    maxStartHeap = []
    maxEndHeap = []
    n = len(intervals)

    res = [-1] * n
    for endIndex in range(n):
        heappush(maxStartHeap, (-intervals[endIndex].start, endIndex))
        heappush(maxEndHeap, (-intervals[endIndex].end, endIndex))
    
    for _ in range(n):
        topEnd, endIndex = heappop(maxEndHeap)
        if -maxStartHeap[0][0] >= -topEnd:
            topStart, startIndex = heappop(maxStartHeap)
            while maxStartHeap and -maxStartHeap[0][0] >= -topEnd:
                topStart, startIndex = heappop(maxStartHeap)
            res[endIndex] = startIndex
            heappush(maxStartHeap, (topStart, startIndex))
    return res
