class Solution:
    def maximizeSum(self, nums: list[int], k: int) -> int:
        gains = []

        for i in nums:
            c = [0] * 10
            v = i
            while v:
                c[v % 10] += 1
                v //= 10

            x = 0
            for d in range(9, -1, -1):
                for _ in range(c[d]):
                    x = x * 10 + d

            gains.append(x - i)

        gains.sort(reverse=True)
        return sum(nums) + sum(gains[:k])
        





s = Solution()
print(s.maximizeSum([102,90,14], k = 2))