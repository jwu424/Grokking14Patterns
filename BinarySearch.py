# Given a sorted array of numbers, find if a given number ‘key’ is present in the array. 
# Though we know that the array is sorted, we don’t know if it’s sorted in ascending or descending order. 
# You should assume that the array can have duplicates.
# Write a function to return the index of the ‘key’ if it is present in the array, otherwise return -1.
# Time: O(log(N))
def binary_search(arr, key):
    start, end = 0, len(arr) - 1
    isAsc = arr[start] < arr[end]

    while start <= end:
        mid = start + (end - start) // 2
        if key == arr[mid]:
            return mid
        
        if isAsc:
            if key < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if key < arr[mid]:
                start = mid + 1
            else:
                end = mid - 1
    return -1


# Given an array of numbers sorted in an ascending order, find the ceiling of a given number ‘key’. 
# The ceiling of the ‘key’ will be the smallest element in the given array greater than or equal to the ‘key’.
# Write a function to return the index of the ceiling of the ‘key’. If there isn’t any ceiling return -1.
# Time: O(logN)

def search_ceiling_of_a_number(arr, key):
    if key > arr[-1]:
        return -1
    if key < arr[0]:
        return 0
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if key < arr[mid]:
            end = mid - 1
        elif key > arr[mid]:
            start = mid + 1
        else:
            return mid
    return start


# Given an array of numbers sorted in ascending order, find the floor of a given number ‘key’. 
# The floor of the ‘key’ will be the biggest element in the given array smaller than or equal to the ‘key’
# Write a function to return the index of the floor of the ‘key’. If there isn’t a floor, return -1.
# Time: O(logN)

def search_floor_of_a_number(arr, key):
    if key < arr[0]:
        return -1
    start, end = 0, len(arr)-1
    while start <= end:
        mid = start + (end - start) // 2
        if key < arr[mid]:
            end = mid - 1
        elif key > arr[mid]:
            start = mid + 1
        else:
            return mid
    return end


# Given an array of lowercase letters sorted in ascending order, find the smallest letter in the given array greater than a given ‘key’.
# Assume the given array is a circular list, which means that the last letter is assumed to be connected with the first letter. 
# This also means that the smallest letter in the given array is greater than the last letter of the array and is also the first letter of the array.
# Write a function to return the next letter of the given ‘key’.

# Time: O(logN)

def search_next_letter(letters, key):
    n = len(letters)
    if key < letters[0] or key >= letters[n - 1]:
        return letters[0]
    
    start, end = 0, n - 1
    while start <= end:
        mid = start + (end - start) // 2
        if key < letters[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return letters[start % n]


# Given an array of numbers sorted in ascending order, find the range of a given number ‘key’. 
# The range of the ‘key’ will be the first and last position of the ‘key’ in the array.
# Write a function to return the range of the ‘key’. If the ‘key’ is not present return [-1, -1].
# Time: O(logN)

def find_range(arr, key):
    res = [-1, -1]
    res[0] = binary_search_max_min(arr, key, False)
    if res[0] != -1:
        res[1] = binary_search_max_min(arr, key, True)
    return res

def binary_search_max_min(arr, key, IsMax):
    keyIndex = -1
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if key < arr[mid]:
            end = mid - 1
        elif key > arr[mid]:
            start = mid + 1
        else:
            keyIndex = mid
            if IsMax:
                start = mid + 1
            else:
                end = mid - 1
    return keyIndex 


# Given an infinite sorted array (or an array with unknown size), find if a given number ‘key’ is present in the array. 
# Write a function to return the index of the ‘key’ if it is present in the array, otherwise return -1.
# Since it is not possible to define an array with infinite (unknown) size, you will be provided with an interface ArrayReader to read elements of the array. 
# ArrayReader.get(index) will return the number at index; if the array’s size is smaller than the index, it will return Integer.MAX_VALUE.
# Time: O(logN)

class ArrayReader:

    def __init__(self, arr):
        self.arr = arr

    def get(self, index):
        if index >= len(self.arr):
            return math.inf
        return self.arr[index]


def search_in_infinite_array(reader, key):
    start, end = 0, 1
    while reader.get(end) < key:
        newstart = end + 1
        end += (end - start + 1) * 2
        start = newstart
    return binary_search(reader, key, start, end)

def binary_search(reader, key, start, end):
    while start <= end:
        mid = start + (end - start) // 2
        if reader.get(mid) == key:
            return mid
        elif reader.get(mid) < key:
            start = mid + 1
        else:
            end = mid - 1
    return -1


# Given an array of numbers sorted in ascending order, 
# find the element in the array that has the minimum difference with the given ‘key’.
# Time: O(logN)
def search_min_diff_element(arr, key):
    if key < arr[0]:
        return arr[0]
    n = len(arr)
    if key > arr[n-1]:
        return arr[n-1]
    
    start, end = 0, n - 1
    while start <= end:
        mid = start + (end - start)//2
        if arr[mid] == key:
            return arr[mid]
        elif arr[mid] > key:
            end = mid - 1
        else:
            start = mid + 1
    
    if arr[start] - key < key - arr[end]:
        return arr[start]
    return arr[end]


# Find the maximum value in a given Bitonic array. An array is considered bitonic if it is monotonically increasing and then monotonically decreasing. 
# Monotonically increasing or decreasing means that for any index i in the array arr[i] != arr[i+1].
# Time: O(logN)

def find_max_in_bitonic_array(arr):
    start, end = 0, len(arr) - 1
    while start < end:
        mid = start + (end - start) // 2
        if arr[mid] > arr[mid + 1]:
            end = mid
        else:
            start = mid + 1
    return arr[start]


# Given a Bitonic array, find if a given ‘key’ is present in it. 
# An array is considered bitonic if it is monotonically increasing and then monotonically decreasing. 
# Monotonically increasing or decreasing means that for any index i in the array arr[i] != arr[i+1].
# Write a function to return the index of the ‘key’. If the ‘key’ is not present, return -1.
# Time: O(logN)

def search_bitonic_array(arr, key):
    max_index = find_max_in_bitonic_array(arr)
    key_index = binary_search(arr, key, 0, max_index)
    if key_index != -1:
        return key_index
    return binary_search(arr, key, max_index+1, len(arr)-1)


def find_max_in_bitonic_array(arr):
    start, end = 0, len(arr) - 1
    while start < end:
        mid = start + (end - start) // 2
        if arr[mid] > arr[mid + 1]:
            end = mid
        else:
            start = mid + 1
    return start


def binary_search(arr, key, start, end):
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            start = mid + 1
        else:
            end = mid - 1
    return -1


# Given an array of numbers which is sorted in ascending order and also rotated by some arbitrary number, find if a given ‘key’ is present in it.
# Write a function to return the index of the ‘key’ in the rotated array. If the ‘key’ is not present, return -1. 
# You can assume that the given array does not have any duplicates.
# Time: O(logN)

def search_rotated_array(arr, key):
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = start + (end - start)//2
        if arr[mid] == key:
            return mid
        if arr[start] <= arr[mid]:
            if arr[start] <= key and key < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if key > arr[mid] and key <= arr[end]:
                start = mid + 1
            else:
                end = mid - 1
    return -1


# How do we search in a sorted and rotated array that also has duplicates?
# Time: O(logN)

def search_rotated_with_duplicates(arr, key):
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = start + (end - start)//2
        if arr[mid] == key:
            return mid

        if arr[start] == arr[mid] and arr[end] == arr[mid]:
            start += 1
            end -= 1
        elif arr[start] <= arr[mid]:
            if arr[start] <= key and key < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if key > arr[mid] and key <= arr[end]:
                start = mid + 1
            else:
                end = mid - 1
    return -1

# Given an array of numbers which is sorted in ascending order and is rotated ‘k’ times around a pivot, find ‘k’.
# You can assume that the array does not have any duplicates.
# Time: O(logN)

def count_rotations(arr):
    start, end = 0, len(arr)-1
    while start < end:
        mid = start + (end - start)//2
        if mid < end and arr[mid] > arr[mid+1]:
            return mid + 1
        if mid > start and arr[mid-1] > arr[mid]:
            return mid

        if arr[start] < arr[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return 0

# How do we find the rotation count of a sorted and rotated array that has duplicates too?


def count_rotations_with_duplicates(arr):
    start, end = 0, len(arr) - 1
    while start < end:
        mid = start + (end - start) // 2
        if mid < end and arr[mid] > arr[mid + 1]:
            return mid + 1
        if mid > start and arr[mid - 1] > arr[mid]:
            return mid

        if arr[start] == arr[mid] and arr[end] == arr[mid]:
            if arr[start] > arr[start + 1]:
                return start + 1
            start += 1
            if arr[end - 1] > arr[end]:
                return end
            end -= 1
        elif arr[start] < arr[mid] or (arr[start] == arr[mid] and arr[mid] > arr[end]):
            start = mid + 1
        else:  
            end = mid - 1
    return 0  
