from typing import List

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        dic = {}
        rows = len(wall)
        
        for i in range(rows):
            current = 0
            for j in range(len(wall[i])-1):
                if wall[i][j] + current not in dic:
                    dic[wall[i][j] + current] = 1
                    current = wall[i][j] + current

                else:
                    dic[wall[i][j] + current] +=1
                    current = wall[i][j] + current

        return rows - max(dic.values()) if dic else rows
            

                



s = Solution()
print(s.leastBricks([[1],[1],[1]]))