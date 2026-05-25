class Solution:
    def maxDistance(self, colors):
        output = 0
        for i in range(0, len(colors)):
            for j in range(0, len(colors)):
                if colors[i] != colors[j]:
                    value = abs(i - j)
                    if value >output:
                        output = value
                    else:
                        continue
                else:
                    continue
        return output



s = Solution()
print(s.maxDistance([1,2,2,2,2]))