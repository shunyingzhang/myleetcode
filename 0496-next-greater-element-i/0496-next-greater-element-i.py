class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1] * len(nums1)
        Hmap = {n: i for i, n in enumerate(nums1)}
        stack = []

        for n in nums2:
            while stack and n > stack[-1]:
                res[Hmap[stack.pop()]] = n
            if n in nums1:
                stack.append(n)
        return res
            





        # res = [-1] * len(nums1)
        # for i in range(len(nums1)):
        #     for j in range(len(nums2)):
        #         if nums1[i] == nums2[j]:
        #             if j + 1 == len(nums2):
        #                 continue
        #             for k in range(j + 1, len(nums2)):
        #                 if nums1[i] < nums2[k]:
        #                     res[i] = nums2[k]
        #                     break
        #             break
        # return res