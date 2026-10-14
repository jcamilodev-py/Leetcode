class Solution:
    def threeFibonacciSum(self, n: int) -> bool:
        dp = [0, 1, 1]

        while dp[-1] + dp[-2] + dp[-3] < n:
            dp.append(dp[-1] + dp[-2])

        return True if  dp[-1] + dp[-2] + dp[-3] == n else False



s = Solution()
print(s.threeFibonacciSum(8))