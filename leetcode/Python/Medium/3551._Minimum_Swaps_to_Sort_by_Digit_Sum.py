from typing import List


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        indexs = {n: i for i, n in enumerate(nums)}

        def helper(value):
            s = 0

            while value:
                s+=value%10
                value//=10

            return s

        nums.sort()
        nums.sort(key = lambda x: helper(x))

        v = set()

        ans = 0


        for i in range(len(nums)):
            if i in v:
                continue

            j = i
            steps = 0

            while j not in v:
                v.add(j)
                steps+=1
                j = indexs[nums[j]]

            ans+= steps - 1

        return ans



s = Solution()
print(s.minSwaps([18,43,34,16]))