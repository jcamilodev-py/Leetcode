from typing import List

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans = []

        n = len(nums)
        for i in range(1, n, 2):
            for j in range(nums[i-1]):
                ans.append(nums[i])

        return ans


s = Solution()
print(s.decompressRLElist([1,1,2,3]))