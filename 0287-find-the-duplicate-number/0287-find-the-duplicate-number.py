class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        while True:
            n1 = nums[slow]
            n2 = nums[nums[fast]]
            if n1 == n2:
                break
            
            slow = n1
            fast = n2
        
        slow = 0
        while True:
            l1 = nums[slow]
            l2 = nums[n1]
            if l1 == l2:
                break;
            slow = l1
            n1 =l2
        
        return l1
            
        