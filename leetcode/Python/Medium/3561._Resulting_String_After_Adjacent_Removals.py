class Solution:
    def resultingString(self, s: str) -> str:
        stack = []
        for i in s:
            if not stack:
                stack.append(i)
                
            else:
                if ord(stack[-1])+1 == ord(i) or ord(stack[-1]) -1 == ord(i) or i == "a" and stack[-1] == "z" or i == "z" and stack[-1] == "a":
                    stack.pop()

                else:
                    stack.append(i)
        return "".join(stack)
                

s = Solution()
print(s.resultingString("mpnom"))