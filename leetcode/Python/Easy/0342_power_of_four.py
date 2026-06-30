class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        while 1<=n:
            if 1== n:
                return True
            else:
                n /=4
        return False
    
s = Solution()
print(s.isPowerOfFour(16))

