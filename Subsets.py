# Given a set with distinct elements, find all of its distinct subsets.
# Time: O(2^N)
def find_subsets(nums):
    subset = [[]]
    for elem in nums:
        n = len(subset)
        for i in range(n):
            set = list(subset[i])
            set.append(elem)
            subset.append(set)
    return subset


# Given a set of numbers that might contain duplicates, find all of its distinct subsets.
# Time: O(2^N)
def find_subsets(nums):
    nums.sort()
    subset = [[]]
    startIndex, endIndex = 0, 0
    for i in range(len(nums)):
        startIndex = 0
        if i > 0 and nums[i] == nums[i-1]:
            startIndex = endIndex + 1
        endIndex = len(subset) - 1
        for j in range(startIndex, endIndex+1):
            set = list(subset[j])
            set.append(nums[i])
            subset.append(set)
    return subset

# Given a set of distinct numbers, find all of its permutations.
# Time: O(N*N!)
def find_permutations(nums):
    res = []
    generate_per(nums, 0, [], res)
    return res

def generate_per(nums, index, curPer, res):
    if index == len(nums):
        res.append(curPer)
    else:
        for i in range(len(curPer)+1):
            newPer = list(curPer)
            newPer.insert(i, nums[index])
            generate_per(nums, index+1, newPer, res)


from collections import deque
def find_permutations(nums):
    numsLength = len(nums)
    res = []
    permutations = deque()
    permutations.append([])
    for curNum in nums:
        n = len(permutations)
        for _ in range(n):
            oldPerm = permutations.popleft()
            for j in range(len(oldPerm)+1):
                newPer = list(oldPerm)
                newPer.insert(j, curNum)
                if len(newPer) == numsLength:
                    res.append(newPer)
                else:
                    permutations.append(newPer)
    return res

# Given a string, find all of its permutations preserving the character sequence but changing case.
# O(N*2^N)
def find_letter_case_string_permutations(str):
    permutation = [str]
    for i in range(len(str)):
        if str[i].isalpha():
            n = len(permutation)
            for j in range(n):
                chs = list(permutation[j])
                chs[i] = chs[i].swapcase()
                permutation.append(''.join(chs))
    return permutation

# For a given number ‘N’, write a function to generate all combination of ‘N’ pairs of balanced parentheses.
# Time: O(N*2^N)
def generate_valid_parentheses(num):
    res = []
    parenthesesString = [0 for x in range(2*num)]
    generate_valid(num, 0, 0, parenthesesString, 0, res)
    return res

def generate_valid(num, openCount, closeCount, parenthesesString, index, res):
    if openCount == num and closeCount == nums:
        res.append(''.join(parenthesesString))
    else:
        if openCount < num:
            parenthesesString[index] = '('
            generate_valid(num, openCount+1, closeCount, parenthesesString, index+1, res)
        
        if openCount > closeCount:
            parenthesesString[index] = ')'
            generate_valid(num, openCount, closeCount+1, parenthesesString, index+1, res)
