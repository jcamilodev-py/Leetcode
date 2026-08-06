from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def h(l, r):
            if l > r:
                return 

            m = (l + r) //  2

            root = TreeNode(nums[m])  
            root.left =  h(l, m-1)
            root.right = h(m+1, r)

            return root

        return h(0, len(nums)-1)

        

s = Solution()
print(s.sortedArrayToBST([-10,-3,0,5,9]))