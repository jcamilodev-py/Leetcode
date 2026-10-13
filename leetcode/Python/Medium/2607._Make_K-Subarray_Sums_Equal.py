from math import gcd


class Solution:
    def makeSubKSumEqual(self, arr: list[int], k: int) -> int:
        n = len(arr)
        g = gcd(n, k)
        ans = 0

        for i in range(g):
            group = []
            j = i

            while j < n:
                group.append(arr[j])
                j = j + g

            group.sort()

            m = group[len(group) // 2]

            for x in group:
                ans+= abs(x - m)

        return ans


s = Solution()
print(s.makeSubKSumEqual([1,4,1,3], k = 2))