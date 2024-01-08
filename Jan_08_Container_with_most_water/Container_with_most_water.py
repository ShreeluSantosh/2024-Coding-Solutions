class Solution:
    def maxArea(self, height: List[int]) -> int:
        mx = 0
        i = 0
        j  = len(height)-1
        while i < j:
            indDiff = j-i
            m = min(height[i], height[j])
            area = indDiff*m
            if area > mx:
                mx = area
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return mx
