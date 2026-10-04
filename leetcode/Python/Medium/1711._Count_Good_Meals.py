from collections import defaultdict


class Solution:
    def countPairs(self, deliciousness: list[int]) -> int:
        mod = 10 **9 + 7

        dic = defaultdict(int)

        ans = 0

        for i in deliciousness:

            value = 1

            while value <= 2 * 10**20:
                target = value - i

                if target in dic:

                    ans+=dic[target]

                value*=2

            dic[i]+=1

        return ans % mod


            

s = Solution()
print(s.countPairs([1048576,1048576]))