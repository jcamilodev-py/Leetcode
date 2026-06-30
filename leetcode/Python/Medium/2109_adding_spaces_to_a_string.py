from typing import List

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = []

        current = 0
        for i in spaces:
            ans.append(s[0+current:i])
            current = i
            
        ans.append(s[spaces[-1]:])

        return " ".join(ans)


s = Solution()
print(s.addSpaces("spacing", spaces = [0,1,2,3,4,5,6]))