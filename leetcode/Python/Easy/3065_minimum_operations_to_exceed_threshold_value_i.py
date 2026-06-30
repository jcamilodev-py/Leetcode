class Solution:
    def minOperations(self, nums, k):
        nums.sort()
        index, count = 0, 0
        while index< len(nums):
            if nums[index] < k:
                nums.remove(nums[index])
                count+=1
            else:
                index+=1
        return count


s = Solution()
print(s.minOperations([5,6,7], 0))