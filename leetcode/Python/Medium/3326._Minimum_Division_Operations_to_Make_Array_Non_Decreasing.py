from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def maximum_divisor(x):
            for i in range(2, int(x ** 0.5) + 1):
                if x % i == 0:
                    return i
            return x
        
        current = nums[-1]
        ans = 0
        n = len(nums)

        for i in range(n-2, -1, -1):
            if nums[i] > current:
                nums[i] = maximum_divisor(nums[i])

                if nums[i] > current:
                    return -1
                ans+=1
                
            current = nums[i]

        return ans
                
                

s = Solution()
print(s.minOperations([5,51,25]))