from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = max(nums)

        cur_min, cur_max = 1, 1

        for i in nums:
            if i == 0:
                cur_min, cur_max = 1, 1
                continue
            tmp = cur_max * i
            cur_max = max(i * cur_max, i * cur_min, i)
            cur_min = min(tmp, i * cur_min, i)

            ans = max(ans, cur_max)

        return ans

                

s = Solution()
print(s.maxProduct([1,0,-1,2,3,-5,-2]))