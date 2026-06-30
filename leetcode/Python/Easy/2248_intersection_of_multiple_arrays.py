class Solution:
    def intersection(self, nums):
        dic = {}
        output = []
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                if nums[i][j] in dic:
                    dic[nums[i][j]] = dic[nums[i][j]]+1
                    if dic[nums[i][j]] == len(nums):
                        output.append(nums[i][j])
                else:
                    dic[nums[i][j]] = 1
                    if dic[nums[i][j]] == len(nums):
                        output.append(nums[i][j])
        output.sort()
        return output




s = Solution()
print(s.intersection([[1,2,3],[4,5,6]]))



#Dado un arreglo bidimensional de enteros nums donde nums[i]
#es un arreglo no vacío de enteros positivos distintos, devuelve
#la lista de enteros que están presentes en cada arreglo de nums ordenados en orden ascendente.