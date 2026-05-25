class Solution:
    def mergeSimilarItems(self, items1,items2):
        dic = {}
        l = items1 + items2
        l.sort()

        for i in range(len(l)):
            if l[i][0] not in dic:
                dic[l[i][0]] = l[i][1]
            else:
                dic[l[i][0]] = dic[l[i][0]] + l[i][1]
        output = [None] *len(dic)

        for i,d in enumerate(dic):
            output[i] =[d,dic[d]]
        return output

# from collections import defaultdict


# class Solution:
#     def mergeSimilarItems(self, items1, items2):
#         m = defaultdict(int)
#         items1.extend(items2)
#         for entry in items1:
#             m[entry[0]] += entry[1]
        
#         return sorted(m.items(), key=lambda x : x[0])
    

s = Solution()
print(s.mergeSimilarItems(items1 = [[1,3],[2,2]], items2 = [[7,1],[2,2],[1,4]]))