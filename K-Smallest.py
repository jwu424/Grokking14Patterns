# Given an unsorted array of numbers, find Kth smallest number in it.
# Please note that it is the Kth smallest number in the sorted order, not the Kth distinct element.

from heapq import *
import random
# 1.Brute force
# Time: O(N^2)
def find_Kth_smallest_number1(nums, k):
    preSmallNum, preSmallIndex = float('-inf'), -1
    curSmallNum, curSmallIndex = float('inf'), -1
    for i in range(k):
        for j in range(len(nums)):
            if nums[j] > preSmallNum and nums[j] < curSmallNum:
                curSmallNum, curSmallIndex = nums[j], j
            elif nums[j] == preSmallNum and j > preSmallIndex:
                curSmallNum, curSmallIndex = nums[j], j
                break
        preSmallNum, preSmallIndex = curSmallNum, curSmallIndex
        curSmallNum = float('inf')
    return preSmallNum


# 2.HeapSort
# Time: O(NlogN)
def find_Kth_smallest_number2(nums, k):
    return sorted(nums)[k-1]


# 3.MaxHeap
# Time: O(NlogK)
def find_Kth_smallest_number3(nums, k):
    maxHeap = []
    for i in range(k):
        heappush(maxHeap, -nums[i])
    for i in range(k, len(nums)):
        if -nums[i] > maxHeap[0]:
            heappushpop(maxHeap, -nums[i])
    return -maxHeap[0]

# 4.MinHeap
# Time: O(KlogN)
def find_Kth_smallest_number4(nums, k):
    minHeap = []
    for i in range(len(nums)):
        heappush(minHeap, nums[i])
    return minHeap[k-1]


# 5.Using Partition Scheme of Quicksort

def find_Kth_smallest_number5(nums, k):
    return find_Kth_smallest_number4_rec(nums, k, 0, len(nums)-1)

def find_Kth_smallest_number4_rec(nums, k, start, end):
    p = partiton(nums, start, end)

    if p == k-1:
        return nums[p]
    if p > k-1:
        return find_Kth_smallest_number4_rec(nums, k, start, p-1)
    return find_Kth_smallest_number4_rec(nums, k, p+1, end)

def partiton(nums, low, high):
    if low == high:
        return low
    pivot = nums[high]
    for i in range(low, high):
        if nums[i] < pivot:
            nums[low], nums[i] = nums[high], nums[low]
            low += 1
    nums[low], nums[high] = nums[high], nums[low]
    return low


# 6.Using Randomized Partitioning Scheme of Quicksort

def find_Kth_smallest_number5(nums, k):
    return find_Kth_smallest_number4_rec(nums, k, 0, len(nums)-1)

def find_Kth_smallest_number4_rec(nums, k, start, end):
    p = partiton(nums, start, end)

    if p == k-1:
        return nums[p]
    if p > k-1:
        return find_Kth_smallest_number4_rec(nums, k, start, p-1)
    return find_Kth_smallest_number4_rec(nums, k, p+1, end)

def partiton(nums, low, high):
    if low == high:
        return low

    pivotIndex = random.randint(low, high)
    nums[pivotIndex], nums[high] = nums[high], nums[pivotIndex]
    for i in range(low, high):
        if nums[i] < pivot:
            nums[low], nums[i] = nums[high], nums[low]
            low += 1
    nums[low], nums[high] = nums[high], nums[low]
    return low