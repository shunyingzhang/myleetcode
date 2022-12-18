# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        dummy = ListNode(0, head)
        prev = dummy
        
        while prev.next and prev.next.next:
            cur1 = prev.next
            cur2 = prev.next.next
            
            nxt = cur2.next
            prev.next = cur2
            cur2.next = cur1
            cur1.next = nxt
            
            prev = cur1
        return dummy.next