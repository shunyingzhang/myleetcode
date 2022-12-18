# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        cur = dummy.next
        while cur:
            nxt = cur.next
            if cur.val == val:
                prev.next = nxt
            else:
                prev = cur
            cur = nxt
        
        
        
        return dummy.next

                    