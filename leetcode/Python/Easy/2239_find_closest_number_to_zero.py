class Solution:
    def findClosestNumber(self, nums):
        contador = nums[0]
        for i in range(len(nums)):
            if abs(nums[i])< abs(contador):
                contador = nums[i]
            elif abs(nums[i]) == abs(contador):
                contador = max(nums[i], contador)
        return contador





s = Solution()
print(s.findClosestNumber([-1,1]))


# [-9, -5, -2, -1, 1, 3, 5]
# Input: nums = [-4,-2,1,4,8]
# Output: 1
# Explanation:
# The distance from -4 to 0 is |-4| = 4.
# The distance from -2 to 0 is |-2| = 2.
# The distance from 1 to 0 is |1| = 1.
# The distance from 4 to 0 is |4| = 4.
# The distance from 8 to 0 is |8| = 8.
# Thus, the closest number to 0 in the array is 1.