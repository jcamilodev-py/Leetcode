from bisect import bisect_right
from typing import List

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        ans = [0] * len(queries)
        m = max(nums)
        freq = [0] * (m+1)
        count = [0] * (m+1)

        for i in nums:
            freq[i]+=1
        
        for i in range(1, m+1):
            for j in range(i, m+1, i):
                count[i]+=freq[j]
        
        exact = [0] * (m+1)

        for i in range(m, 0, -1):
            total = count[i] * (count[i]-1) // 2

            for j in range(2*i, m+1, i):
                total-=exact[j]
            
            exact[i] = total
        
        p = [0] * (m+1)
        for i in range(1, m+1):
            p[i] = p[i-1] + exact[i]

        m = len(queries)
        for i in range(m):
            g = bisect_right(p, queries[i])
            ans[i] = g
        
        return ans



s = Solution()
print(s.gcdValues([2,3,4], queries = [0,2,2]))