from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
            
        p = [0] * (n + 1)

        for i in range(1, n+1):
            p[i] = p[i - 1] + nums[i - 1]
        
        dic = {0:1}
        
        ans, prefix = 0, 0
        for i in range(n):
            prefix+=nums[i]
            if prefix - k in dic:
                ans+=dic[prefix-k]

            if prefix in dic:
                dic[prefix] +=1
            else:
                dic[prefix] = 1

        return ans

s = Solution()
print(s.subarraySum([1,1,1], k = 2))