from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        l1, l2 = [1]*n, [1]* n
        ans = 0

        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                l1[i] = l1[i-1]+1

        
        for j in range(n-2, -1, -1):
            if ratings[j] > ratings[j+1]:
                l2[j] = l2[j+1]+1


        for i in range(n):
            ans+= max(l1[i], l2[i])
        
        return ans

s = Solution()
print(s.candy([1,0,2]))