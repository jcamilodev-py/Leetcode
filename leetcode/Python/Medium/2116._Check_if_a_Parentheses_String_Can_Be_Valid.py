class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:

        if len(s) % 2 != 0:
            return False
        
        minimum, maximum = 0, 0

        n = len(s)

        for i in range(n):
            if locked[i] == "0":
                minimum, maximum = minimum-1, maximum+1
            elif s[i] == ")":
                minimum, maximum = minimum-1, maximum-1
            else:
                minimum, maximum = minimum+1, maximum+1

            if maximum < 0:
                return False

            minimum = max(minimum, 0)

        return minimum == 0


            
s = Solution()
print(s.canBeValid("))()))", locked = "010100"))