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