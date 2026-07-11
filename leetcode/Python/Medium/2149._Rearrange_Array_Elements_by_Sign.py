from typing import List

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        l1, l2 = [], []
        ans = []


        for i in nums:
            if i < 0: l2.append(i)
            else: l1.append(i)
        
        for i in range(len(l1)):
            ans.append(l1[i])
            ans.append(l2[i])
            
        return ans


s = Solution()
print(s.rearrangeArray([3,1,-2,-5,2,-4]))