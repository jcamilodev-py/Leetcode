class Solution:
    def maximumStrongPairXor(self, nums):
        xor = 0
        for i in nums:
            for j in nums:
                if abs(i-j) <= min(i,j):
                    value = i^j
                    if value > xor:
                        xor = value
                    else:
                        continue
                else:
                    continue
        return xor


# ∣x−y∣≤min(x,y)
s = Solution()
print(s.maximumStrongPairXor([5,4,3,2,1]))