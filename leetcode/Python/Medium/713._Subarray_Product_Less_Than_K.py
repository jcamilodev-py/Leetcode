from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)

        ans = 0
        current = 1
        i = 0

        for j in range(n):
            current*=nums[j]

            while current >= k and i <= j:
                current//=nums[i]
                i+=1

            ans+=(j + 1) - i

        return ans
                

        
            
s = Solution()
print(s.numSubarrayProductLessThanK([10,5,2,6], k = 100))