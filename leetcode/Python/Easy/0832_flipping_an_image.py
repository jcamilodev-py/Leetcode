from typing import List


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:

        for i in image:
            for j in range(len(i)):
                if i[j] == 1:
                    
                    i[j] = 0
                else:
                    i[j] =1
            i.reverse()
        return image
    
        # i,j = 0,0

        # while i < len(image):
        #     if image[i][j] == 1:
        #         image[i][j] = 0
        #         j+=1
        #     else:
        #         image[i][j] = 1
        #         j+=1
        #     if j >= len(image):
        #         image[i].reverse()
        #         i+=1
        #         j=0
        # return image

            
                

s = Solution()
print(s.flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))