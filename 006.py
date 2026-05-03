class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        str = list(s)
        for i in range(len(s)):
            value = str[0]
            del str[0]
            str.append(value)
            if "".join(str) == goal:
                return True
            
        return False


s = Solution()
print(s.rotateString("aba", goal = "aab"))