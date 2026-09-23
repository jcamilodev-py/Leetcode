class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:

        l, r = max(weights), sum(weights)
        ans = r

        def can(cap):
            ships, current = 1, cap
            for i in weights:
                if current - i < 0:
                    ships+=1
                    current = cap

                current-=i

            return ships<=days

        while l <=r:
            m = (l + r) // 2
            print(m, l, r)

            if can(m):
                ans = m
                r = m-1
            else:
                l = m+1

        return ans
        
s = Solution()
print(s.shipWithinDays(weights = [1,2,3,4,5], days = 2)) 