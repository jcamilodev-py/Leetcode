from typing import List

class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        i = 2
        ans = 0
        while i < len(nums):
            value = nums[i-1] / 2
            if nums[i-2] + nums [i] == value:
                ans+=1
            i+=1

        return ans



s = Solution()
print(s.countSubarrays([1,2,1,4,1]))