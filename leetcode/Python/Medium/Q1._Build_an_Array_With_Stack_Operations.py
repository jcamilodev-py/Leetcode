from typing import List

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []
        stack = []
        r = list(range(1, n+1))
        n = len(target)

        i, j = 0, 0
        while len(stack) != n:
            if target[i] == r[j]:
                ans.append("Push")
                stack.append(target[i])
                i+=1
                j+=1
            else:
                ans.append("Push")
                ans.append("Pop")
                j+=1
        
        return ans




s = Solution()
print(s.buildArray(target = [1,3], n = 3))