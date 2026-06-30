class Solution:
    def minTimeToVisitAllPoints(self, points):
        x = 0
        y = 1
        lista = []
        while y< len(points):
            num_dx = abs(points[x][0] - points[y][0])
            num_dy = abs(points[x][1] - points[y][1])
            time = max(num_dx, num_dy)
            lista.append(time)
            x +=1
            y +=1
        output = sum(lista)
        return output



s = Solution()
print(s.minTimeToVisitAllPoints([[3,2],[-2,2]]))

        