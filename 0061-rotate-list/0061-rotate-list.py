# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        
        tail = head
        length = 1
        while tail.next:
            tail = tail.next
            length += 1
        k = k % length
        
        if k == 0:
            return head
        
        # cur = head
        # for i in range(length - k - 1):
        #     cur = cur.next
        # newhead = cur.next
        # cur.next = None
        # tail.next = head
        # return newhead
        
        
        
        
        pt1 = head
        pt2 = head
        while k > 0:
            pt1 = pt1.next
            k -= 1
        
        
        while pt1.next:
            pt2 = pt2.next
            pt1 = pt1.next
        
        res = pt2.next
        pt2.next = None
        pt1.next = head
        
        return res
        
        
            
        