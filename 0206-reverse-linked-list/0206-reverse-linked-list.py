# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        rev = head
        if head.next:
            rev = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        return rev
        
        
        
        
        # prev = None
        # curr = head
        # while curr:
        #     nxt = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = nxt
        # # return prev
        # return prev
#         if not head:
#             return None
        
#         rev = head
#         if head.next:
#             rev = self.reverseList(head.next)
#             head.next.next = head
#         head.next = None
#         return rev
            
        