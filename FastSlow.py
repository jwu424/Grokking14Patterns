# Given the head of a Singly LinkedList, write a function to determine if the LinkedList has a cycle in it or not.
# Time: O(N)
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def has_cycle(head):
    slow, fast = head, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True
    return False

# Given the head of a LinkedList with a cycle, find the length of the cycle.
# Time: O(N)
def has_cycle(head):
    slow, fast = head, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return cyc_length(slow)
    return 0

def cyc_length(slow):
    temp = slow
    count = 0
    while True:
        slow = slow.next
        count += 1
        if slow == temp:
            break
    return count

# Given the head of a Singly LinkedList that contains a cycle, write a function to find the starting node of the cycle.
# Time: O(N)

def find_cycle_start(head):
    slow, fast = head, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            count = cyc_length(slow)
            break
    return find_start(head, count)

def cyc_length(slow):
    temp = slow
    count = 0
    while True:
        slow = slow.next
        count += 1
        if slow == temp:
            break
    return count

def find_start(head, count):
    p1, p2 = head, head
    while count > 0:
        p2 = p2.next
        count -= 1
    while p1 != p2:
        p1 = p1.next
        p2 = p2.next
    return p1


# Any number will be called a happy number if, after repeatedly replacing it with a number equal to the sum of the square of all of its digits, leads us to number ‘1’. All other (not-happy) numbers will never reach ‘1’. Instead, they will be stuck in a cycle of numbers which does not include ‘1’.

def find_happy_number1(num):
    res = {}
    while num != 1:
        temp = str(num)
        num = sum([int(x) * int(x) for x in temp])
        if num not in res:
            res[num] = 1
        else:
            return False
    return True


def find_happy_number2(num):
    slow, fast = num, num
    while True:
        slow = find_next(slow)
        fast = find_next(find_next(fast))
        if slow == fast:
            break
    return slow == 1

def find_next(num):
    return sum([int(x) * int(x) for x in str(num)])


# Given the head of a Singly LinkedList, write a method to return the middle node of the LinkedList.
# If the total number of nodes in the LinkedList is even, return the second middle node.
# O(N)
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def find_middle_of_linked_list(head):
    slow, fast = head, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow


# Given the head of a Singly LinkedList, write a method to check if the LinkedList is a palindrome or not.

# Your algorithm should use constant space and the input LinkedList should be in the original form once the algorithm is finished.
# The algorithm should have O(N) time complexity where ‘N’ is the number of nodes in the LinkedList.

def is_palindromic_linked_list(head):
    if not head or not head.next:
        return True
    slow, fast = head, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    
    head_second_half = reverse(slow)
    copy = head_second_half

    while head and head_second_half:
        if head.value != head_second_half.value:
            break

        head = head.next
        head_second_half = head_second_half.next
    reverse(copy)

    if not head_second_half:
        return True
    return False

def reverse(head):
    prev = None
    while head:
        next = head.next
        head.next = prev
        prev = head
        head = next
    return prev


# Given the head of a Singly LinkedList, write a method to modify the LinkedList
# such that the nodes from the second half of the LinkedList are inserted alternately
# to the nodes from the first half in reverse order.
# So if the LinkedList has nodes 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null, your method should return 1 -> 6 -> 2 -> 5 -> 3 -> 4 -> null.
# Time: O(N)

def reorder(head):
    if not head or not head.next:
      return 
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    head_second = reverse(slow)

    head_first = head
    while head_first and head_second:
        head_first_next = head_first.next
        head_first.next = head_second
        head_first = head_first_next

        head_second_next = head_second.next
        head_second.next = head_first_next
        head_second = head_second_next
    if head_first:
      head_first.next = None
    return 

def reverse(head):
    prev = None
    while head:
        next = head.next
        head.next = prev
        prev = head
        head = next
    return prev


# We are given an array containing positive and negative numbers. Suppose the array contains a number ‘M’ at a particular index. Now, if ‘M’ is positive we will move forward ‘M’ indices and if ‘M’ is negative move backwards ‘M’ indices. You should assume that the array is circular which means two things:

# If, while moving forward, we reach the end of the array, we will jump to the first element to continue the movement.
# If, while moving backward, we reach the beginning of the array, we will jump to the last element to continue the movement.
# Write a method to determine if the array has a cycle. The cycle should have more than one element and should follow one direction which means the cycle should not contain both forward and backward movements.

def circular_array_loop_exists(arr):
    for i in range(len(arr)):
        is_forward = arr[i] >= 0
        slow, fast = i, i

        while True:
            slow = find_next(arr, is_forward, slow)
            fast = find_next(arr, is_forward, fast)

            if fast != -1:
                fast = find_next(arr, is_forward, fast)
            if fast == -1 or slow == -1 or slow == fast:
                break
        
        if slow != -1 and slow == fast:
            return True
    return False

def find_next(arr, is_forward, current):
    direction = arr[current] >= 0
    if is_forward != direction:
        return -1
    next_index = (current + arr[current]) % len(arr)

    if next_index == current:
        next_index = -1
    return next_index