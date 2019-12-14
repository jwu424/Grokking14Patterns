# Topological Sort of a directed graph (a graph with unidirectional edges) is a linear ordering of its vertices such that for every directed edge (U, V) from vertex U to vertex V, U comes before V in the ordering.
# Given a directed graph, find the topological ordering of its vertices.

# Time: O(V+E), where ‘V’ is the total number of vertices and ‘E’ is the total number of edges in the graph.

from collections import deque
def topological_sort(vertices, edges):
    sortOrder = []
    if vertices <= 0:
        return sortOrder
    inDegree = {i: 0 for i in range(vertices)}
    graph = {i: [] for i in range(vertices)}

    for edge in edges:
        parent, child = edge[0], edge[1]
        graph[parent].append(child)
        inDegree[child] += 1
    
    sources = deque()
    for key in inDegree:
        if inDegree[key] == 0:
            sources.append(key)

    while sources:
        vertex = sources.popleft()
        sortOrder.append(vertex)
        for child in graph[vertex]:
            inDegree[child] -= 1
            if inDegree[child] == 0:
                sources.append(child)
    
    if len(sortOrder) != vertices:
        return []
    return sortOrder

# There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’. Each task can have some prerequisite tasks which need to be completed before it can be scheduled. Given the number of tasks and a list of prerequisite pairs, find out if it is possible to schedule all the tasks.
# Time: O(V+E)

def is_scheduling_possible(tasks, prerequisites):
    sortOrder = []
    if tasks <= 0:
        return False
    
    inDegree = {i: 0 for i in range(tasks)}
    graph = {i: [] for i in range(tasks)}

    for pre in prerequisites:
        parent, child = pre[0], pre[1]
        graph[parent].append(child)
        inDegree[child] += 1
    
    sources = deque()
    for key in inDegree:
        if inDegree[key] == 0:
            sources.append(key)
    
    while sources:
        task = sources.popleft()
        sortOrder.append(task)
        for child in graph[task]:
            inDegree[child] -= 1
            if inDegree[child] == 0:
                sources.append(child)
    
    return len(sortOrder) == tasks


# There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’. Each task can have some prerequisite tasks which need to be completed before it can be scheduled. 
# Given the number of tasks and a list of prerequisite pairs, write a method to find the ordering of tasks we should pick to finish all tasks.
# Time: O(V+E)

def find_order(tasks, prerequisites):
    sortOrder = []
    if tasks <= 0:
        return sortOrder
    inDegree = {i: 0 for i in range(tasks)}
    graph = {i: [] for i in range(tasks)}

    for pre in prerequisites:
        parent, child = pre[0], pre[1]
        inDegree[child] += 1
        graph[parent].append(child)
    
    source = deque()
    for key in graph:
        if inDegree[key] == 0:
            source.append(key)
    
    while source:
        task = source.popleft()
        sortOrder.append(task)
        for child in graph[task]:
            inDegree[child] -= 1
            if inDegree[child] == 0:
                source.append(child)
    
    if len(sortOrder) != tasks:
        return []
    return sortOrder

# There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’. Each task can have some prerequisite tasks which need to be completed before it can be scheduled. 
# Given the number of tasks and a list of prerequisite pairs, write a method to print all possible ordering of tasks meeting all prerequisites.
# Time: O(V!*E)

def print_orders(tasks, prerequisites):
    sortedOrder = []
    if tasks <= 0:
        return False
    inDegree = {i: 0 for i in range(tasks)}
    graph = {i: [] for i in range(tasks)}

    for pre in prerequisites:
        parent, child = pre[0], pre[1]
        inDegree[child] += 1
        graph[parent].append(child)
    
    sources = deque()
    for key in graph:
        if inDegree[key] == 0:
            sources.append(key)
    print_all_topological_sorts(graph, inDegree, sources, sortedOrder)

def print_all_topological_sorts(graph, inDegree, sources, sortedOrder):
    if sources:
        for vertex in sources:
            sortedOrder.append(vertex)
            sourcesForNextCall = deque(sources)
            sourcesForNextCall.remove(vertex)
            for child in graph[vertex]:
                inDegree[child] -= 1
                if inDegree[child] == 0:
                    sourcesForNextCall.append(child)
            print_all_topological_sorts(graph, inDegree, sourcesForNextCall, sortedOrder)
            sortedOrder.remove(vertex)
            for child in graph[vertex]:
                inDegree[child] += 1
    if len(sortedOrder) == len(inDegree):
        print(sortedOrder)


# There is a dictionary containing words from an alien language for which we don’t know the ordering of the characters. 
# Write a method to find the correct order of characters in the alien language.
# Time: O(V+N)

def find_order(words):
    if len(words) == 0:
        return ''
    
    inDegree = {}
    graph = {}
    for word in words:
        for char in word:
            graph[char] = []
            inDegree[char] = 0
    
    for i in range(0, len(words)-1):
        w1, w2 = words[i], words[i+1]
        for j in range(0, min(len(w1), len(w2))):
            parent, child = w1[j], w2[j]
            if parent != child:
                graph[parent].append(child)
                inDegree[child] += 1
                break
    sources = deque()
    for key in inDegree:
        if inDegree[key] == 0:
            sources.append(key)
    sortedOrder = []
    while sources:
        vertex = sources.popleft()
        sortedOrder.append(vertex)
        for child in graph[vertex]:
            inDegree[child] -= 1
            if inDegree[child] == 0:
                sources.append(child)
    if len(sortedOrder) != len(inDegree):
        return ""
    return ''.join(sortedOrder)


# Given a sequence originalSeq and an array of sequences, write a method to find if originalSeq can be uniquely reconstructed from the array of sequences.
# Unique reconstruction means that we need to find if originalSeq is the only sequence such that all sequences in the array are subsequences of it.
