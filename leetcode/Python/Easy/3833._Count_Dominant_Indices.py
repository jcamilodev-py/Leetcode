from typing import List

class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        n = len(nums)
        value = n
        s = sum(nums)
        ans = 0

        for i in range(1, n):
            value-=1
            s -=nums[i-1]
            if nums[i-1] > s / value:
                ans+=1
        
        return ans
            



s = Solution()
print(s.dominantIndices([4,1,2]))