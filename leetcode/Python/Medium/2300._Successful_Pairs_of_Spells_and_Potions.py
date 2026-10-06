from bisect import bisect_left


class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        potions.sort()
        ans = []
        m = len(potions)

        for i in spells:
            target = (success + (i-1)) // i
            idx = bisect_left(potions, target)
            ans.append(m - idx)

        return ans


s = Solution()
print(s.successfulPairs(spells = [3,1,2], potions = [5,8,8], success = 16))