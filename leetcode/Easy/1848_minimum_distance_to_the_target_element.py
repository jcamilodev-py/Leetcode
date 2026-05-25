from typing import List

class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        ans = []

        for i,j in enumerate(nums):
            if j == target:
                ans.append(abs(i - start))
        
        return min(ans)
        

s = Solution()
print(s.getMinDistance([1], target = 1, start = 0))