class Solution:
    def canAliceWin(self, n: int) -> bool:
        current = 10
        alice = False
        while n >= current:
            n-=current
            current-=1

            if alice:
                alice = False
            else:
                alice = True

        return alice

            


s = Solution()
print(s.canAliceWin(12))