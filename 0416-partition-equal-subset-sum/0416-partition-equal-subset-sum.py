class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target % 2 !=  0:
            return False
        else:
            target = target // 2
        
        rsdl = set()
        rsdl.add(target)
        
        for n in nums:
            if n in rsdl:
                return True
            nextrsdl = set()
            for r in rsdl:
                nextrsdl.add(r - n)
                nextrsdl.add(r)
            
            rsdl = nextrsdl
                
        return False
            
            
            
        