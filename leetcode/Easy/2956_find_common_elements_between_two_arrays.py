class Solution:
    def findIntersectionValues(self, nums1, nums2):
        dic1 = {}
        dic2 = {}
        lista1 = []
        lista2 = []
        for i in nums1:
            if i not in dic1:
                dic1[i] = 1
            else:
                dic1[i] = dic1[i]+1
        for j in nums2:
            if j not in dic2:
                dic2[j] = 1
            else:
                dic2[j] = dic2[j]+1
        for i in dic1:
           if i in dic2:
               lista1.append(dic1[i])
        for j in dic2:
            if j in dic1:
                lista2.append(dic2[j])     
        output = []  
        output.append(sum(lista1))
        output.append(sum(lista2))
        return output

s = Solution()
print(s.findIntersectionValues([1,2,3,4], [2,2,2,2]))