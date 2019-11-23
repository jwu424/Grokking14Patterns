# This is a document about the sliding Window. May be used in array and Linked List.

# Question 1
# Given an array, find the average of all contiguous subarrays of size ‘K’ in it.

def find_averages_of_subarrays(K, arr):
    res = []
    window_start, windom_sum = 0, 0
    for window_end in range(len(arr)):
        windom_sum += arr[window_end]

        if window_end >= K - 1:
            res.append(windom_sum / K)
            windom_sum -= arr[window_start]
            window_start += 1
    return res


# Question 2
# Given an array of positive numbers and a positive number ‘k’, find the maximum sum of any contiguous subarray of size ‘k’.

# 1. Brute force
# Time: O(N+K)

# 2. Try to avoid duplicate operations.
# Time: O(N)

# 3. Another version of method 2
# Time: O(N)

def max_sub_array_of_size_k1(k, arr):
    maxx = 0
    for i in range(len(arr)-k+1):
        temp = sum(arr[i:i+k])
        maxx = max(maxx, temp)
    return maxx


def max_sub_array_of_size_k2(k, arr):
    maxx = 0
    for i in range(len(arr)-k+1):
    if i == 0:
        temp = sum(arr[i:i+k])
    else:
        temp = temp - arr[i-1] + arr[i+k-1]
        maxx = max(maxx, temp)
    return maxx


def max_sub_array_of_size_k3(k, arr):
    max_sum = 0
    window_start, windown_sum = 0, 0
    for window_end in range(len(arr)):
        windown_sum += arr[window_end]

        if window_end >= k - 1:
            max_sum = max(max_sum, windown_sum)
            windown_sum -= arr[window_start]
            window_start += 1
    return max_sum

# Given an array of positive numbers and a positive number ‘S’, find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. Return 0, if no such subarray exists.
# 1. Brute force
# Time complexity: O(N^2)

# 2. Better way. 
# Time complexity: O(N)

def smallest_subarray_with_given_sum(s, arr):
    for i in range(1, len(arr)+1):
        for j in range(len(arr)-i+1):
            if sum(arr[j:j+i]) >= s:
                return i
    return 0

def smallest_subarray_with_given_sum(s, arr):
    window_sum = 0
    min_length = math.inf
    window_start = 0

    for window_end in range(len(arr)):
        window_sum += arr[window_end]

        while window_sum >= s:
            min_length = min(min_length, window_end-window_start+1)
            window_sum -= arr[window_start]
            window_start += 1
    if min_length == math.inf:
        return 0
    return min_length


# Given a string, find the length of the longest substring in it with no more than K distinct characters.

# The idea is similar to the last question. Start from beginning, we first try to get a string that len(string)=k. Then we delete from the beginning.
# Time: O(N)

def longest_substring_with_k_distinct(str, k):
    window_start = 0
    max_length = 0
    dictt = {}
    for window_end in range(len(str)):
        dictt[str[window_end]] = dictt.get(str[window_end], 0) + 1

        while len(dictt) > k:
            max_length = max(max_length, window_end-window_start)
            if dictt[str[window_start]] == 1:
                del dictt[str[window_start]]
                window_start += 1
            else:
                dictt[str[window_start]] -= 1
                window_start += 1
    return max_length


# Given an array of characters where each character represents a fruit tree, you are given two baskets and your goal is to put maximum number of fruits in each basket. The only restriction is that each basket can have only one type of fruit.
# You can start with any tree, but once you have started you can’t skip a tree. You will pick one fruit from each tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.
# Write a function to return the maximum number of fruits in both the baskets.

# The idea of this question is same with the above one, but here the target is a little different.
# Time: O(N)

def fruits_into_baskets(fruits):
    window_start = 0
    max_num = 0
    dictt = {}
    for window_end in range(len(fruits)):
        dictt[fruits[window_end]] = dictt.get(fruits[window_end], 0) + 1

        while len(dictt) > 2:
            if dictt[fruits[window_start]] == 1:
                del dictt[fruits[window_start]]
                window_start += 1
            else:
                dictt[fruits[window_start]] -= 1
                window_start += 1
        temp = [v for k, v in dictt.items()]
        max_num = max(max_num, sum(temp)) 
    return max_num

# Given a string, find the length of the longest substring which has no repeating characters.

# 1. Idea is similar. Whenever the count of the key in dictt == 2, we should move window_start.
# Time complexity: O(N)

# 2. Try to record the index of the elem, instead of count.
# Time complexity: O(N)

def longest_substring_with_k_distinct1(str):
    window_start = 0
    max_length = 0
    dictt = {}
    for window_end in range(len(str)):
        dictt[str[window_end]] = dictt.get(str[window_end], 0) + 1

        if dictt[str[window_end]] == 2:
            max_length = max(max_length, sum(dictt.values()) - 1)
            while dictt[str[window_end]] > 1:
                dictt[str[window_start]] -= 1
                window_start += 1
    max_length = max(max_length, sum(dictt.values()))
    return max_length


def longest_substring_with_k_distinct2(str):
    window_start = 0
    max_length = 0
    dictt = {}
    for window_end in range(len(str)):
        right_char = str[window_end]
        if right_char in dictt:
            window_start = max(window_start, dictt[right_char] + 1)
        dictt[str[window_end]] = window_end
        max_length = max(max_length, window_end-window_start+1)
    return max_length


# Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’ letters with any letter, find the length of the longest substring having the same letters after replacement.
# Time complexity: O(N)

def length_of_longest_substring(str, k):
    window_start, max_length, max_repeat = 0, 0, 0
    dictt = {}

    for window_end in range(len(str)):
        dictt[str[window_end]] = dictt.get(str[window_end], 0) + 1
        max_repeat = max(max_repeat, dictt[str[window_end]])

        while (window_end - window_start + 1 - max_repeat) > k:
            dictt[str[window_start]] -= 1
            window_start += 1
        
        max_length = max(max_length, window_end - window_start + 1)
    return max_length


# Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s, find the length of the longest contiguous subarray having all 1s.
# Time complexity: O(N)

def length_of_longest_substring(arr, k):
    window_start, max_length, OneCounts = 0, 0, 0

    for window_end in range(len(arr)):
        if arr[window_end] == 1:
            OneCounts += 1
        
        while (window_end - window_start + 1 - OneCounts) > k:
            if window_start == 1:
                OneCounts -= 1
            window_start += 1
        max_length = max(max_length, window_end - window_start + 1)
    return max_length


# Given a string and a pattern, find out if the string contains any permutation of the pattern.
# Time complexity: O(N)

def find_permutation(str, pattern):
    window_start, matched = 0, 0
    char_frequency = {}

    for chr in pattern:
        char_frequency[chr] = char_frequency.get(chr, 0) + 1

    for window_end in range(len(str)):
        right_char = str[window_end]
        if right_char in char_frequency:
      # decrement the frequency of matched character
            char_frequency[right_char] -= 1
            if char_frequency[right_char] == 0:
                matched += 1

        if matched == len(char_frequency):
            return True

    # shrink the window by one character
        if window_end >= len(pattern) - 1:
            left_char = str[window_start]
            window_start += 1
            if left_char in char_frequency:
                if char_frequency[left_char] == 0:
                    matched -= 1
                char_frequency[left_char] += 1

    return False


# Given a string and a pattern, find all anagrams of the pattern in the given string.
# Time complexity: O(N)

def find_string_anagrams(str, pattern):
    window_start, matched = 0, 0
    char_frequency = {}
    res = []
    for chr in pattern:
        char_frequency[chr] = char_frequency.get(chr, 0) + 1

    for window_end in range(len(str)):
        right_char = str[window_end]
        if right_char in char_frequency:
      # decrement the frequency of matched character
            char_frequency[right_char] -= 1
            if char_frequency[right_char] == 0:
                matched += 1

        if matched == len(char_frequency):
            res.append(window_start)

    # shrink the window by one character
        if window_end >= len(pattern) - 1:
            left_char = str[window_start]
            window_start += 1
            if left_char in char_frequency:
                if char_frequency[left_char] == 0:
                    matched -= 1
                char_frequency[left_char] += 1

    return res


# Given a string and a pattern, find the smallest substring in the given string which has all the characters of the given pattern.
# Time complexity: O(N)

def find_substring(str, pattern):
    window_start, matched = 0, 0
    sub_start = 0
    min_length = len(str) + 1
    char_frequency = {}

    for chr in pattern:
        char_frequency[chr] = char_frequency.get(chr, 0) + 1

    for window_end in range(len(str)):
        right_char = str[window_end]
        if right_char in char_frequency:
      # decrement the frequency of matched character
            char_frequency[right_char] -= 1
            if char_frequency[right_char] >= 0:
                matched += 1

        while matched == len(char_frequency):
            if min_length > window_end - window_start + 1:
                min_length = window_end - window_start + 1
                sub_start = window_start

            left_char = str[window_start]
            window_start += 1
            if left_char in char_frequency:
                if char_frequency[left_char] == 0:
                    matched -= 1
                char_frequency[left_char] += 1

    if min_length > len(str):
        return ''
    return str[sub_start:sub_start+min_length]




def find_word_concatenation(str, words):
    if len(words) == 0 or len(words[0]) == 0:
        return []

    word_frequency = {}

    for word in words:
        word_frequency[word] = word_frequency.get(word, 0) + 1

    result_indices = []
    words_count = len(words)
    word_length = len(words[0])

    for i in range((len(str) - words_count * word_length)+1):
        words_seen = {}
        for j in range(0, words_count):
            next_word_index = i + j * word_length
        # Get the next word from the string
            word = str[next_word_index: next_word_index + word_length]
            if word not in word_frequency:  # Break if we don't need this word
                break

        # Add the word to the 'words_seen' map
            words_seen[word] = words_seen.get(word, 0) + 1

        # No need to process further if the word has higher frequency than required
            if words_seen[word] > word_frequency.get(word, 0):
                break

            if j + 1 == words_count:  # Store index if we have found all the words
                result_indices.append(i)

    return result_indices