class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = []
        total = 0
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] % 2 == 0:
                    if nums[j] % 2 != 0:
                        total+=1
                else:
                    if nums[j] % 2 == 0:
                        total+=1
            ans.append(total)
            total = 0
        
        return ans

s = Solution()
print(s.countOppositeParity([1,2,3,4]))