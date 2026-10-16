class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        mod = 10**9 + 7
        n = len(nums)
        b1 = [0] * (n + 2)
        b2 = [0] * (n + 2)

        def upd(B, i, v):
            while i <= n:
                B[i] += v
                i += i & -i

        def pref(B, i):
            s = 0
            while i > 0:
                s += B[i]
                i -= i & -i
            return s

        def range_add(l, r, v):
            upd(b1, l, v)
            upd(b1, r + 1, -v)
            upd(b2, l, v * (l - 1))
            upd(b2, r + 1, -v * r)

        def prefix_sum(i):
            return pref(b1, i) * i - pref(b2, i)

        def range_sum(l, r):
            return prefix_sum(r) - prefix_sum(l - 1)

        last = {}
        sq = 0 
        ans = 0

        for j, x in enumerate(nums):
            p = last.get(x, -1)
            l, r = p + 2, j + 1
            s = range_sum(l, r)
            sq = (sq + 2 * s + (r - l + 1)) % mod
            ans = (ans + sq) % mod
            range_add(l, r, 1)
            last[x] = j

        return ans



s = Solution()
print(s.sumCounts([1,2,1]))