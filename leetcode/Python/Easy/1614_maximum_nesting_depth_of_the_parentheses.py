class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        stack = []
        dic = {'1','2','3','4','5','6','7','8','9','0','+','-','*','/','(',')'}
        for i in s:

            if not stack and i not in dic:
                stack.append(i)
            elif i == "(":
                stack.append(i)
                
                if len(stack) > count:
                    count = len(stack)
                
            elif i == ")":

                stack.pop()

        return count



s = Solution()
print(s.maxDepth("1+(2*3)/(2-1)"))