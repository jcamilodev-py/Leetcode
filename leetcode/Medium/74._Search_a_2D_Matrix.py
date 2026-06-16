from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        i = n // 2
        seen = set()
        while i >= 0 and i < n:
            if i in seen: 
                return False
            seen.add(i)
            
            if matrix[i][0] > target:
                i-=1
            elif matrix[i][0] <= target and matrix[i][-1] >= target:
                for j in matrix[i]:
                        if j == target:
                            return True
                return False
            else:
                i+=1

        return False
            




s = Solution()
print(s.searchMatrix([[1],[3]], target = 2))