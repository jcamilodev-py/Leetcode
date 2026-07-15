from typing import List

class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        n = len(mat)
        m = len(mat[0])
        ans = [[0] * m for _ in range(n)]
        

        for i in range(n):
            for j in range(m):
                if i % 2 == 0:
                    ans[i][(j-k) % m] = mat[i][j] 
                else:
                    ans[i][(j+k) % m] = mat[i][j]
                
            if ans[i] != mat[i]:
                return False

        return True


s = Solution()
print(s.areSimilar(mat = [[1,2,1,2],[5,5,5,5],[6,3,6,3]], k = 2))        