from typing import List, Counter

class Solution:
    def firstUniqueFreq(self, nums: List[int]) -> int:
        seen =  set({})

        dic = Counter(nums)

        l = list(dic.items())
        n = len(l)

        for i in range(n):
            ans = True
            for j in range(i+1, n):
                print(i, l[i][1], l[j][1], j)
                if l[i][1] == l[j][1] or l[i][1] in seen:
                    seen.add(l[i][1])
                    ans = False
                    break

            if ans and l[i][1] not in seen:
                return l[i][0]
                
        return -1 if l[-1][1] in seen else l[-1][0]


s = Solution()
print(s.firstUniqueFreq([10,10,20,20]))