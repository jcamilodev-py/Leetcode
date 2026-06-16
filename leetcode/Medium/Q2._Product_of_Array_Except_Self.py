from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l = [1] * n
        r = [1] * n
        ans = []

        tmp = 1
        for i in range(1, n):
            tmp = tmp*nums[i-1]
            l[i] = tmp
        
        tmp = 1
        for j in range(n-2, -1, -1):
            tmp = tmp*nums[j+1]
            r[j] = tmp
        
        for x in range(n):
            ans.append(l[x] * r[x])

        return ans
    
    
s = Solution()
print(s.productExceptSelf([1,2,3,4]))