class Solution:
    def reverseParentheses(self, s: str) -> str:
        p, stack, ans = {}, [], []

        for i,c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif c == ")":
                j = stack.pop()
                p[i] = j
                p[j] = i

        i,d = 0,1

        while i < len(s):
            if s[i] == "(" or s[i] == ")":
                i = p[i]
                d = -d
            else:
                ans.append(s[i])

            i+=d

        return "".join(ans)

        

        

s = Solution()
print(s.reverseParentheses("(u(love)i)"))