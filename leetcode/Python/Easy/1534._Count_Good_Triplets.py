from typing import List

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        ans = 0
        n = len(arr)
        pref = [0] * 1001

        for j in range(n-1):
            for k in range(j+1, n):
                if abs(arr[j] - arr[k]) <= b:
                    m = min(arr[j] + a, arr[k] + c)
                    mx = max(arr[j] - a, arr[k] - c)
                    mx = max(mx, 0)
                    m = min(m, 1000)

                    if mx <= m:
                        ans += pref[m] - (0 if mx == 0 else pref[mx-1])
            for idx in range(arr[j], 1001):
                pref[idx]+=1
        return ans



s = Solution()
print(s.countGoodTriplets([3,0,1,1,9,7], a = 7, b = 2, c = 3))