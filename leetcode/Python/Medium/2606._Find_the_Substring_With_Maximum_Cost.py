class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: list[int]) -> int:
        dic = {chr(ord('a') + i): i+1 for i in range(26)}
        dic.update(zip(chars, vals))

        current = 0
        ans = 0

        for i in s:
            current+=dic[i]

            if current < 0:
                current = 0

            ans = max(ans, current)

        return ans

s = Solution()
print(s.maximumCostSubstring(s = "adaa", chars = "d", vals = [-1000]))