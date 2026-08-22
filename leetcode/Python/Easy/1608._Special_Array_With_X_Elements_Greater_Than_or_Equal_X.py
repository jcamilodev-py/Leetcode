from typing import List

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()

        n = len(nums)
        print(nums)

        for i in range(1, n+1):
            j = n - 1

            while True:
                if j == -1:
                    if i == n:
                        return i
                    break

                if nums[j] >= i:
                    j-=1
                else:
                    if (n - 1) - j == i:
                        return i
                    else:
                        break
        return -1





s = Solution()
print(s.specialArray([20,6,3,1,13,7,9,7,4,5,14,11,3,2,2,6,13,3,8,2]))