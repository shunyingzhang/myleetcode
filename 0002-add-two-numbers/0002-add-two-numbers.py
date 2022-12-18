# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        carry = 0
        
        while l1 or l2 or carry:
            if l1:
                val1 = l1.val
            else:
                val1 = 0
                
            if l2:
                val2 = l2.val
            else:
                val2 = 0
                
            val = val1 + val2  + carry
            cur.next = ListNode(val % 10)
            carry = val // 10
                
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            
            cur = cur.next
            
        return dummy.next
            
        
        
        
#         dummy = ListNode()
#         cur = dummy
#         carry = 0
#         while l1 or l2 or carry:
#             if l1:
#                 val1 = l1.val
#             else:
#                 val1 = 0
#             if l2:
#                 val2 = l2.val
#             else:
#                 val2= 0
            
#             val = val1 +  val2 + carry
#             carry = val // 10
#             cur.next = ListNode(val % 10)
            
#             cur = cur.next
#             if l1:
#                 l1 = l1.next
#             if l2:
#                 l2 = l2.next
            
#         return dummy.next
        