class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)

        minn = prices[0]
        maxx = prices[n-1]
        
        l = [0] * n
        r = [0] * n

        for i in range(1, n):
            minn = min(minn, prices[i])
            l[i] = max(l[i-1], prices[i] - minn)

        for i in range(n-2, -1, -1):
            maxx = max(maxx, prices[i])
            r[i] = max(r[i+1], maxx - prices[i])

        ans = 0

        for i in range(n):
            ans = max(ans, l[i] + r[i])

        return ans


s = Solution()
print(s.maxProfit([3,3,5,0,0,3,1,4]))