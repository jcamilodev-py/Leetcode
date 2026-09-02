class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        odd, even = 0, 0
        n = len(nums1)

        for i in nums1:
            if i % 2 == 0:
                even+=1
            else:
                odd+=1

        return True if odd >= 1 or odd == n or even == n else False



s = Solution()
print(s.uniformArray([30,99,80]))