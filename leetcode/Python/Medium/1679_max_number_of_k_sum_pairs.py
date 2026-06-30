from typing import List

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)-1
        i,j = 0,n
        nums = sorted(nums)
        ans = 0

        while i < j:
            if nums[i] + nums[j] > k:
                j-=1
            elif nums[i] + nums[j] < k:
                i+=1
            else:
                ans+=1
                i+=1
                j-=1
        return ans


s = Solution()
print(s.maxOperations([1,2,3,4], k = 5))