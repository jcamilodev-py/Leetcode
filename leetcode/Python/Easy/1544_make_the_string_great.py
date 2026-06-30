class Solution:
    def makeGood(self, s: str) -> str:
        stack = []

        for i in s:

            if stack:
                l = ord(i) - 32
                j = ord(i) + 32
                if chr(l) == stack[-1] or chr(j) == stack[-1]:
                    stack.pop() 
                else:
                    stack.append(i)

            else:
                stack.append(i)

        return "".join(stack)


s = Solution()
print(s.makeGood("AaCcbB"))