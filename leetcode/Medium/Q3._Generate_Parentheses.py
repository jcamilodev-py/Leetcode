from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        ans = []

        def dfs(current, open, close):
            if open + close == 2*n:
                ans.append(current)
                return
            
            current_open = "("
            current_close = ")"

            if open < n:            
                dfs(current + current_open, open+1, close)
            if close < open:
                dfs(current + current_close, open, close+1)
                
        dfs("", 0, 0)
        return ans

s = Solution()
print(s.generateParenthesis(3))