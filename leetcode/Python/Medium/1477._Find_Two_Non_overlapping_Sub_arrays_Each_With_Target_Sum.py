class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:

        n = len(arr)

        dp = [float("inf")] * n
        l,r = 0,0

        current_sum = arr[0]
        ans = float('inf')
        while r < n:

            if current_sum < target:
                r+=1
                if r == n:
                    break
                current_sum+=arr[r]
            elif current_sum > target:
                current_sum-=arr[l]
                l+=1


            else:
                if l > 0 and dp[l-1] != float('inf'):
                    ans = min(ans, dp[l-1] + (r - l +1))

                dp[r] = r - l + 1

                current_sum-=arr[l]
                l+=1

            if r > 0:
                dp[r] = min(dp[r], dp[r-1])


        return ans if ans != float('inf') else -1


         



                    

s = Solution()
print(s.minSumOfLengths([3,2,2,4,3], target = 3))