import heapq


class Solution:
    def maxScore(self, nums1: list[int], nums2: list[int], k: int) -> int:
        pairs = [(i,j) for i,j in zip(nums1, nums2)]
        pairs = sorted(pairs, key=lambda p: p[1], reverse=True)

        heap = []
        s = 0
        ans = 0

        print(pairs)

        for i, j in pairs:
            s+=i
            heapq.heappush(heap, i)

            if len(heap) > k:
                s-=heapq.heappop(heap)

            if len(heap) == k:
                ans = max(ans, s * j)

        return ans




s = Solution()
print(s.maxScore(nums1 = [1,3,3,2], nums2 = [2,1,3,4], k = 3))