from typing import List

class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        n = len(nums)
        cout = 0
        arr = [0]* (n + 1)
        for i in range(1, n+1):
            arr[i] = arr[i - 1] + nums[i - 1]
        
        for i in range(n-1):
            sum1 = arr[i+1] - arr[0]
            sum2 = arr[-1] - arr[i+1]
            if abs(sum1 - sum2) % 2 == 0:
                cout+=1

        return cout
        



s = Solution()
print(s.countPartitions([2,4,6,8]))