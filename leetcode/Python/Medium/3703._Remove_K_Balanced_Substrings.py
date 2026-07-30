class Solution:
    def removeSubstring(self, s: str, k: int) -> str:
        stack = []
        n = len(s)
        for i in range(n):
            if not stack:
                stack.append([s[i], 1])
            else:
                if stack[-1][0] == s[i]:
                    stack[-1][1]+=1
                else:
                    stack.append([s[i], 1])

                if len(stack) >= 2 and s[i] == ")" and stack[-1][1] == k and stack[-2][1] >=k:
                    stack.pop()
                    stack[-1][1]-=k
                    if stack[-1][1] == 0:
                        stack.pop()
        ans = []
        for i in stack:
            ans.append(i[0] * i[1])

        return "".join(ans)
        

s = Solution()
print(s.removeSubstring("(()(()(()))((()", 2))