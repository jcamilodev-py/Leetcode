class Solution:
    def canBeEqual(self, target, arr) -> bool:
        target.sort()
        arr.sort()
        for i,j in zip(target,arr):
            if i == j:
                continue
            else:
                return False
        return True



s = Solution()
print(s.canBeEqual([3,7,9], [3,7,11]))
#  [7],  [7]
# [3,7,9],  [3,7,11]
        