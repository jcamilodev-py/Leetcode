from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge_sort(arr):

            if len(arr) <= 1: return arr

            m = len(arr) // 2

            l = arr[:m]
            r = arr[m:]

            ls = merge_sort(l)
            rs = merge_sort(r)

            return merge(ls, rs)

        def merge(l, r):
            i, j = 0, 0
            ans = []

            while i < len(l) and j < len(r):
                if l[i] <= r[j]:
                    ans.append(l[i])
                    i+=1
                else:
                    ans.append(r[j])
                    j+=1

            ans.extend(l[i:])
            ans.extend(r[j:])

            return ans

        return merge_sort(nums)
                





s = Solution()
print(s.sortArray([5,2,3,1]))