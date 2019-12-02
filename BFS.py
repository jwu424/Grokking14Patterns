# Given a binary tree, populate an array to represent its level-by-level traversal. You should populate the values of all nodes of each level from left to right in separate sub-arrays.
# Time: O(N)
from collections import deque
def traverse(root):
    res = []
    if not root:
        return res
    queue = deque()
    queue.append(root)
    while queue:
        levelSize = len(queue)
        curlevel = []
        for _ in range(levelSize):
            curNode = queue.popleft()
            curlevel.append(curNode.val)
            if curNode.left:
                queue.append(curNode.left)
            if curNode.right:
                queue.append(curNode.right)
        res.append(curlevel)
    return res
    
# Given a binary tree, populate an array to represent its level-by-level traversal in reverse order, i.e., the lowest level comes first. You should populate the values of all nodes in each level from left to right in separate sub-arrays.
# Time: O(N)
def traverse(root):
    res = deque()
    if not root:
        return res
    queue = deque()
    queue.append(root)
    while queue:
        levelsize = len(queue)
        curlevel = []
        for _ in range(levelsize):
            curnode = queue.popleft()
            curlevel.append(curnode.val)
            if curnode.left:
                queue.append(curnode.left)
            if curnode.right:
                queue.append(curnode.right)
        res.append(curlevel)
    return res

# Given a binary tree, populate an array to represent its zigzag level order traversal. You should populate the values of all nodes of the first level from left to right, then right to left for the next level and keep alternating in the same manner for the following levels.
# Time: O(N)
def traverse(root):
    res = deque()
    if not root:
        return res
    queue = deque()
    queue.append(root)
    leftToright = True
    while queue:
        levelsize = len(queue)
        curlevel = deque()
        for _ in range(levelsize):
            curnode = queue.popleft()
            if leftToright:
                curlevel.append(curnode.val)
            else:
                curlevel.appendleft(curnode.val)
            if curnode.left:
                queue.append(curnode.left)
            if curnode.right:
                queue.append(curnode.right)
        leftToright = not leftToright
        res.append(list(curlevel))
    return res


# Given a binary tree, populate an array to represent the averages of all of its levels.
# Time: O(N)
def find_level_averages(root):
    res = []
    if not root:
        return res
    queue = deque()
    queue.append(root)
    while queue:
        levelSize = len(queue)
        levelSum = 0
        for _ in range(levelSize):
            curNode = queue.popleft()
            levelSum += curNode.val
            if curNode.left:
                queue.append(curNode.left)
            if curNode.right:
                queue.append(curNode.right)
        res.append(levelSum / levelSize)
    return res

# Find the minimum depth of a binary tree. The minimum depth is the number of nodes along the shortest path from the root node to the nearest leaf node.
# Time: O(N)
def find_minimum_depth(root):
    if not root:
        return 0
    res = 1
    queue = deque()
    queue.append(root)
    while queue:
        levelsize = len(queue)
        for _ in range(levelsize):
            curNode = queue.popleft()
            if not curNode.left and not curNode.right:
                return res
            if curNode.left:
                queue.append(curNode.left)
            if curNode.right:
                queue.append(curNode.right)
        res += 1
    
# Given a binary tree, find its maximum depth (or height).
# Time: O(N)
def find_maximum_depth(root):
    if not root:
        return 0
    res = 0
    queue = deque()
    queue.append(root)
    while queue:
        levelSize = len(queue)
        res += 1
        for _ in range(levelSize):
            curNode = queue.popleft()
            if curNode.left:
                queue.append(curNode.left)
            if curNode.right:
                queue.append(curNode.right)
    return res

# Given a binary tree and a node, find the level order successor of the given node in the tree. The level order successor is the node that appears right after the given node in the level order traversal.
# Time: O(N)
def find_successor(root, key):
    if not root:
        return None
    queue = deque()
    queue.append(root)
    while queue:
        curNode = queue.popleft()
        if curNode.left:
            queue.append(curNode.left)
        if curNode.right:
            queue.append(curNode.right)
        
        if curNode.val == key:
            break
    return queue[0] if queue else None


# Given a binary tree, connect each node with its level order successor. The last node of each level should point to a null node.
# Time: O(N)
def connect_level_order_siblings(root):
    if not root:
        return 
    queue = deque()
    queue.append(root)
    while queue:
        preNode = None
        levelsize = len(queue)
        for _ in range(levelsize):
            curNode = queue.popleft()
            if preNode:
                preNode.next = curNode
            preNode = curNode

            if curNode.left:
                queue.append(curNode.left)
            if curNode.right:
                queue.append(curNode.right)


# Given a binary tree, connect each node with its level order successor. The last node of each level should point to the first node of the next level.
# Time: O(N)
def connect_all_siblings(root):
    if not root:
        return 
    queue = deque()
    queue.append(root)
    preNode, curNode = None, None
    while queue:
        curNode = queue.popleft()
        if preNode:
            preNode.next = curNode
        preNode = curNode

        if curNode.left:
            queue.append(curNode.left)
        if curNode.right:
            queue.append(curNode.right)


# Given a binary tree, return an array containing nodes in its right view. The right view of a binary tree is the set of nodes visible when the tree is seen from the right side.
# Time: O(N)
def tree_right_view(root):
    if not root:
        return []
    res = []
    queue = deque()
    queue.append(root)
    while queue:
        levelSize = len(queue)
        for _ in range(levelSize):
            curNode = queue.popleft()
            if curNode.left:
                queue.append(curNode.left)
            if curNode.right:
                queue.append(curNode.right)
        res.append(curNode)
    return res


# Given a binary tree, return an array containing all the boundary nodes of the tree in an anti-clockwise direction.
# The boundary of a tree contains all nodes in the left view, all leaves, and all nodes in the right view. Please note that there should not be any duplicate nodes. For example, the root is only included in the left view; similarly, if a level has only one node we should include it in the left view.
def find_tree_boundary(root):
    if not root:
        return []
    res = []
    queue = deque()
    queue.append(root)
    leftView, rightView = [], deque()
    while queue:
        levelSize = len(queue)
        for i in range(levelSize):
            curNode = queue.popleft()
            if not curNode.left and not curNode.right:
                continue
            elif i == 0:
                leftView.append(curNode)
            elif i == levelSize - 1:
                rightView.appendleft(curNode)

            if curNode.left:
                queue.append(curNode.left)
            if curNode.right:
                queue.append(curNode.right)
    return leftView + find_leaves_dfs(root) + list(rightView)

def find_leaves_dfs(root):
    leaves = []
    queue = deque()
    queue.append(root)
    while queue:
        curNode = queue.pop()
        if not curNode.left and not curNode.right:
            leaves.append(curNode)
        if curNode.right:
            queue.append(curNode.right)
        if curNode.left:
            queue.append(curNode.left)
    return leaves