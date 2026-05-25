from typing import List

class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        dic = {num: i for i, num in enumerate(nums)}
        print(dic)
        for old, new in operations:
            i = dic.pop(old)
            nums[i] = new
            dic[new] = i

        return nums


s = Solution()
print(s.arrayChange([1,2], operations = [[1,3],[2,1],[3,2]]
))