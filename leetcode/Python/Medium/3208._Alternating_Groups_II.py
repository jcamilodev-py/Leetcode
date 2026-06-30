from typing import List

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        colors = colors + colors
        i,j, count, ans = 0, 1, 1, 0

        while j <= (n - 1) + (k - 1):
            if colors[j-1] == colors[j]:
                i = j
                j = i+1
                count = 1
            else:
                j+=1
                count+=1
            
            if count == k:
                ans+=1
                count -=1

        return ans


s = Solution()
print(s.numberOfAlternatingGroups([0,1,1], k = 3))