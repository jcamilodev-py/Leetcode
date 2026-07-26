from typing import List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)

        visited = [False] * n

        def dfs(room):
            visited[room] = True
            for i in rooms[room]:
                if not visited[i]:
                    dfs(i)

        dfs(0)

        return all(visited)
            




s = Solution()
print(s.canVisitAllRooms([[6,7,8],[5,4,9],[],[8],[4],[],[1,9,2,3],[7],[6,5],[2,3,1]]))