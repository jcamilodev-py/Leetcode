from typing import List
import heapq

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        dic = {}
        arr = []
        ans = -1

        for i in nums:
            if i not in dic:
                value = i
                dic[i] = 0
                while value > 0:

                    dic[i]+= value % 10
                    value//=10

            arr.append((dic[i], i))

        heapq.heapify(arr)
        while len(arr) > 1:

            n1 = heapq.heappop(arr)

            if n1[0] ==  arr[0][0]:
                ans = max(ans, n1[1] + arr[0][1])

        return ans 
    


s = Solution()
print(s.maximumSum([18,43,36,13,7]))