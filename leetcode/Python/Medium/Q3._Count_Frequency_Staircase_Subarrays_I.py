class Solution:
    def countStaircase(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0

        for i in range(n):
            freq = {}    
            order = {}  
            d = 0       
            good = 0    

            for j in range(i, n):
                v = nums[j]

                if v not in order:
                    d += 1
        
                    if i + d * (d + 1) // 2 > n:
                        break
                    order[v] = d
                    freq[v] = 1
                    if d == 1:
                        good += 1
                else:
                    t = order[v]
                    f = freq[v]
                    if f == t:
                        good -= 1
                    f += 1
                    freq[v] = f
                   
                    if f > t:
                        break
                    if f == t:
                        good += 1

                if good == d:
                    ans += 1

        return ans




s = Solution()
print(s.countStaircase([2,3,4,4,3,4]))