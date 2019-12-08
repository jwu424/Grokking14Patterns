# Given an unsorted array of numbers, find the ‘K’ largest numbers in it.
# Time: O(NlogK); Space: O(logK)

from heapq import *
def find_k_largest_numbers(nums, k):
    nums = list(set(nums))
    minHeap = []
    for i in range(k):
        heappush(minHeap, nums[i])
    for i in range(k, len(nums)):
        if nums[i] > minHeap[0]:
            heappop(minHeap)
            heappush(minHeap, nums[i])
    return list(minHeap)


# Given an unsorted array of numbers, find Kth smallest number in it.
#Please note that it is the Kth smallest number in the sorted order, not the Kth distinct element.
# Time: O(NlogK); Space: O(logK)

def find_Kth_smallest_number(nums, k):
    minHeap = []
    for i in range(k):
        heappush(minHeap, -nums[i])
    for i in range(k, len(nums)):
        if -nums[i] > minHeap[0]:
            heappop(minHeap)
            heappush(minHeap, -nums[i])
    return minHeap[0] * (-1)
    

# Given an array of points in the a 2D plane, find ‘K’ closest points to the origin.
# Time: O(NlogK); Space: O(K)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # used for max-heap
    def __lt__(self, other):
        return self.distance_from_origin() > other.distance_from_origin()

    def distance_from_origin(self):
        return (self.x * self.x) + (self.y * self.y)

    def print_point(self):
        print("[" + str(self.x) + ", " + str(self.y) + "] ", end='')


def find_closest_points(points, k):
    maxHeap = []
    for i in range(k):
        heappush(maxHeap, points[i])

    for i in range(k, len(points)):
        if points[i].distance_from_origin() < maxHeap[0].distance_from_origin():
            heappop(maxHeap)
            heappush(maxHeap, points[i])

    return list(maxHeap)

# Given ‘N’ ropes with different lengths, we need to connect these ropes into one big rope with minimum cost. 
# The cost of connecting two ropes is equal to the sum of their lengths.
# Time: O(NlogN); Space: O(K)

def minimum_cost_to_connect_ropes(ropeLengths):
    minHeap = []
    res = 0
    for elem in ropeLengths:
        heappush(minHeap, elem)
    while len(minHeap) > 1:
        elem1 = heappop(minHeap)
        elem2 = heappop(minHeap)
        heappush(minHeap, elem1+elem2)
        res = res + elem1 + elem2
    return res

# Given an unsorted array of numbers, find the top ‘K’ frequently occurring numbers in it.
# Time: O(N + N*logK)

from heapq import *

def find_k_frequent_numbers(nums, k):
    count = {}
    for elem in nums:
        count[elem] = count.get(elem, 0) + 1
    minHeap = []
    for num, freq in count.items():
        heappush(minHeap, (freq, num))
        if len(minHeap) > k:
            heappop(minHeap)
    res = []
    while minHeap:
        res.append(heappop(minHeap)[1])
    return res

# Given a string, sort it based on the decreasing frequency of its characters.
# Time: O(N + D*logD). D: ditinct elem. 

def sort_character_by_frequency(str):
    count = {}
    for elem in str:
        count[elem] = count.get(elem, 0) + 1
    minHeap = []
    for cha, freq in count.items():
        heappush(minHeap, (-freq, cha))
    res = []
    while minHeap:
        freq, cha = heappop(minHeap)
        res.append((-freq) * cha)
    return ''.join(res)

# Design a class to efficiently find the Kth largest element in a stream of numbers.
# The class should have the following two things:
# The constructor of the class should accept an integer array containing initial numbers from the stream and an integer ‘K’.
# The class should expose a function add(int num) which will store the given number and return the Kth largest number.

class KthLargestNumberInStream:
    def __init__(self, nums, k):
        self.minHeap = []
        self.k = k
        for elem in nums:
            self.add(elem)

    def add(self, num):
        heappush(self.minHeap, num)
        if len(self.minHeap) > self.k:
            heappop(self.minHeap)
        return self.minHeap[0]


# Given a sorted number array and two integers ‘K’ and ‘X’, find ‘K’ closest numbers to ‘X’ in the array. 
# Return the numbers in the sorted order.
# Time: O(N*logN)

def find_closest_elements(arr, K, X):
    minHeap = []
    res = []
    for elem in arr:
        heappush(minHeap, (abs(X-elem), elem))
    while K > 0:
        res.append(heappop(minHeap)[1])
        K -= 1
    return sorted(res)


# Given an array of numbers and a number ‘K’, we need to remove ‘K’ numbers from the array such that we are left with maximum distinct numbers.
# Time: O(NlogK + KlogK)

def find_maximum_distinct_elements(nums, k):
    if len(nums) <= k:
        return 0
    count = {}
    minHeap = []
    res = 0
    for elem in nums:
        count[elem] = count.get(elem, 0) + 1
    for num, freq in count.items():
        if freq == 1:
            res += 1
        else:
            heappush(minHeap, (freq, num))
    while minHeap and k > 0:
        freq, num = heappop(minHeap)
        k -= freq - 1
        if k >= 0:
            res += 1
    if k > 0:
        res -= k
    return res


# Given an array, find the sum of all numbers between the K1’th and K2’th smallest elements of that array.
# Time: O(NlogN)

def find_sum_of_elements(nums, k1, k2):
    minHeap = []
    for num in nums:
        heappush(minHeap, num)
    for _ in range(k1):
        heappop(minHeap)

    elemSum = 0
    for _ in range(k2-k1-1):
        elemSum += heappop(minHeap)
    return elemSum


# Given a string, find if its letters can be rearranged in such a way that no two same characters come next to each other.
# Time: O(NlogN)

def rearrange_string(str):
    count = {}
    for elem in str:
        count[elem] = count.get(elem, 0) + 1
    maxHeap = []
    for elem, freq in count.items():
        heappush(maxHeap, (-freq, elem))
    
    prev_freq, prev_elem = 0, None
    res = []
    while maxHeap:
        freq, elem = heappop(maxHeap)
        if prev_elem and -prev_freq > 0:
            heappush(maxHeap, (prev_freq, prev_elem))
        res.append(elem)
        prev_elem = elem
        prev_freq = freq + 1
    return ''.join(res) if len(res) == len(str) else ""