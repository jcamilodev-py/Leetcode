class Solution:
    def minimumSum(self, num: int) -> int:
        n = sorted(str(num))
        n1 = n[0] + n[2]
        n2 = n[1] + n[3]
        return int(n1) + int(n2)
        
          

s = Solution()
print(s.minimumSum(2687))