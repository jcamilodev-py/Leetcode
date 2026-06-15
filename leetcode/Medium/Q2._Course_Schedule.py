from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}

        for i in prerequisites:
            a, b = i

            graph[a].append(b)

        visited = set()
        memo = set()
        def dfs(current, visited, memo):
            if current in memo:
                return
            visited.add(current)
            for i in graph[current]:
                if i in visited:
                    return False
                else:
                    if dfs(i, visited, memo) == False:
                        return False
            memo.add(current)

            visited.remove(current)
        
        for i in graph:
            if dfs(i, visited, memo) == False:
                return False
        return True


s = Solution()
print(s.canFinish(numCourses = 2, prerequisites = [[1,0]]))