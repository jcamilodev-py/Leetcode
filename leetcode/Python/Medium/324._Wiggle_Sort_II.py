from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]):
        n = len(nums)

        s = sorted(nums)
        m = (n + 1) // 2

        small = s[:m][::-1]
        large = s[m:][::-1]


        for i in range(len(small)):
            nums[2*i] = small[i]

        for i in range(len(large)):
            nums[2*i+1] = large[i]


s = Solution()
print(s.wiggleSort([1,2,3,4,5,6]))