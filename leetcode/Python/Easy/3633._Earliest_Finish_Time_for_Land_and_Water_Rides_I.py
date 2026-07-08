from typing import List
from bisect import bisect_left

class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:

        def res(landStartTime, landDuration, waterStartTime, waterDuration):

            l = len(landStartTime)
            water = list(zip(waterStartTime, waterDuration))
            water.sort()
        
            starts = [s for s, d in water]
            s = len(starts)

            pre = [0] * s
            pre[0] = water[0][1]

            for i in range(1, s):
                pre[i] = min(pre[i-1], water[i][1])

            suff = [0] * s
            suff[-1] = water[-1][0] + water[-1][1]

            ans = float('inf')


            for i in range(s-2, -1, -1):
                suff[i] = min(water[i][0] + water[i][1], suff[i+1])
        
            for i in range(l):
                land_end = landStartTime[i] + landDuration[i]
                idx = bisect_left(starts, land_end)

                if idx > 0:
                    ans = min(ans, land_end + pre[idx-1])
            
                if idx < s:
                    ans = min(ans, suff[idx])

            return ans
        
        return min(res(landStartTime, landDuration, waterStartTime, waterDuration), res(waterStartTime, waterDuration, landStartTime, landDuration))


s = Solution()
print(s.earliestFinishTime(landStartTime = [2,8], landDuration = [4,1], waterStartTime = [6], waterDuration = [3]))