class Solution(object):
    def isValid(self, s: str)->bool:
        map = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        stack = []
        for i in s:
            if i in map:
                if not stack:
                    return False
                top = stack.pop()
                if map[i] !=top:
                    return False
            else:
                stack.append(i)
        if stack:
            return False
        else:
            return True
            
s = "([])"
solu = Solution()
print(solu.isValid(s))
