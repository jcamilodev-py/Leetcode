from typing import List

class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        seen = set()
        for i in range(1, len(nums)):
            if nums[i] + nums[i-1] in seen:
                return True
            seen.add(nums[i] + nums[i-1])
        
        return False


s = Solution()
print(s.findSubarrays([99,24,64,34,45,53,98,57,7,72,13,8,61,52,34,99,93,43,71,18,44,30,12,75,64,97,46,1,87,17,16,91,69,47,18,7,21,33,94,52]))
