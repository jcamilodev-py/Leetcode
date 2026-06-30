class Solution:
    def distributeCandies(self, candyType) -> int:
        l = []
        for i in range(len(candyType)):
            if not candyType[i] in l:
                l.append(candyType[i])
        return len(l[0:int(len(candyType)/2)])


s = Solution()
print(s.distributeCandies([6,6,6,6]))
# Input: candyType = [1,1,2,2,3,3]
# Output: 3
# Explanation: Alice can only eat 6 / 2 = 3 candies. Since there are only 3 types, she can eat one of each type.    