from typing import List

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def help(largest):
            s = 1
            current_sum = 0
            for i in nums:
                current_sum+=i
                if current_sum > largest:
                    s+=1
                    current_sum = i
            return s <= k
        
        l, r = max(nums), sum(nums)

        ans = r

        while l <= r:
            m = (l + r) // 2

            if help(m):
                ans = m
                r = m - 1
            else:
                l = m + 1

        return ans




s = Solution()
print(s.splitArray([7,2,5,10,8], k = 2))