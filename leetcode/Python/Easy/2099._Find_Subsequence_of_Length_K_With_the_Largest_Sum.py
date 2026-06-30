from typing import List

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        arr = []
        ans = []

        for i,j in enumerate(nums):
            arr.append((i,j))
        
        s = sorted(arr, key=lambda x: x[1], reverse=True)

        value = s[:k]

        s = sorted(value, key=lambda x: x[0])

        for i in s:
            ans.append(i[1])
        
        return ans



s = Solution()
print(s.maxSubsequence([2,1,3,3], k = 3))