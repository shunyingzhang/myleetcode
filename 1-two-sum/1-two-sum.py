class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Map = {}
        for i, a in enumerate(nums):
            diff = target - a
            if diff in Map:
                return [Map[diff], i]
            Map[a] = i 
        return
        