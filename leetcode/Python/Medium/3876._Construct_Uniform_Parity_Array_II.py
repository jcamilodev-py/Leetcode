class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        n = len(nums1)
        nums1.sort()

        even, odd = [], []

        for i in range(n):
            if nums1[i] % 2 == 0:
                even.append(nums1[i])
            else:
                odd.append(nums1[i])
        

        if len(even) == n or len(odd) == n:
            return True

        for i in even:
            if i - odd[0] < 1 and i - odd[-1] < 1:
                return False

        return True




s = Solution()
print(s.uniformArray([2,3]))