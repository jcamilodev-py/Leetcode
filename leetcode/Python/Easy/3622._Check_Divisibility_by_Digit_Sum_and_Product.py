class Solution:
    def checkDivisibility(self, n: int) -> bool:
        value = n
        s = 0
        p = 1

        while n:
            s+= n % 10
            p*= n % 10
            n //=10

        return value % (s + p) == 0


s = Solution()
print(s.checkDivisibility(99))