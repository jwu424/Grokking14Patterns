# We are given an array containing ‘n’ objects. Each object, when created, was assigned a unique number from 1 to ‘n’ based on their creation sequence. 
# This means that the object with sequence number ‘3’ was created just before the object with sequence number ‘4’.
# Write a function to sort the objects in-place on their creation sequence number in O(n)O(n) and without any extra space.
# For simplicity, let’s assume we are passed an integer array containing only the sequence numbers, though each number is actually an object.
# Time: O(N). Worst: O(N)+O(N)

def cyclic_sort(nums):
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    return nums


# We are given an array containing ‘n’ distinct numbers taken from the range 0 to ‘n’. Since the array has only ‘n’ numbers out of the total ‘n+1’ numbers, find the missing number.
# Time Complexity: O(N)

def find_missing_number(nums):
    i, n = 0, len(nums)
    while i < n:
        j = nums[i]
        if nums[i] < n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    
    for i in range(n):
        if i != nums[i]:
            return i
    return n


# We are given an unsorted array containing numbers taken from the range 1 to ‘n’. The array can have duplicates, which means some numbers will be missing. Find all those missing numbers.
# Time: O(N)
def find_missing_numbers(nums):
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    res = []
    for i in range(len(nums)):
        if nums[i] != i + 1:
            res.append(i+1)
    return res


# We are given an unsorted array containing ‘n+1’ numbers taken from the range 1 to ‘n’. The array has only one duplicate but it can be repeated multiple times. Find that duplicate number without using any extra space. You are, however, allowed to modify the input array.

def find_duplicate(nums):
    i = 0
    while i < len(nums):
        if nums[i] != i + 1:
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                return nums[i]
        else:
            i += 1
    return -1


# We are given an unsorted array containing ‘n’ numbers taken from the range 1 to ‘n’. The array originally contained all the numbers from 1 to ‘n’, but due to a data error, one of the numbers got duplicated which also resulted in one number going missing. Find both these numbers.
# Time: O(N)
def find_corrupt_numbers(nums):
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    for i in range(len(nums)):
        if nums[i] != i + 1:
            return [nums[i], i + 1]
    return [-1, -1]


# Given an unsorted array containing numbers, find the smallest missing positive number in it.

def find_first_missing_positive(nums):
    i, n = 0, len(nums)
    while i < n:
        j = nums[i] - 1
        if nums[i] > 0 and nums[i] <= n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    return n + 1

# Given an unsorted array containing numbers and a number ‘k’, find the first ‘k’ missing positive numbers in the array.
# Time: O(n+k)
def find_first_k_missing_positive(nums, k):
  missingNumbers = []
  extranum = set()
  i, n = 0, len(nums)
  while i < n:
    j = nums[i] - 1
    if nums[i] > 0 and nums[i] <= n and nums[i] != nums[j]:
      nums[i], nums[j] = nums[j], nums[i]
    else:
      i += 1
  
  for i in range(n):
    if len(missingNumbers) < k:
      if nums[i] != i + 1:
        missingNumbers.append(i+1)
        extranum.add(nums[i])
  i = 1
  while len(missingNumbers) < k:
    cand = i + n
    if cand not in extranum:
      missingNumbers.append(cand)
    i += 1
  return missingNumbers

