from math import gcd

class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumOdd = n ** 2
        sumEven = ((n * 2) / 2)
        sumEven*= n+1

        return gcd(sumOdd, int(sumEven))


s = Solution()
print(s.gcdOfOddEvenSums(4))