class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] +=1
        m = max(dic.values())
        for i,j in dic.items():
            if j == m:
                return i



s = Solution()
print(s.majorityElement([3,2,2,2,3]))