class Solution:
    def removeElement(self, nums, val):
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k+=1
        return k


nums = [3,2,2,3]
val = 3
s = Solution()

print(s.removeElement(nums, val))

# lista = [1,2,3,4]
# for i in lista:
#     print(i)



