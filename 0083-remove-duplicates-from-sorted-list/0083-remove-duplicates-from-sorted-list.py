# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        if not head:
            return head
        cur = head.next
        while cur:
            nxt = cur.next
            if cur.val == prev.val:
                prev.next = nxt
            else:
                prev = cur
            
            cur = nxt
        return head