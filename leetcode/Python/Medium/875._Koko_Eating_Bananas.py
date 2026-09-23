class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l, r = 1, max(piles)

        ans = r

        def can(k):
            time = 0

            for i in piles:
                time+= (i + k -1) // k

            return time <= h

        while l <= r:
            m = (l + r) // 2

            if can(m):
                ans = m
                r = m-1
            else:
                l = m+1

        return ans






s = Solution()
print(s.minEatingSpeed([3,6,7,11], h = 8))