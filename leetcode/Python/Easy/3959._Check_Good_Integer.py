class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        digit_sum = 0
        square_sum = 0

        while n > 0:
            digit_sum+= n % 10
            square_sum+= (n % 10) ** 2
            n//=10

        return square_sum - digit_sum >= 50



s = Solution()
print(s.checkGoodInteger(1000))