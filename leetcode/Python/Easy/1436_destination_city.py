from typing import List

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        seen = set({})
        
        for i in paths:
            seen.add(i[0])

        for i in paths:
            if i[1] not in seen:
                return i[1]



s = Solution()
print(s.destCity([["B","C"],["D","B"],["C","A"]]))