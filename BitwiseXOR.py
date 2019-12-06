# XOR is a logical bitwise operator that returns 0 (false) if both bits are the same and returns 1 (true) otherwise.

# Given an array of n-1n−1 integers in the range from 11 to nn, find the one number that is missing from the array.

def find_missing_number(arr):
    n = len(arr) + 1
    x1 = 1
    for i in range(2, n+1):
        x1 = x1 ^ i
    x2 = arr[0]
    for i in range(1, n-1):
        x2 = x2 ^ i
    
    return x1 ^ x2


# In a non-empty array of integers, every number appears twice except for one, find that single number.
# Time: O(N)
def find_single_number(arr):
    num = 0
    for i in arr:
        num = num ^ i
    return num


# In a non-empty array of numbers, every number appears exactly twice except two numbers that appear only once. 
# Find the two numbers that appear only once.
# Time: O(N)

def find_single_numbers(nums):
    n1xn2 = 0
    for i in nums:
        n1xn2 = n1xn2 ^ i
    rightmost = 1
    while rightmost & n1xn2 == 0:
        rightmost = rightmost << 1
    num1, num2 = 0, 0
    for num in nums:
        if num & rightmost != 0:
            num1 ^= num
        else:
            num2 ^= num
    return [num1, num2]

# For a given positive number N in base-10, return the complement of its binary representation as a base-10 integer.
# Time: O(b)
def calculate_bitwise_complement(num):
    bit_count, n = 0, num
    while n > 0:
        bit_count += 1
        n = n >> 1
    all_bits_set = pow(2, bit_count) - 1
    return num ^ all_bits_set

# Given a binary matrix representing an image, we want to flip the image horizontally, then invert it.
# To flip an image horizontally means that each row of the image is reversed. 
# For example, flipping [0, 1, 1] horizontally results in [1, 1, 0].
# To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. For example, inverting [1, 1, 0] results in [0, 0, 1].

def flip_and_invert_image(matrix):
    c = len(matrix)
    for row in matrix:
        for i in range((c+1)//2):
            row[i], row[c-i+1] = row[c-i-1] ^ 1, row[i] ^ 1
    return matrix