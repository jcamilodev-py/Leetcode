from typing import List

class Solution: 
    def longestOnes(self, nums: List[int], k: int) -> int:
        ans = 0
        zeros = 0
        left = 0
        for i, rigth in enumerate(nums):
            if rigth == 0:
                zeros+=1

            while zeros > k:
                if nums[left] == 0:
                    left+=1
                    zeros-=1
                else:
                    left+=1
            ans = max(ans, i - left +1)
        return ans



s = Solution()
print(s.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))