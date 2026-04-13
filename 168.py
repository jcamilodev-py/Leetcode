from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        value = sum(nums[:k])
        maximun = value
        for i in range(k, len(nums)):
            value += nums[i] - nums[i-k]
            maximun = max(maximun, value)

        return maximun / k


s = Solution()
print(s.findMaxAverage([1,12,-5,-6,50,3], 4))