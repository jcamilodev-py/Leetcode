class Solution:
    def checkValidString(self, s: str) -> bool:
        minimum, maximum = 0, 0

        for i in s:
            if i == "(":
                minimum, maximum = minimum+1, maximum+1
            elif i == ")":
                minimum, maximum = minimum-1, maximum-1
            else:
                minimum, maximum = minimum-1, maximum+1

            if maximum < 0:
                return False
            elif minimum < 0:
                minimum = 0

        return minimum == 0

        
s = Solution()
print(s.checkValidString("(*)"))