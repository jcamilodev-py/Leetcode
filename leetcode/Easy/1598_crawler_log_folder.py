from typing import List

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []

        for i in logs:
            if i == "../":
                if stack:
                    stack.pop()
            elif i != "./":
                stack.append(i)
        
        return len(stack)


s = Solution()
print(s.minOperations(["d1/","d2/","./","d3/","../","d31/"]))