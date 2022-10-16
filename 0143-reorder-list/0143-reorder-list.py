# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        snd = slow.next
        slow.next = None
        while snd:
            tmp = snd.next
            snd.next = prev
            prev = snd
            snd = tmp
        
        first = head
        snd = prev
        while snd:
            tmp1 = first.next
            tmp2 = snd.next
            first.next = snd
            snd.next = tmp1
            first = tmp1
            snd = tmp2
    