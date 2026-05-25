from typing import List

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        ans = float('-inf')
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] < nums[j]:
                    if (nums[j] - nums[i]) > ans:
                        ans = nums[j] - nums[i]

        return -1 if ans == float("-inf") else ans




        
s = Solution()
print(s.maximumDifference([7,1,5,4]))