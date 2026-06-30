class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        lista = []
        for i in range(len(nums)):
            contador = 0
            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    contador += 1
            lista.append(contador)
        return lista


sol = Solution()
print(sol.smallerNumbersThanCurrent([8, 1, 2, 2, 3]))
            