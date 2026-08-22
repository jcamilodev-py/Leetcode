class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        return arr.index(max(arr))




s = Solution()
print(s.peakIndexInMountainArray([0,10,5,2]))