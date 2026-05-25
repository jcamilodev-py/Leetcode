from typing import List

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()

        m = float('inf')
        n = len(arr)
        ans = []

        for i in range(1, n):
            if abs(arr[i] - arr[i-1]) < m:
                m = abs(arr[i] - arr[i-1])
        
        for j in range(1, n):
            if abs(arr[j] - arr[j-1]) == m:
                ans.append([arr[j-1], arr[j]])
        
        return ans


s = Solution()
print(s.minimumAbsDifference([4,2,1,3]))