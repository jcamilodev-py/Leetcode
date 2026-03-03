class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        dic = {'1','2','3','4','5','6','7','8','9','0'}
        s = list(s)

        for i in reversed(s):
            if i in dic:
                stack.append(i)
            else:
                if stack and stack[-1] in dic:
                    stack.pop()
                else:
                    stack.append(i)

        stack = reversed(stack)
        
        return "".join(stack)

s = Solution()
print(s.clearDigits("c3b4ba"))