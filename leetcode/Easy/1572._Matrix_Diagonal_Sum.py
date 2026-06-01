from typing import List

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        if n == 1:
            return mat[0][0]
        
        ans, j = 0, 0
        x = n-1
        
    
        for i in range(n):
                if j == x:
                     ans+=mat[i][j]
                     j+=1
                     x-=1
                else:
                    ans+=mat[i][j] + mat[i][x]
                    j+=1
                    x-=1
        return ans



s = Solution()
print(s.diagonalSum([[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]]))