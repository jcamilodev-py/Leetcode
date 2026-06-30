from typing import List

class Solution:
        def sumOddLengthSubarrays(self, arr: List[int]) -> int:
            n = len(arr)
            ans = 0
            for i in range(n):
                total = (i + 1) * (n - i)
                odd = (total + 1) // 2
                ans += arr[i] * odd

            
            return ans
                        


s = Solution()
print(s.sumOddLengthSubarrays([1,4,2,5,3]))