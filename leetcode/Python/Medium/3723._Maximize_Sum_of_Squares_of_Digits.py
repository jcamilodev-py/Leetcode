class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        ans = "9" * (sum // 9)

        sum%= 9

        if sum:
            ans+=str(sum)

        n = len(ans)

        if n > num:
            return ""

        return ans + "0" * (num - n) 

             
            


s = Solution()
print(s.maxSumOfSquares(num = 2, sum = 17))