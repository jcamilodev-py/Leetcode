from typing import List
from collections import defaultdict

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:

        dic = defaultdict(int)

        n = len(img1)

        positions_img1 = []

        for i in range(n):
            for j in range(n):
                if img1[i][j] == 1:
                    positions_img1.append((i,j))

        for i in range(n):
            for j in range(n):
                if img2[i][j] == 1:
                    for x,y in positions_img1:
                        dic[(i-x, j-y)]+=1


        return max(dic.values()) if dic else 0



s = Solution()
print(s.largestOverlap([[1,1,0],[0,1,0],[0,1,0]], img2 = [[0,0,0],[0,1,1],[0,0,1]]))