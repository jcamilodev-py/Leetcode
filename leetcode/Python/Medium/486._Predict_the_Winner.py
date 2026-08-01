from typing import List

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        m = {}
        def max_diff(l, r):
            if l == r:
                return nums[l]

            if (l, r) in m:
                return m[(l, r)]

            pl = nums[l] - max_diff(l+1, r)
            pr = nums[r] - max_diff(l, r-1)

            m[(l, r)] = max(pl, pr)

            return m[(l, r)]

        return max_diff(0, len(nums)-1) >=0


s = Solution()
print(s.predictTheWinner([1,5,233,7]))