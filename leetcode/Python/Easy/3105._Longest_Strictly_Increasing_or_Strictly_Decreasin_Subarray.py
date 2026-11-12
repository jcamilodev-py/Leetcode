from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        def h(i, j, arr, ans):
            while j < n:
                if i == j:
                    j+=1
                elif arr[j] > arr[j-1]:
                    j+=1
                else:
                    ans = max(ans, j - i)
                    i = j

            ans = max(ans, j - i)
            return ans

        return max(h(0,0,nums,0), h(0,0,nums[::-1],0))




s = Solution()
print(s.longestMonotonicSubarray([3,2,1]))