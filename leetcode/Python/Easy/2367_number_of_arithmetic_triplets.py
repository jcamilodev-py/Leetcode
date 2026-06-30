from typing import List


class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        dic = {}
        count = 0

        for i in nums:
            dic[i] = diff

        for j in nums:
            if j + dic[j] in dic and dic[j]+  dic[j]+j in dic:
                count +=1
        return count


s = Solution()
print(s.arithmeticTriplets([3,6,9,12,15], 3))