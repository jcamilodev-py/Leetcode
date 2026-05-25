from typing import List, Counter

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        ans = 0
        counter = Counter(nums)
        maximum = max(counter.values())

        for i in counter.values():
            if i == maximum:
                ans+=i
        return ans


s = Solution()
print(s.maxFrequencyElements([1,2,3,4,5]))