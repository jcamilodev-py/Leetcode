# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:


        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast= fast.next.next

        return slow
        # current = head
        # count = 0


        # while current:
        #     count+=1
        #     current = current.next


        # count = count // 2

        # current = head
        # for i in range(count):
        #     current = current.next

        # return current