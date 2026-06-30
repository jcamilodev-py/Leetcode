class Solution:
    def minimumChairs(self, s: str) -> int:
        chairs = 0
        count = 0
        for i in s:
            if i == "E":
                count+=1
                if count > chairs:
                    chairs = count
            else:
                count -=1
        return chairs


s = Solution()
print(s.minimumChairs("ELEELEELLL"))


# Input: s = "EEEEEEE"

# Output: 7

# Explanation:

# After each second, a person enters the waiting room and no person leaves it. Therefore, a minimum of 7 chairs is needed.

# Example 2:

# Input: s = "ELELEEL"

# Output: 2

