from bisect import bisect_left

def p(max_len=10):
    pals = []
    for length in range(1, max_len + 1):
        half_len = (length + 1) // 2
        start = 10 ** (half_len - 1) if half_len > 1 else 1
        end = 10 ** half_len
        for half in range(start, end):
            s = str(half)
            if length % 2 == 0:
                full = s + s[::-1]
            else:
                full = s + s[-2::-1]
            pals.append(int(full))
    return pals

all = sorted(p())
even = [i for i in all if i % 2 == 0]
odd = [i for i in all if i % 2 != 0]


class Solution:
    def minOperations(self, nums: list[int]) -> int:
        ans = 0

        for i in nums:
            pal = even if i % 2 == 0 else odd

            best = float('inf')
            idx = bisect_left(pal, i)
            if idx < len(pal):
                best = min(best, pal[idx] - i)

            if idx > 0:
                best = min(best, i - pal[idx-1])

            ans += best // 2

        return ans

s = Solution()
print(s.minOperations([10,12,14,16]))