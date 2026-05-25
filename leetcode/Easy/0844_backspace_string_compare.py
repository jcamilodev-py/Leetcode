class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s = []
        stack_t = []

        for i in s:
                if i == "#":
                    if stack_s:
                      stack_s.pop()

                else:
                    stack_s.append(i)

        for j in t:
                if j == "#":
                    if stack_t:
                      stack_t.pop()

                else:
                     stack_t.append(j)

        return stack_s == stack_t



s = Solution()
print(s.backspaceCompare("ab##", "c#d#"))