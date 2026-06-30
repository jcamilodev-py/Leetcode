from typing import List

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        ans = 0

        n = len(nums)
        p = [0] * (n+1)

        for i in range(1, n+1):
            p[i] = p[i-1] + nums[i-1]
        
        for i in range(1, n):
            current = p[i]
            if current >= p[-1] - p[i]:
                ans+=1
        
        return ans
            


s = Solution()
print(s.waysToSplitArray([2,3,1,0]))