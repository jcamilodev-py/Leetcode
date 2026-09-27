from collections import Counter

class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        nums.sort()
        c = Counter(nums)
        seen = set()
        n = len(nums)

        ans = []

        while n != len(ans):
            for i in c:
                if c[i] > 0 and i not in seen:
                    ans.append(i)
                    c[i]-=1
                    seen.add(i)

            seen.clear()

        return ans
                







s = Solution()
print(s.rearrangeArray([16,5,10]))