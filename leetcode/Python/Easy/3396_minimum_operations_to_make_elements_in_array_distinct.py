from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        seen = set()
        i = 0
        ans = 0
        while i < len(nums):
            if nums[i] in seen:
                nums = nums[3:]
                ans+=1
                i = 0
                seen = set()
            else:
                seen.add(nums[i])
                i+=1
        return ans



s = Solution()
print(s.minimumOperations([1,2,3,4,5,6,7,8,8]))