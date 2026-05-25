from typing import List

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        seen = set(range(1, (len(grid) ** 2) + 1))
        dic = {}
        ans = []
        for i in grid:
            for j in i:
                if j in seen:
                    seen.remove(j)
                
                if j in dic:
                    ans.append(j)
                else:
                    dic[j] = 1
                    
        ans.append(list(seen)[0])
        return ans



s = Solution()
print(s.findMissingAndRepeatedValues([[9,1,7],[8,9,2],[3,4,6]]))