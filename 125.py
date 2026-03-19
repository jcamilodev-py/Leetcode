from typing import List


class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        output = [0,0] 
        count = 0
        for i in range(len(mat)):
            for j in (mat[i]):
                if j == 1:
                    count+=1

            if count > output[1]:

                output[0] = i
                output[1] = count
            
            count = 0
        return output


s = Solution()
print(s.rowAndMaximumOnes([[0,0,0],[0,1,1]]))
