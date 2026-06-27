from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        m=float("inf")
        s=0
        n=len(nums)
        for r in range(n):
            s +=nums[r]
            while s>=target:
                m=min(m,r-l+1)
                s-=nums[l]
                l +=1
        return m if m!=float("inf") else 0
        


s = Solution()
print(s.minSubArrayLen(7, [2,3,1,2,4,3]))