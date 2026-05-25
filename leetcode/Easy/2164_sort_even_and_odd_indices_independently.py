class Solution:
    def sortEvenOdd(self, nums):
        listaP, listaI = [], []
        countI, countJ = 0,0
        output = [None]*len(nums)
        for i in range(len(nums)):
            if i %2 == 0:
                listaP.append(nums[i])
            else:
                listaI.append(nums[i])
        listaP.sort()
        listaI.sort(reverse=True)
        for i in range(len(nums)):
            if i %2== 0:
             output[i] = listaP[countI]
             countI+=1
            else:
                output[i] = listaI[countJ]
                countJ+=1

        return output

s = Solution()


print(s.sortEvenOdd([2,1]))

        # x = [1,2,3]
        # x.sort(reverse=True)

        

        # i = 0
        # j = 2
        # if nums[i] % 2 == 0:
        #   print(j)
        #   while nums[i] >= nums[j]:
        #     if nums[i] > nums[j]:
        #         it = nums[i]
        #         print(i)
        #         print(nums[i])
        #         nums[i] = nums[j]
        #         nums[j] = it
        #         i+=2
        #         j+=2
        #     else:
        #         i+=2
        #         j+=2
        # else:
        #    while nums[i]<= nums[j]:
        #      if nums[i] < nums[j]:
        #         jt = nums[j]
        #         nums[j] = nums[i]
        #         nums[i] = jt
        #         i+=2
        #         j+=2
        #      else:
        #         i+=2
        #         j+=2

# Output: [2,3,4,1]
#numeros pares de menor a mayor
#numeros impares de mayor a menor