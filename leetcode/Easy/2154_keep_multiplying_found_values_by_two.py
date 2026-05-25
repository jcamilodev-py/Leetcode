from typing import List

class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        dic = {}
        for i,j in enumerate(nums):
            dic[j] = i
        
        while original in dic:
            nums[dic[original]] = original*2
            original*=2
        return original
                

s = Solution()
print(s.findFinalValue([2,7,9], original = 4))