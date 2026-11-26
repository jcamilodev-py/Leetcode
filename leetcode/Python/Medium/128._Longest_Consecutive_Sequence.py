class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        parent = {}
        size = {}

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            if size[ra] < size[rb]:           
                ra, rb = rb, ra
            parent[rb] = ra
            size[ra] += size[rb]

        for i in nums:
            if i in parent:
                continue
            parent[i] = i

            size[i] = 1

            if i - 1 in parent:
                union(i, i-1)

            if i + 1 in parent:
                union(i, i+1)

        return max(size[i] for i in size)
        

s = Solution()
print(s.longestConsecutive([100,4,200,1,3,2]))