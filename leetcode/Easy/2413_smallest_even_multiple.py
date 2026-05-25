class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        while n %2 != 0:
            n*=2
        return n


s = Solution()
print(s.smallestEvenMultiple(n = 6))