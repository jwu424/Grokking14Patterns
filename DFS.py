# Given a binary tree and a number ‘S’, find if the tree has a path from root-to-leaf such that the sum of all the node values of that path equals ‘S’.
# Time: O(N)

def has_path(root, sum):
    if not root:
        return False
    if root.val == sum and not root.left and not root.right:
        return True
    return has_path(root.leaf, sum - root.val) or has_path(root.right, sum - root.val)

# Given a binary tree and a number ‘S’, find all paths from root-to-leaf such that the sum of all the node values of each path equals ‘S’.
# Time: O(N^2). Since del list[-1] is O(N) and we also need to traverse all nodes.
# Space: For a balanced tree, the leaf nodes is N/2, depth is log(N) ==> Total paths list space will be O(NlogN) ==> tigher time complexity: O(NlogN)

def find_paths(root, sum):
    res = []
    find_path_recursive(root, sum, [], res)
    return res

def find_path_recursive(curNode, sum, curPath, res):
    if not curNode:
        return 
    curPath.append(curNode.val)
    if curNode.val == sum and not curNode.left and not curNode.right:
        res.append(list(curPath))
    else:
        find_path_recursive(curNode.left, sum-curNode.val, curPath, res)
        find_path_recursive(curNode.right, sum-curNode.val, curPath, res)
    del curPath[-1]


def find_paths(root, sum):
    allPaths = []
    find_paths_recursive(root, sum, [], allPaths)
    return allPaths


def find_paths_recursive(currentNode, sum, currentPath, allPaths):
    if currentNode is None:
        return
    if currentNode.val == sum and currentNode.left is None and currentNode.right is None:
        allPaths.append(list(currentPath+[currentNode.val]))
    else:
        find_paths_recursive(currentNode.left, sum -
                            currentNode.val, currentPath+[currentNode.val], allPaths)
        find_paths_recursive(currentNode.right, sum -
                            currentNode.val, currentPath+[currentNode.val], allPaths)



# Given a binary tree, find the root-to-leaf path with the maximum sum.
# Time: O(N)
def find_paths_max(root):
    if not root:
        return 
    max_sum_left = 0 if not root.left else find_paths_max(root.left)
    max_sum_right = 0 if not root.right else find_paths_max(root.right)
    return max_sum_left + root.val if max_sum_left > max_sum_right else max_sum_right + root.val


# Given a binary tree where each node can only have a digit (0-9) value, each root-to-leaf path will represent a number. Find the total sum of all the numbers represented by all paths.
# Time: O(N)

def find_sum_of_path_numbers(root):
    return find_root_to_leaf_path_nums(root, 0)

def find_root_to_leaf_path_nums(curNode, pathSum):
    if not curNode:
        return 0
    pathSum = 10 * pathSum + curNode.val

    if not curNode.left and not curNode.right:
        return pathSum
    return find_root_to_leaf_path_nums(curNode.left, pathSum) + find_root_to_leaf_path_nums(curNode.right, pathSum)

# Given a binary tree and a number sequence, find if the sequence is present as a root-to-leaf path in the given tree.
# Time: O(N)
def find_path(root, sequence):
    if not root:
        return len(sequence) == 0
    return find_path_same(root, sequence, 0)

def find_path_same(curNode, sequence, sequenceIndex):
    if not curNode:
        return False
    seqLen = len(sequence)

    if sequenceIndex >= seqLen or curNode.val != sequence[sequenceIndex]:
        return False
    if not curNode.left and not curNode.right and sequenceIndex == seqLen - 1:
        return True
    return find_path_same(curNode.left, sequence, sequenceIndex + 1) or \
           find_path_same(curNode.right, sequence, sequenceIndex + 1)


# Given a binary tree and a number ‘S’, find all paths in the tree such that the sum of all the node values of each path equals ‘S’. 
# Please note that the paths can start or end at any node but all paths must follow direction from parent to child (top to bottom).
# Time: worst: O(N^2), balance tree: O(NlogN)
def count_paths(root, S):
    return count_paths_recursive(root, S, [])

def count_paths_recursive(curNode, S, curPath):
    if not curNode:
        return 0
    
    curPath.append(curNode.val)
    pathCount, pathSum = 0, 0
    for i in range(len(curPath)-1, -1, -1):
        pathSum += curPath[i]
        if pathSum == S:
            pathCount += 1
    pathCount += count_paths_recursive(curNode.left, S, curPath)
    pathCount += count_paths_recursive(curNode.right, S, curPath)

    del curPath[-1]
    return pathCount

# Given a binary tree, find the length of its diameter.
# The diameter of a tree is the number of nodes on the longest path between any two leaf nodes. 
# The diameter of a tree may or may not pass through the root.
# Time: O(N)
class TreeDiameter():
    def __init__(self):
        self.treeDiameter = 0
    
    def find_diameter(self, root):
        self.calculate_height(root)
        return self.treeDiameter
    
    def calculate_height(self, curNode):
        if not curNode:
            return 0
        leftTreeHeight = self.calculate_height(curNode.left)
        rightTreeHeight = sefl.calculate_height(curNode.right)

        diameter = leftTreeHeight + rightTreeHeight + 1
        self.treeDiameter = max(diameter, sefl.treeDiameter)

        return max(leftTreeHeight, rightTreeHeight) + 1

# Find the path with the maximum sum in a given binary tree. Write a function that returns the maximum sum. 
# A path can be defined as a sequence of nodes between any two nodes and doesn’t necessarily pass through the root.
# O(N)
class MaxPath():
    
    def find_diameter(self, root):
        self.globalMax = -math.inf
        self.findMaxPath(root)
        return self.globalMax
    
    def findMaxPath(self, curNode):
        if not curNode:
            return 0
        leftMax = self.findMaxPath(curNode.left)
        rightMax = sefl.findMaxPath(curNode.right)

        leftMax = max(leftMax, 0)
        rightMax = max(rightMax, 0)
        locMax = leftMax + rightMax + curNode.val
        self.globalMax = max(locMax, sefl.globalMax)

        return max(leftMax, rightMax) + curNode.val