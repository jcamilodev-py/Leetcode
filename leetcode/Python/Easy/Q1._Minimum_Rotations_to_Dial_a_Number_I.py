class Solution:
    def minRotations(self, s: str) -> int:
        ans = 0
        current = 0

        for i in s:
            target = int(i)

            d = abs(current - target)

            ans+= min(d, 10 - d)

            current = target

        return ans


s = Solution()
print(s.minRotations("0192837465"))