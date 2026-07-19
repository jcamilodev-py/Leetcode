class Solution:
    def canReach(self, start: list[int], target: list[int]) -> bool:
        if (start[0] + start[1]) % 2 == 0 and (target[0] + target[1]) % 2 == 0:
            return True
        elif (start[0] + start[1]) % 2 != 0 and (target[0] + target[1]) % 2 != 0:
            return True
        
        return False



s = Solution()
print(s.canReach([4,5], [6,6]))