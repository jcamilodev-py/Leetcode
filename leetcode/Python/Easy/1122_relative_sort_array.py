class Solution:
    def relativeSortArray(self, arr1, arr2):
        dic = {}
        lista = []
        ls = []
        for i in arr2:
            if i in arr1:
                dic[i] = arr1.count(i)
        for j in dic:
            for l in range(dic[j]):
              lista.append(j)

        for x in arr1:
            if x not in arr2:
                ls .append(x)
        ls.sort()
        return lista+ls

s = Solution()
print(s.relativeSortArray([28,6,22,8,44,17], [22,28,8,6]))
# [2,2,2,1,4,3,3,9,6,7,19]

