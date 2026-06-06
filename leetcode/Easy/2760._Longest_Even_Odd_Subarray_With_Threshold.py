from typing import List

class Solution:
    def longestAlternatingSubarray(self, arr: List[int], threshold: int) -> int:
        l=0
        r=0
        ans=0
        n=len(arr)
        while l<n and r<n:
            if arr[l]%2==0 and arr[l]<=threshold:
                itr=0
                while r<n and arr[r]<=threshold and arr[r]%2==itr%2 :
                    r+=1
                    itr+=1
                ans=max(ans,(r-1)-l+1)
                l=r
            else:
                l+=1
                r+=1
        return ans 




s = Solution()
print(s.longestAlternatingSubarray([2,3,4,5], threshold = 4))