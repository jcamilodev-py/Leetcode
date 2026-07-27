from typing import List
import heapq

class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        MOD = 10 ** 9 + 7
        ans = 1
        heapq.heapify(nums)
        while k > 0:
            heapq.heapreplace(nums, nums[0]+1)
            k-=1

        for i in nums:
            ans*=i
            ans%=MOD
        return ans




s = Solution()
print(s.maximumProduct([0,4], 5))