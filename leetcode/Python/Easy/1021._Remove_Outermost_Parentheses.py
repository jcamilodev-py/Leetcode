class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        open = 1
        idx = 0
        ans = []

        for i in range(1, len(s)):
            if s[i] == "(":
                open+=1
            else:
                open-=1

            if open == 0:
                ans.append(s[idx+1:i])
                idx = i+1

        return "".join(ans)
        




s = Solution()
print(s.removeOuterParentheses("()()"))