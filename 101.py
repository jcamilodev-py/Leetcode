# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []

        current = head
        while current != None:
            stack.append(current.val)
            current = current.next

        current = head
        for i in reversed(stack):
            if current.val != i:
                return False
            current = current.next
            
        return True
                


s = Solution()
print(s.isPalindrome([1,2,2,1]))