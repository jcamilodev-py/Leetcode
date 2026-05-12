class Solution:
    def minLength(self, s: str) -> int:
        stack = []

        for i in s:

            if stack and stack[-1] == 'A' and i == 'B' or stack and stack[-1] == 'C' and i == 'D':
                stack.pop()

            else:
                stack.append(i)

        return len(stack)




s = Solution()
print(s.minLength("CACDBD"))