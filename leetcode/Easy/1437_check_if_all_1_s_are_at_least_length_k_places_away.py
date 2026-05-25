from typing import List

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        j = 0
        for i in range(len(nums)):
            if nums[i] == 1 and i != j:
                if nums[j] == 1:
                    if (i - j) -1 < k:
                        return False
                    else:
                        j = i
                else:
                    while nums[j] != 1:
                        j+=1
        return True

     

s = Solution()
print(s.kLengthApart([0,0,0,1,0,1], k = 2))