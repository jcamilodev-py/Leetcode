class Solution:
    def simplifiedFractions(self, n: int) -> list[str]:
        seen = set()
        ans = []
        for i in range(1, n):
            for j in range(i+1,n+1):
                if i / j not in seen:
                    ans.append(str(i) + "/" + str(j))
                    seen.add(i/j)
        
        return ans





s = Solution()
print(s.simplifiedFractions(4))