# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left - right == 0:
            return head
        l = head
        r = head
        for i in range(left - 2):
            l = l.next
        for i in range(right - 1):
            r = r.next
        
        prev = r.next
        cur = l.next
        if left == 1:
            cur = head
        for i in range(right - left + 1):
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
            
        if left == 1:
            return prev
        
        l.next = prev
        return head
        
            
        