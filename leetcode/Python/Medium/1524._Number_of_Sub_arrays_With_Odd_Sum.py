from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        mod = 10 ** 9 + 7

        ans, current_sum, odd, even = 0,0,0,0

        for i in range(len(arr)):
            current_sum+=arr[i]

            if current_sum % 2:
                ans+=1+even
                odd+=1
            else:
                ans+=odd
                even+=1

            ans%=mod

        return ans 

        


s = Solution()
print(s.numOfSubarrays([1,3,5]))