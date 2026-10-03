class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]

        ans = 0

        for i, j in enumerate(s):
            if j == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    ans = max(ans, i - stack[-1])

        return ans




s = Solution()
print(s.longestValidParentheses(")()())"))