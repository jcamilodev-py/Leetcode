class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        ans = []
        l = 0

        def recursive(current, l, k):

            if l == n:
                ans.append(current)
                return
            
            
            last = current % 10
            

            candidates = {last + k, last - k}
            

            for c in candidates:
                if 0 <= c <=9:
                    next_num = current * 10 + c
                    recursive(next_num, l + 1, k)


        for i in range(1,10):
            recursive(i, l+1, k)
        
        return ans
            

    

s = Solution()
print(s.numsSameConsecDiff(n = 3, k = 7))