class Solution:
    def smallestSubsequence(self, s: str) -> str:
        n = len(s)
        use = set()
        stack = []
        dic = {}

        for i in range(n):
            if s[i] not in dic:
                dic[s[i]] = 1
            else:
                dic[s[i]] = i



        for i in range(n):
            if not stack:
                stack.append(s[i])
                use.add(s[i])
                continue
            
            if s[i] not in use:
                while stack and s[i] < stack[-1]:
                    if dic[stack[-1]] > i:
                        v = stack.pop()
                        use.remove(v)
                        continue
                    else:
                        break

                stack.append(s[i])
                use.add(s[i])
                
        return "".join(stack)
            



s = Solution()
print(s.smallestSubsequence("cdadabcc"))