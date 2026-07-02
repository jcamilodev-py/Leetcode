class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        MOD = 10 ** 9 + 7
        mid = target // 2
        k = min(mid, n)
        ans = int(k*(k+1) / 2)
        if mid < n:
            b = target + (n - mid) -1
            x = b *(b+1) // 2
            y = (target -1) * target // 2
            g = x - y
            ans+= g

        return ans % MOD


s = Solution()
print(s.minimumPossibleSum(n = 10, target = 9))