from typing import List
from collections import deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Find circle if exists, false else true
        # 1. build graph of courses and save all that have none
        # 2. from all courses start dfs if any course in encountered again
        #    in the same dfs then we have a cirular dep. return false
        # else if the get through all nodes return true
        in_degree = [0] * numCourses
        graph: List[List[int]] = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            graph[b].append(a)
            in_degree[a] += 1

        queue: deque[int] = deque()

        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)

        visited = 0
        order: List[int] = []
        while len(queue) > 0:
            curr = queue.pop()
            order.append(curr)
            visited += 1
            for dep in graph[curr]:
                in_degree[dep] -= 1
                if in_degree[dep] == 0:
                    queue.appendleft(dep)

        return order if visited == numCourses else []
