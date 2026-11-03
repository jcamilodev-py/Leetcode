class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        graph = {i: [] for i in range(numCourses)}
        ans = []

        values = [0] * numCourses

        for i in prerequisites:
            a, b = i

            graph[a].append(b)


        def dfs(i):
            if values[i] == 1:
                return False
            if values[i] == 2:
                return True

            values[i] = 1

            for j in graph[i]:
                if not dfs(j):
                    return False
            values[i] = 2
            ans.append(i)
            return True

        for j in range(numCourses):
            if not dfs(j):
                return []

        return ans
            






s = Solution()
print(s.findOrder(numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]))