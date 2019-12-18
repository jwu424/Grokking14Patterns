# Given the head of a Singly LinkedList, reverse the LinkedList. Write a function to return the new head of the reversed LinkedList.
# Time: O(N)
def reverse(head):
    if not head or not head.next:
        return head
    prev, cur, next = None, head, None
    while cur:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next
    return prev


# Given the head of a LinkedList and two positions ‘p’ and ‘q’, reverse the LinkedList from position ‘p’ to ‘q’.
# Time: O(N)
def reverse_sub_list(head, p, q):
    if p == q:
        return head
    cur, prev = head, None
    i = 0
    while cur and i < p - 1:
        prev = cur
        cur = cur.next
        i += 1
    last_node_of_first_part = prev
    last_node_of_sub_list = cur
    i = 0
    while cur and i < q - p + 1:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next
        i += 1
    if last_node_of_first_part:
        last_node_of_first_part.next = prev
    else:
        head = prev
    last_node_of_sub_list.next = cur
    return head


# Reverse the first ‘k’ elements of a given LinkedList.

def reverse_first_k(head, k):
    if k == 0:
        return head
    prev, cur, next = None, head, None
    i = 0
    while cur and i < k:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next
        i += 1
    if cur:
        head.next = cur
    return prev

# Given a LinkedList with ‘n’ nodes, reverse it based on its size in the following way:

# If ‘n’ is even, reverse the list in a group of n/2 nodes.
# If n is odd, keep the middle node as it is, reverse the first ‘n/2’ nodes and reverse the last ‘n/2’ nodes.
# https://www.geeksforgeeks.org/reverse-a-linked-list-according-to-its-size/
def reverseBySize2(head):
    n = getSize(head)

    if n % 2 == 0:
        return reverseSizeBy2Unit(head, n//2, False)
    else:
        return reverseSizeBy2Unit(head, n//2, True)

def getSize(head):
    curr = head
    count = 0
    while curr:
        curr = curr.next
        count += 1
    return count

def reverseSizeBy2Unit(head, k, skipmiddle):
    if not head:
        return None
    count = 0
    curr, prev, next = head, None, None

    while curr and count < k:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
        count += 1
    if not skipmiddle:
        if next:
            head.next = reverseSizeBy2Unit(next, k, False)
    else:
        head.next = next
        if next:
            next.next = reverseSizeBy2Unit(next.next, k, True)
    return prev


# Given the head of a LinkedList and a number ‘k’, reverse every ‘k’ sized sub-list starting from the head.
# If, in the end, you are left with a sub-list with less than ‘k’ elements, reverse it too.

def reverse_every_k_elements(head, k):
    if k <= 1 or not head:
        return head
    
    cur, prev = head, None
    while True:
        last_node_of_prev_part = prev
        last_node_of_sublist = cur
        next = None
        i = 0
        while cur and i < k:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
            i += 1
        if last_node_of_prev_part:
            last_node_of_prev_part.next = prev
        else:
            head = prev
        last_node_of_sublist.next = cur
        
        if not cur:
            break
        prev = last_node_of_sublist
    return head


# Given the head of a LinkedList and a number ‘k’, reverse every alternating ‘k’ sized sub-list starting from the head.
# If, in the end, you are left with a sub-list with less than ‘k’ elements, reverse it too.

def reverse_alternate_k_elements(head, k):
    if k <= 1 or not head:
        return head
    
    cur, prev = head, None
    while True:
        last_node_of_prev_part = prev
        last_node_of_sublist = cur
        next = None
        i = 0
        while cur and i < k:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
            i += 1
        if last_node_of_prev_part:
            last_node_of_prev_part.next = prev
        else:
            head = prev
        last_node_of_sublist.next = cur
        prev = last_node_of_sublist
        i = 0
        while cur and i < k:
            cur = cur.next
            prev = prev.next
            i += 1
        if not cur:
            break
        
    return head


# Given the head of a Singly LinkedList and a number ‘k’, rotate the LinkedList to the right by ‘k’ nodes.
# Time: O(N)

def rotate(head, rotations):
    if not head or not head.next or rotations <= 0:
        return head
    cur = head
    count = 1
    while cur.next:
        cur = cur.next
        count += 1
    rotations = rotations % count
    end = cur

    i = 1
    cur = head
    while cur and i < rotations:
        cur = cur.next
        i += 1
    next = cur.next

    end.next = head
    cur.next = None
    head = next
    return head