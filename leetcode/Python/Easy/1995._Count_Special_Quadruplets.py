from typing import List

class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        dic = {}
        ans, n = 0, len(nums)

        for i in range(2, n-1):
            for j in range(0, i-1):
                s = nums[j] + nums[i-1]
                dic[s] = dic.get(s, 0) +1
        
            for x in range(i+1, n):
                o = nums[x] - nums[i]
                ans+=dic.get(o, 0)
        
        return ans


s = Solution()
print(s.countQuadruplets([1,1,1,3,5]))