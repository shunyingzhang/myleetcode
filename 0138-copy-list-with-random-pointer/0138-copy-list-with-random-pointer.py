"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        CopyList = {None: None}
        
        cur = head
        while cur:
            copy = Node(cur.val)
            CopyList[cur] = copy 
            cur = cur.next
        
        cur = head
        while cur:
            copy = CopyList[cur]
            copy.next = CopyList[cur.next]
            copy.random = CopyList[cur.random]
            cur = cur.next
        return CopyList[head]
        