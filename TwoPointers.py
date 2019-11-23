# Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.
# Time complexity: O(N)

def pair_with_targetsum(arr, target_sum):
    f, s = 0, len(arr) - 1
    while f < s:
        if arr[f] + arr[s] == target_sum:
            return [f, s]
        elif arr[f] + arr[s] < target_sum:
            f += 1
        else:
            s -= 1
    return [-1, -1]

# Given an array of sorted numbers, remove all duplicates from it. You should not use any extra space; after removing the duplicates in-place
# return the new length of the array.
# Time complexity: O(N)

def remove_duplicates(arr):
    if len(arr) <= 1:
        return len(arr)
    f, s = 1, 1
    while s < len(arr):
        if arr[f-1] != arr[s]:
            arr[f] = arr[s]
            f += 1
        s += 1
    return f

# Given an unsorted array of numbers and a target ‘key’, remove all instances of ‘key’ in-place and return the new length of the array.
# Time: O(N)

def remove_element(arr, key):
    nextElem = 0
    for i in range(len(arr)):
        if arr[i] != key:
            arr[nextElem] = arr[i]
            nextElem += 1
    return nextElem



def remove_element(arr, key):
    if len(arr) == 0:
        return 0
    if len(arr) == 1 and arr[0] == key:
        return 0
    if len(arr) == 1 and arr[0] != key:
        return 1
    f, s = 0, len(arr)-1
    while f < s:
        while arr[s] == key:
            s -= 1
        if arr[f] == key:
            arr[f], arr[s] = arr[s], arr[f]
            s -= 1
            f += 1
        else:
            f += 1
    return f


# Given a sorted array, create a new array containing squares of all the number of the input array in the sorted order.
# Time: O(N)

def make_squares(arr):
    if not arr:
        return []
    res = [0] * len(arr)
    l, r, highIndex = 0, len(arr)-1, len(arr)-1
    while l <= r:
        left_val = arr[l] * arr[l]
        right_val = arr[r] * arr[r]
        if left_val > right_val:
            res[highIndex] = left_val
            l += 1
        else:
            res[highIndex] = right_val
            r -= 1
        highIndex -= 1
    return res

# Given an array of unsorted numbers, find all unique triplets in it that add up to zero.
# Time: O(N^2)
class Solution():
    def search_triplets(arr):
        arr.sort()
        res = []
        for i in range(len(arr)-2):
            if i > 0 and arr[i] == arr[i-1]:
                continue
            self.search_two(arr, -arr[i], i+1, res)
        return res

    def search_two(self, arr, target, left, res):
        right = len(arr) - 1
        while left < right:
            temp = arr[left] + arr[right]
            if temp == target:
                res.append([-target, arr[left], arr[right]])
                left += 1
                right -= 1
                while left < right and arr[left] == arr[left-1]:
                    left += 1
                while left < right and arr[right] == arr[right+1]:
                    right -= 1
            elif temp < target:
                left += 1
            else:
                right -= 1


# Given an array of unsorted numbers and a target number, find a triplet in the array whose sum is as close to the target number as possible, 
# return the sum of the triplet. If there are more than one such triplet, return the sum of the triplet with the smallest sum.
# Time: O(N^2)

def triplet_sum_close_to_target(arr, target_sum):
    arr.sort()
    smaller_diff = float('inf')
    for i in range(len(arr)-2):
        if i > 0 and arr[i] == arr[i-1]:
            continue
        left = i + 1
        right = len(arr) - 1
        while left < right:
            target_diff = target_sum - arr[left] - arr[right] - arr[i]
            if target_diff == 0:
                return target_sum
            if abs(target_diff) < abs(smaller_diff) or (abs(target_diff) == abs(smaller_diff) and target_diff > smaller_diff):
                smaller_diff = target_diff
            elif target_diff > 0:
                left += 1
            else:
                right -= 1
    return target_sum - smaller_diff


# Given an array arr of unsorted numbers and a target sum, count all triplets in it such that arr[i] + arr[j] + arr[k] < target
# where i, j, and k are three different indices. Write a function to return the count of such triplets.
# Time: O(N^2)

def triplet_with_smaller_sum(arr, target):
    arr.sort()
    count = 0
    for i in range(len(arr)-2):
        count += search_two(arr, target-arr[i], i)
    return count

def search_two(arr, target_sum, first):
    count = 0
    left, right = first+1, len(arr) - 1
    while left < right:
        if arr[left] + arr[right] < target_sum:
            count += right - left
            left += 1
        else:
            right -= 1
    return count


# Write a function to return the list of all such triplets instead of the count. How will the time complexity change in this case?
# Time: O(N^3)

def triplet_with_smaller_sum(arr, target):
    arr.sort()
    res = =[]
    for i in range(len(arr)-2):
        search_two(arr, target-arr[i], i, res)
    return count

def search_two(arr, target_sum, first, res):
    count = 0
    left, right = first+1, len(arr) - 1
    while left < right:
        if arr[left] + arr[right] < target_sum:
            for j in range(left, right-1):
                res.append([arr[first], arr[left], att[i]])
            left += 1
        else:
            right -= 1

# Given an array with positive numbers and a target number, find all of its contiguous subarrays whose product is less than the target number.
# Time: O(N^2), Space for out list: O(N*(N+1)/2) = O(N^2)
from collections import deque
def find_subarrays(arr, target):
    cur = 1
    slow = 0
    res = []
    for i in range(len(arr)):
        cur *= arr[i]
        while cur >= target and slow <= i:
            cur /= arr[slow]
            slow += 1
        temp = deque()
        for j in range(i, slow-1, -1):
            temp.appendleft(arr[j])
            res.append(list(temp))
    return res        
        

# Given an array containing 0s, 1s and 2s, sort the array in-place. You should treat numbers of the array as objects, hence, we can’t count 0s, 1s, and 2s to recreate the array.

# The flag of the Netherlands consists of three colors: red, white and blue; and since our input array also consists of three different numbers that is why it is called Dutch National Flag problem.

def dutch_flag_sort(arr):
    zero_index, two_index = 0, len(arr)-1
    i = 0
    while i <= two_index:
        if arr[i] == 0:
            arr[i], arr[zero_index] = arr[zero_index], arr[i]
            i += 1
            zero_index += 1
        elif arr[i] == 2:
            arr[i], arr[two_index] = arr[two_index], arr[i]
            two_index -= 1
        else:
            i += 1


# Given an array of unsorted numbers and a target number, find all unique quadruplets in it, whose sum is equal to the target number.
# Time: O(N^3)
def search_quadruplets(arr, target):
    if len(arr) < 4:
        return []
    arr.sort()
    res = []
    for i in range(len(arr)-3):
        for j in range(i+1, len(arr)-2):
            first, second = arr[i], arr[j]
            temp_target = target - first - second
            left, right = j+1, len(arr)-1
            while left < right:
                temp = arr[left] + arr[right]
                if temp == temp_target:
                    res.append([first, second, arr[left], arr[right]])
                    left += 1
                    right -= 1
                    while (left < right and arr[left] == arr[left-1]):
                        left += 1
                    while (left< right and arr[right] == arr[right+1]):
                        right -= 1
                elif temp < temp_target:
                    left += 1
                else:
                    right -= 1
    return res


# Given two strings containing backspaces (identified by the character ‘#’), check if the two strings are equal.

from collections import deque
def backspace_compare1(str1, str2):
    s1 = clean(str1)
    s2 = clean(str2)
    return s1 == s2

def clean(str):
    res = deque()
    count = 0
    for i in range(len(str)-1, -1, -1):
        if str[i] == '#':
            count += 1
        elif str[i] != '#' and count > 0:
            count -= 1
        else:
            res.appendleft(str[i])
    return list(res)


def backspace_compare2(str1, str2):
    index1 = len(str1) - 1
    index2 = len(str2) - 1
    while index1 >= 0 or index2 >= 0:
        i1 = get_next_word(str1, index1)
        i2 = get_next_word(str2, index2)

        if str1[i1] != str2[i2]:
            return False
        if i1 < 0 and i2 < 0:
            return True
        if i1 < 0 or i2 < 0:
            return False
        index1 = i1 - 1
        index2 = i2 - 1
    return True

def get_next_word(str, index):
    count = 0
    while index >= 0:
        if str[index] == '#':
            count += 1
        elif count > 0:
            count -= 1
        else:
            break
        index -= 1
    return index


# Given an array, find the length of the smallest subarray in it which when sorted will sort the whole array.

def shortest_window_sort(arr):
    low, high = 0, len(arr) - 1
    while low < len(arr)-1 and arr[low] <= arr[low+1]:
        low += 1
    if low == len(arr) - 1:
        return 0
    
    while high >= 0 and arr[high] >= arr[high-1]:
        high -= 1
    
    submax = max(arr[low:high+1])
    submin = min(arr[low:high+1])

    while low > 0 and arr[low-1] > submin:
        low -= 1
    while high < len(arr) - 1 and arr[high+1] < submax:
        high += 1
    return high - low + 1
    

# Suppose you are given an array containing non-negative numbers representing heights of a set of buildings. 
# Now, because of differences in heights of buildings water can be trapped between them. Find the two buildings
# that will trap the most amount of water. Write a function that will return the maximum volume of water that will be trapped between these two buildings.


def find_max_water(building_heights):
    left, right = 0, len(building_heights) - 1
    max_area, current_area = 0, 0

    while left < right:
        if building_heights[left] < building_heights[right]:
            current_area = (right - left) * building_heights[left]
            left += 1
        else:
            current_area = (right - left) * building_heights[right]
            right -= 1
        max_area = max(max_area, current_area)
    return max_area