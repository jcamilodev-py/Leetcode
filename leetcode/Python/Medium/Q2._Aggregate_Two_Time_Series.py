class Solution:
    def aggregateTimeSeries(self, series1: list[list[int]], series2: list[list[int]]) -> list[list[int]]:
        ans = []


        while series1 and series2:
            if series1[0][0] < series2[0][0]:
                ans.append([series1[0][0], series1[0][1] + series2[0][1]])

                del series1[0]

            elif series1[0][0] > series2[0][0]:
                ans.append([series2[0][0], series1[0][1] + series2[0][1]])

                del series2[0]
            else:
                ans.append([series2[0][0], series1[0][1] + series2[0][1]])

                del series1[0]
                del series2[0]


        while series1:
            ans.append([series1[0][0], series1[0][1]])
            del series1[0]

        while series2:
            ans.append([series2[0][0], series2[0][1]])
            del series2[0]

        return ans


s = Solution()
print(s.aggregateTimeSeries([[6,7]], [[9,8],[13,7]]))