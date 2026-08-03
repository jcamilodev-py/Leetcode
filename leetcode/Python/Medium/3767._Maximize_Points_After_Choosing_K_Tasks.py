from typing import List

class Solution:
    def maxPoints(self, technique1: List[int], technique2: List[int], k: int) -> int:
        ans = sum(technique2)
        n = len(technique1)
        arr = [0] * n

        for i in range(n):
            arr[i] = technique1[i] - technique2[i]


        arr.sort(reverse=True)

        for i in range(n):
            if k > 0:
                ans+=arr[i]
                k-=1
            else:
                if arr[i] > 0:
                    ans+=arr[i]
                else:
                    return ans

        return ans           




s = Solution()
print(s.maxPoints(technique1 = [5,2,10], technique2 = [10,3,8], k = 2))