class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        n = len(s)
        s = list(s)
        for i in range(n):
            if stack:
                if s[i] == ")":
                    if stack[-1][0] == "(":
                        stack.pop()
                    else:
                        stack.append((")", i))
                elif s[i] == "(":
                    stack.append(("(", i))
            else:
                if s[i] in "()":
                    stack.append((s[i], i))

        j = 0
        for i in stack:
            del s[i[1] - j]
            j+=1

        return "".join(s)



s = Solution()
print(s.minRemoveToMakeValid("))(("))