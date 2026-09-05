class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:

        n = len(nums)
        inf = float('inf')

        def h(nums, o, d):
            p = [d]

            for i in nums:
                p.append(o(i, p[-1]))

            return p

        p = h(nums, max, 0)
        s = h(nums[::-1], min, inf)[::-1]

        for i in range(n):
            if p[i+1] - s[i] <= k:
                return i
        return -1





s = Solution()
print(s.firstStableIndex([5,0,1,4], k = 3))