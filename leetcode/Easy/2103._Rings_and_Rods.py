class Solution:
    def countPoints(self, rings: str) -> int:
        n = len(rings)
        dic = {}
        ans = 0

        for i in range(0, n-1, 2):
            if int(rings[i+1]) not in dic:
                dic[int(rings[i+1])] = {rings[i]}
            else:
                dic[int(rings[i+1])].add(rings[i])
        
        for i in dic:
            if len(dic[i]) == 3:
                ans+=1
        
        return ans



s = Solution()
print(s.countPoints("B0B6G0R6R0R6G9"))