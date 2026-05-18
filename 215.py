class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        s = blocks[:k]
        count = s.count("W")
        ans = count
        n = len(blocks)
        
        if k == n:
            return count
        i,j = 1, k
        
        while j < n:

            if blocks[i-1] == "W" and blocks[j] == "B":
                count-=1
            elif blocks[i-1] == "B" and blocks[j] == "W":
                count+=1
        
            if count < ans:
                ans = count
            i+=1
            j+=1

        return ans


s = Solution()
print(s.minimumRecolors("WWBBBWBBBBBWWBWWWB", k = 16))