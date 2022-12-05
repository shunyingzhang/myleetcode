class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = [-1] * len(arr)

        rightMax = arr[len(arr) - 1]
        
        for i in range(len(arr) - 2, -1, -1):
            res[i] = max(rightMax, arr[i + 1])
            rightMax = res[i]
        
        return res
        