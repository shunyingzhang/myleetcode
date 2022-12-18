# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Cutting the linked list to half half
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reversing the second half
        prev = None
        cur = slow.next
        slow.next = None
        
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        
        #Comparing prev and head apple by apple:
        while head and prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        
        return True
            
            
            
            
            