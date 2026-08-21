from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        if target < matrix[0][0]:
            return False

        m = len(matrix[0])

        i = 0
        j = m-1

        while j != -1:
            if matrix[i][j] > target:
                j-=1
            elif matrix[i][j] < target:
                for l in matrix:
                    if l[j] == target:
                        return True
                j-=1
            else:
                return True
        return False
        

s = Solution()
print(s.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20))