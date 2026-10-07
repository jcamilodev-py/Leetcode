from functools import cache


class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        n = len(s)
        ans = []


        @cache
        def dp(i, current, d):
            if d < 0:
                return

            if i == n:
                if d == 0:
                    ans.append(current)
                return

            if s[i] not in "()":
                dp(i + 1, current + s[i], d)
            else:
                dp(i + 1, current + s[i], d + (1 if s[i] == "(" else -1))
                dp(i+1, current, d)

        dp(0, "", 0)

        m = max(len(value) for value in ans)
        res = [value for value in ans if len(value) == m]

        return res
            


s = Solution()
print(s.removeInvalidParentheses("(a)())()"))