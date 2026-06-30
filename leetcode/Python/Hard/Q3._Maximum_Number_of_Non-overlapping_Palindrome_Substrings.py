class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        i = 0
        seen = []
        n = len(s)

        for i in range(n):
            l = i
            r = i

            while l >= 0 and r <= n-1 and s[l] == s[r]:
                if r - l + 1 >=k:
                    seen.append((l,r))
                l-=1
                r+=1
            
            l, r = i,  i+1

            while l >= 0 and r <= n-1 and s[l] == s[r]:
                if r - l + 1 >=k:
                    seen.append((l,r))
                l-=1
                r+=1

        if not seen:
            return 0


        seen.sort(key=lambda x: x[1])
        greedy = [seen[0]]
        last_end = greedy[0][1]
        for i in range(1, len(seen)):
            if seen[i][0] > last_end:
                greedy.append(seen[i])
                last_end = seen[i][1]

        return len(greedy)



s = Solution()
print(s.maxPalindromes("sjbxiufnaanqkwsqswkqrcznzcddhtuhtthuttjfuufjtcfywgecegwyhhnnhtozczirynhhnyrire", k = 3))