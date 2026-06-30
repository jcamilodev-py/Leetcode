class Solution:
    def containsNearbyDuplicate(self, nums, k):
        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic:

                if abs(i - dic[nums[i]])<=k:
                    return True
                else:
                    dic[nums[i]] = i
            else:
                dic.update({nums[i]:i})
        return False

            
        #     for j in range(i+1,len(nums)):
        #         if nums[i] == nums[j] and abs(i - j) <=k:
        #             return True
        # return False




s = Solution()
print(s.containsNearbyDuplicate([1,2,3,1], 2))
# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
# Example 1:

# Input: nums = [1,2,3,1], k = 3
# Output: true
# Example 2:

# Input: nums = [1,0,1,1], k = 1
# Output: true
# Example 3:

# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false