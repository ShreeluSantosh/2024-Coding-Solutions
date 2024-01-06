class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        d = []
        d1 = []
        d2 = []
        for i in nums1:
            if (i not in nums2) and (i not in d1):
                d1.append(i)
        d.append(d1)
        for j in nums2:
            if (j not in nums1) and (j not in d2):
                d2.append(j)
        d.append(d2)
        return d