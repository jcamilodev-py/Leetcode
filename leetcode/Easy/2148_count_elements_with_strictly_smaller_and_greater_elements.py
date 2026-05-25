from typing import List

class Solution:
    def countElements(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        
        nums.sort()
        for i in range(1, n-1):
            if nums[i] > nums[0] and nums[i] < nums[-1]:
                ans+=1
        return ans

s = Solution()
print(s.countElements([1,2]))