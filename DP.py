# Given two integer arrays to represent weights and profits of ‘N’ items, we need to find a subset of these items which will give us maximum profit such that their cumulative weight is not more than a given number ‘C’. Each item can only be selected once, which means either we put an item in the knapsack or we skip it.

# Brute Force
# Time: O(2^N). Space: O(N)

def solve_knapsack(profits, weights, capacity):
    return knapsack_recursive(profits, weights, capacity, 0)

def knapsack_recursive(profits, weights, capacity, curIndex):
    if capacity <= 0 or curIndex >= len(profits):
        return 0
    profit1 = 0
    if weights[curIndex] <= capacity:
        profit1 = profits[curIndex] + knapsack_recursive(
            profits, weights, capacity - weights[curIndex], curIndex+1)
    profit2 = knapsack_recursive(profits, weights, capacity, curIndex+1)
    return max(profit1, profit2)


# Memoization
# Time: O(N*C). Space: O(N*C)

def solve_knapsack(profits, weights, capacity):
    dp = [[-1 for x in range(capacity+1)] for y in range(len(profits))]
    return knapsack_recursive(profits, weights, capacity, 0)

def knapsack_recursive(profits, weights, capacity, curIndex):
    if capacity <= 0 or curIndex >= len(profits):
        return 0
    if dp[curIndex][capacity] != -1:
        return dp[curIndex][capacity]
    profit1 = 0
    if weights[curIndex] <= capacity:
        profit1 = profits[curIndex] + knapsack_recursive(
            profits, weights, capacity - weights[curIndex], curIndex+1)
    profit2 = knapsack_recursive(profits, weights, capacity, curIndex+1)
    dp[curIndex][capacity] = max(profit1, profit2)
    return dp[curIndex][capacity]


# Bottom-up
# Time: O(N*C). Space: O(N*C)

def solve_knapsack(profits, weights, capacity):
    n = len(profits)
    if capacity <= 0 or n == 0 or len(weights) != n:
        return 0
    dp = [[0 for x in range(capacity+1)] for y in range(n)]

    for i in range(0, n):
        dp[i][0] = 0
    
    for c in range(0, capacity+1):
        if weights[0] <= c:
            dp[0][c] = profits[0]
    for i in range(1, n):
        for c in range(1, capacity+1):
            profit1, profit2 = 0, 0
            if weights[i] <= c:
                profit1 = profits[i] + dp[i-1][c-weights[i]]
            profit2 = dp[i-1][c]
            dp[i][c] = max(profit1, profit2)
    return dp[n-1][capacity]


# Bottome-up 2
# Time: O(N*C). Space: O(2C)

def solve_knapsack(profits, weights, capacity):
    n = len(profits)
    if capacity <= 0 or n == 0 or len(weights) != n:
        return 0
    dp = [[0 for x in range(capacity+1)] for y in range(2)]

    for c in range(0, capacity+1):
        if weights[0] <= c:
            dp[0][c] = dp[1][c] = profits[0]
    
    for i in range(1, n):
        for c in range(0, capacity+1):
            profit1, profit2 = 0, 0
            if weights[i] <= c:
                profit1 = profits[i] + dp[(i-1)%2][c-weights[i]]
            profit2 = dp[(i-1)%2][c]
            dp[i%2][c] = max(profit1, profit2)
    return dp[(n-1)%2][capacity]

# Bottome-up 3
# Time: O(N*C). Space: O(C)

def solve_knapsack(profits, weights, capacity):
    n = len(profits)
    if capacity <= 0 or n == 0 or len(weights) != n:
        return 0
    dp = [0 for x in range(capacity+1)]

    for c in range(0, capacity+1):
        if weights[0] <= c:
            dp[c] = profits[0]
    
    for i in range(1, n):
        for c in range(capacity, -1, -1):
            profit1, profit2 = 0, 0
            if weights[i] <= c:
                profit1 = profits[i] + dp[c-weights[i]]
            profit2 = dp[c]
            dp[i%2][c] = max(profit1, profit2)
    return dp[capacity]


# Given a set of positive numbers, find if we can partition it into two subsets such that the sum of elements in both subsets is equal.

# Top-down
# Time: O(2^N)
def can_partition(num):
    ss = sum(num)
    if ss % 2 != 0:
        return False
    target = ss / 2
    return partition_recursive(num, target, 0, 0)

def partition_recursive(num, target, curIndex, curSum):
    if curSum > target or curIndex >= len(num):
        return False
    if curSum == target:
        return True
    if curSum + curIndex <= target:
        if partition_recursive(num, target, curIndex+1, curSum+num[curIndex]):
            return True
    return partition_recursive(num, target, curIndex+1, curSum)

# Top-down with memoization
# Time: O(N * S). S: total sum of all numbers.
def can_partition(num):
    s = sum(num)
    if s %2 != 0:
        return False
    dp = [[-1 for x in range(int(s/2)+1)] for y in range(len(num))]
    return True if partition_recursive(dp, num, int(s/2), 0) == 1 else False

def partition_recursive(dp, num, sum, curIndex):
    if sum == 0:
        return 1
    n = len(num)
    if n == 0 or curIndex >= n:
        return 0
    if dp[curIndex][sum] == -1:
        if num[curIndex] <= sum:
            if partition_recursive(dp, num, sum-num[curIndex], curIndex+1):
                dp[curIndex][sum] = 1
                return 1
        dp[curIndex][sum] = partition_recursive(dp, num, sum, curIndex+1)
    return dp[curIndex][sum]


# Bottom-up
# Time: O(N * S). S: total sum of all numbers.
def can_partition(num):
    s = sum(num)
    if s %2 != 0:
        return False
    s = int(s/2)
    n = len(num)
    dp = [[False for x in range(s+1)] for y in range(n)]
    for i in range(0, n):
        dp[i][0] = True
    for j in range(1, s+1):
        dp[0][j] = num[0] == j
    for i in range(1, n):
        for j in range(1, s+1):
            if dp[i-1][j]:
                dp[i][j] = dp[i-1][j]
            elif j >= num[i]:
                dp[i][j] = dp[i-1][j-num[i]]
    return dp[n-1][s]


def can_partition2(num):
    totalSum = sum(num)
    if totalSum % 2 != 0:
        return False
    target = totalSum//2
    dp = [[False for x in range(target+1)] for y in range(2)]
    for i in range(2):
        dp[i][0] = True
    for j in range(1, target+1):
        dp[0][j] = num[0] == j
    for i in range(1, len(num)):
        for j in range(1, target+1):
            if dp[(i-1)%2][j]:
                dp[i%2][j] = dp[(i-1)%2][j]
            elif num[i] <= j:
                dp[i%2][j] = dp[(i-1)%2][j-num[i]]
    return dp[(len(num))%2][-1]

# Given a set of positive numbers, determine if a subset exists whose sum is equal to a given number ‘S’.

# Top-down
# Time: O(2^N)
def can_partition(num, target):
    if sum(num) < target:
        return False
    return can_partition_resc(num, target, 0)

def can_partition_resc(num, target, curIndex):
    if target == 0:
        return True
    if len(num) == 0 or curIndex >= len(num):
        return False
    p1 = False
    if num[curIndex] <= target:
        p1 = can_partition_resc(num, target-num[curIndex], curIndex+1)
    p2 = can_partition_resc(num, target, curIndex+1)
    return p1 or p2


# Bottom-up
# Time: O(N * S); Space: O(N * S)
def can_partition(num, target):
    n = len(num)
    dp = [[False for x in range(target+1)] for y in range(n)]
    for i in range(0, n):
        dp[i][0] = True
    for j in range(1, target+1):
        dp[0][j] = num[0] == j
    for i in range(1, n):
        for j in range(1, target+1):
            if dp[i-1][j]:
                dp[i][j] = dp[i-1][j]
            elif j >= num[i]:
                dp[i][j] = dp[i-1][j-num[i]]
    return dp[n-1][target]


# improved Bottom-up
# Time: O(N * S); Space: O(S)
def can_partition(num, target):
    n = len(num)
    dp = [False for x in range(target+1)]
    dp[0] = True
    for j in range(1, target+1):
        dp[j] = num[0] == j
    for i in range(1, n):
        for j in range(target, -1, -1):
            if not dp[j] and j >= num[i]:
                dp[j] = dp[j-num[i]]
    return dp[target]


# Given a set of positive numbers, partition the set into two subsets with minimum difference between their subset sums.

# Top-down
# Time: O(2^N)
def can_partition(num):
    return can_partition_recursive(num, 0, 0, 0)

def can_partition_recursive(num, curIndex, sum1, sum2):
    if curIndex == len(num):
        return abs(sum1-sum2)
    diff1 = can_partition_recursive(num, curIndex+1, sum1+num[curIndex], sum2)
    diff2 = can_partition_recursive(num, curIndex+1, sum1, sum2+num[curIndex])
    return min(diff1, diff2)

# Top-down with memoization
# Time: O(N*S)
def can_partition(num):
    s = sum(num)
    dp = [[-1 for i in range(s+1)] for j in range(len(num))]
    return can_partition_recursive(dp, num, 0, 0, 0)

def can_partition_recursive(dp, num, curIndex, sum1, sum2):
    if curIndex == len(num):
        return abs(sum1-sum2)
    if dp[curIndex][sum1] == -1:
        diff1 = can_partition_recursive(dp, num, curIndex+1, sum1+num[curIndex], sum2)
        diff2 = can_partition_recursive(dp, num, curIndex+1, sum1, sum2+num[curIndex])
        dp[curIndex][sum1] = min(diff1, diff2)
    return dp[curIndex][sum1]

# Bottom-up
# Time: O(N*S)
def can_partition(num):
    s = sum(num)
    n = len(num)
    dp = [[False for x in range(int(s/2)+1)] for y in range(n)]
    for i in range(n):
        dp[i][0] = True
    for j in range(int(s/2)+1):
        dp[0][j] = num[0] == j
    
    for i in range(1, n):
        for j in range(1, int(s/2)+1):
            if dp[i-1][j]:
                dp[i][j] = dp[i-1][j]
            elif j >= num[i]:
                dp[i][j] = dp[i-1][j-num[i]]
    sum1 = 0
    for i in range(int(s/2), -1, -1):
        if dp[n-1][i]:
            sum1 = i
            break
    return abs(s-2*sum1)


# Given a set of positive numbers, find the total number of subsets whose sum is equal to a given number ‘S’.

# Top-down
# Time: O(2^N)
def count_subsets(num, sum):
    return count_subset_recursive(num, sum, 0, 0)

def count_subset_recursive(num, sum, curSum, curIndex):
    if curSum == sum:
        return 1
    n = len(num)
    if n == 0 or curIndex >= n:
        return 0
    temp1 = 0
    if curSum + num[curIndex] <= sum:
        temp1 = count_subset_recursive(num, sum, curSum + num[curIndex], curIndex+1)
    temp2 = count_subset_recursive(num, sum, curSum, curIndex+1)
    return temp1 + temp2

# Top-down with memoization
# Time: O(N*S)
def count_subsets(num, sum):
    dp = [[-1 for x in range(sum+1)] for y in range(len(num))]
    return count_subset_recursive(dp, num, sum, 0)

def count_subset_recursive(dp, num, sum, curIndex):
    if sum == 0:
        return 1
    n = len(num)
    if n == 0 or curIndex >= n:
        return 0
    if dp[curIndex][sum] == -1:
        sum1 = 0
        if num[curIndex] <= sum:
            sum1 = count_subset_recursive(dp, num, sum-num[curIndex], curIndex+1)
        sum2 = count_subset_recursive(dp, num, sum, curIndex+1)
        dp[curIndex][sum] = sum1+sum2
    return dp[curIndex][sum]

# Bottom-down
# Time: O(N*S), Space: O(N*S)
def count_subsets(num, sum):
    n = len(num)
    dp = [[-1 for x in range(sum+1)] for y in range(len(num))]
    for i in range(n):
        dp[i][0] = 1
    for s in range(1, sum+1):
        dp[0][s] = num[0] == s
    for i in range(1, n):
        for s in range(1, sum+1):
            dp[i][s] = dp[i-1][s]
            if s >= num[i]:
                dp[i][s] += dp[i-1][s-num[i]]
    return dp[n-1][sum]

# Time: O(N*S), Space: O(S)
def count_subsets(num, sum):
    n = len(num)
    dp = [0 for x in range(sum+1)]
    dp[0] = 1
    for s in range(1, sum+1):
        dp[s] = num[0] == s
    for i in range(1, n):
        for s in range(sum, -1, -1):
            if s >= num[i]:
                dp[s] += dp[s-num[i]]
    return dp[sum]


# You are given a set of positive numbers and a target sum ‘S’. Each number should be assigned either a ‘+’ or ‘-’ sign. We need to find the total ways to assign symbols to make the sum of the numbers equal to the target ‘S’.

# Brute force
# Time: O(2^N)
def find_target_subsets(num, s):
    if len(num) == 0:
        return 0
    return find_target_subsets_recursive(num, s, 0)

def find_target_subsets_recursive(num, s, curIndex):
    n = len(num)
    if curIndex == n:
        if s == 0:
            return 1
        else:
            return 0
    temp1 = find_target_subsets_recursive(num, s-num[curIndex], curIndex+1)
    temp2 = find_target_subsets_recursive(num, s+num[curIndex], curIndex+1)
    return temp1 + temp2
    

# Bottom-Up
# Time: O(N*S)
def find_target_subsets(num, s):
    totalSum = sum(num)
    if totalSum < s or (s + totalSum) % 2 == 1:
        return 0
    return count_subsets(num, (s+totalSum)//2)

def count_subsets(num, sum):
    n = len(num)
    dp = [[0 for x in range(sum+1)] for y in range(n)]
    for i in range(n):
        dp[i][0] = 1
    for s in range(1, sum+1):
        dp[0][s] = num[0] == s
    for i in range(1, n):
        for s in range(1, sum+1):
            dp[i][s] = dp[i-1][s]
            if s >= num[i]:
                dp[i][s] += dp[i-1][s-num[i]]
    return dp[n-1][s]