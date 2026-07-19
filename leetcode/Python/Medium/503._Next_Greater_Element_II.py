from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums+=nums
        monotick = [-1] * (n*2)
        stack = []

        for i in range(n * 2):
            while stack and nums[i] > nums[stack[-1]]:
                idx = stack.pop()
                monotick[idx] = nums[i]
            
            stack.append(i)
        
        return monotick[:n]
        



s = Solution()
print(s.nextGreaterElements([1,2,1]))