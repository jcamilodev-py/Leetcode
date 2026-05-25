from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        count = 0
        students.reverse()
        sandwiches.reverse()
        while len(students) > count:

            if students[-1] == sandwiches[-1]:
                students.pop()
                sandwiches.pop()
                count = 0
            else:
                students = [students[-1]] + students[:-1]
                count +=1

        return len(students)



s = Solution()
print(s.countStudents(students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1]))