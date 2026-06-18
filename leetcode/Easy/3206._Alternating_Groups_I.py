from typing import List

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        i, j = 0, 2
        ans = 0
        n = len(colors)

        while i < n:
            if i == n-1:
                if colors[i] != colors[0] and colors[i] == colors[j]:
                    ans+=1
                return ans
            elif colors[i] != colors[i+1] and colors[i] == colors[j]:
                ans+=1
                i+=1
                j+=1
            else:
                i+=1
                j+=1
            
            if j == n:
                j = j % j


        return ans

s = Solution()
print(s.numberOfAlternatingGroups([1,1,1]))