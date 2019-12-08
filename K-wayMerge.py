# Given an array of ‘K’ sorted LinkedLists, merge them into one sorted list.
# Time: O(NlogK)

from heapq import *

class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

  # used for the min-heap
    def __lt__(self, other):
        return self.value < other.value


def merge_lists(lists):
    minHeap = []
    for root in lists:
        if root:
            heappush(minHeap, root)
    resHead, resTail = None, None
    while minHeap:
        node = heappop(minHeap)
        if not resHead:
            resHead = resTail = node
        else:
            resTail.next = node
            resTail = resTail.next
        if node.next:
            heappush(minHeap, node.next)
    return resHead


# Given ‘M’ sorted arrays, find the K’th smallest number among all the arrays.

# Time: less than O(NlogK)
def find_Kth_smallest1(lists, k):
    maxHeap = []
    for row in lists:
        for i in range(len(row)):
            if len(maxHeap) < k:
                heappush(maxHeap, -row[i])
            else:
                if row[i] < -maxHeap[0]:
                    heappushpop(maxHeap, -row[i])
                else:
                    break
    return -maxHeap[0]

# Time: O(KlogN)
def find_Kth_smallest2(lists, k):
    minHeap = []
    for i in range(len(lists)):
        heappush(minHeap, (list[i][0], 0, lists[i]))
    count, number = 0, 0
    while minHeap:
        number, i, list = heappop(minHeap)
        count += 1
        if count == k:
            break
        if len(list) > i + 1:
            heappush(minHeap, (list[i+1], i+1, list))

    return number


# Given an N * N matrix where each row and column is sorted in ascending order, find the Kth smallest element in the matrix.
# Time: O(KlogN)

def find_Kth_smallest1(lists, k):
    minHeap = []
    for i in range(min(k, len(lists))):
        heappush(minHeap, (list[i][0], 0, lists[i]))
    count, number = 0, 0
    while minHeap:
        number, i, list = heappop(minHeap)
        count += 1
        if count == k:
            break
        if len(list) > i + 1:
            heappush(minHeap, (list[i+1], i+1, list))

    return number

# Time: O(Nlog(max-min))

def find_Kth_smallest2(matrix, k):
    n = len(matrix)
    start, end = matrix[0][0], end = matrix[-1][-1]
    while start < end:
        mid = start + (end - start)//2
        smaller, larger = (matrix[0][0], matrix[n-1][n-1])
        count, smaller, larger = count_less_equal(matrix, mid, smaller, larger)
        if count == k:
            return smaller
        if count < k:
            start = larger
        else:
            end = smaller
    return start

def count_less_equal(matrix, mid, smaller, larger):
    count, n = 0, len(matrix)
    row, col = n-1, 0
    while row >= 0 and col < n:
        if matrix[row][col] > mid:
            larger = min(larger, matrix[row][col])
            row -= 1
        else:
            smaller = max(smaller, matrix[row][col])
            count += row + 1
            col += 1
    return count, smaller, larger


# Given ‘M’ sorted arrays, find the smallest range that includes at least one number from each of the ‘M’ lists.
# Time: O(NlogM). M input arrays. N total num

def find_smallest_range(lists):
    minHeap = []
    rangeStart, rangeEnd = 0, float('inf')
    curMax = float('-inf')
    for arr in lists:
        heappush(minHeap, (arr[0], 0, arr))
        curMax = max(curMax, arr[0])
    while len(minHeap) == len(lists):
        num, i, arr = heappop(minHeap)
        if rangeEnd - rangeStart > curMax - num:
            rangeStart = num
            rangeEnd = curMax
        if len(arr) > i + 1:
            heappush(minHeap, (arr[i+1], i+1, arr))
            curMax = max(curm, arr[i+1])
    return [rangeStart, rangeEnd]

# Given two sorted arrays in descending order, find ‘K’ pairs with the largest sum where each pair consists of numbers from both the arrays.
# Time: O(N*M*logK) ==> O(K^2logK) if all have K elem. 

def find_k_largest_pairs(nums1, nums2, k):
    minHeap = []
    for i in range(min(k, len(nums1))):
        for j in range(min(k, len(nums2))):
            if len(minHeap) < k:
                heappush(minHeap, (nums1[i] + nums2[j], i, j))
            else:
                if nums1[i] + nums2[j] < minHeap[0][0]:
                    break
                else:
                    heappushpop(minHeap, (nums1[i] + nums2[j], i, j))
    res = []
    for (num, i, j) in minHeap:
        res.append([nums1[i], nums2[j]])
    return res