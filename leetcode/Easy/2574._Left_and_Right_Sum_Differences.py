from typing import List

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        count = 0
        ans = []
        s = sum(nums)

        for i in nums:
            ans.append(abs((s - i ) - count))
            s-=i
            count+=i
        return ans


s = Solution()
print(s.leftRightDifference([10,4,8,3]))