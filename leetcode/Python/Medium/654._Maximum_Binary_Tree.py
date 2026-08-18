from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:

        def cartesian(arr):
            stack = []
            root = None

            for i in arr:
                current = TreeNode(i)
                last = None

                while stack and stack[-1].val < i:
                    last = stack.pop()

                if stack:
                    stack[-1].right = current
                else:
                    root = current

                current.left = last
                stack.append(current)
            return root

        return cartesian(nums)



s = Solution()
print(s.constructMaximumBinaryTree([3,2,1,6,0,5]))