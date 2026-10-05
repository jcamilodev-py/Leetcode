class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        d, prev, ans = 0, "(", 0

        for i in s:
            if i == "(":
                d+=1
                prev = "("
            else:
                d-=1
                if prev == "(":
                    ans+= 1 << d

                prev = i

        return ans





s = Solution()
print(s.scoreOfParentheses("()"))