from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        i,j,count = 0,0,0
        g.sort()
        s.sort()

        while i < len(g) and j < len(s):
            if g[i] > s[j]:
                j+=1
            else:
                i+=1
                j+=1
                count+=1
        print(g,s)
        return count

# [7, 8, 9, 10] [5, 6, 7, 8]

s = Solution()
print(s.findContentChildren([1,2,3], s = [1,1]))
# Output: 1

# Input: g = [1,2], s = [1,2,3]
# Output: 2