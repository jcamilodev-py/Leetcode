class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for i in s:
            if stack:
              if i == stack[-1]:
                  stack.pop()
              else:
                  stack.append(i)

            else:
                stack.append(i)
        return "".join(stack)



s = Solution()
print(s.removeDuplicates("azxxzy"))
