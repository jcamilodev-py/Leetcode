from typing import List

class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        ans = [-1, -1]
        i = 0
        j = indexDifference
        n = len(nums)
        while j < n:
            if abs(nums[i] - nums[j]) >= valueDifference:
                ans[0] = i
                ans[1] = j
                return ans
            j+=1

            if j == n:
                i+=1
                j = indexDifference + i 
        return ans
                



s = Solution()
print(s.findIndices([5,1,4,1], indexDifference = 2, valueDifference = 4))