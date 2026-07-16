from math import gcd

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)
        mx = nums[0]
        prefix_gcd = [0] * n
        ans = 0
        dic = {}

        for i in range(n):
            if nums[i] > mx:
                mx = nums[i]
            value = gcd(nums[i], mx)

            if (nums[i], mx) not in dic:
                dic[(nums[i], mx)] = value
            prefix_gcd[i] = dic[(nums[i], mx)]

        prefix_gcd.sort()

        i, j = 0, n-1

        while i < j:
            if (prefix_gcd[i], prefix_gcd[j]) not in dic:
                value = gcd(prefix_gcd[i], prefix_gcd[j])
                dic[(prefix_gcd[i], prefix_gcd[j])] = value
            
            ans+=dic[(prefix_gcd[i], prefix_gcd[j])]
            i+=1
            j-=1

        return ans


s = Solution()
print(s.gcdSum([3,6,2,8]))