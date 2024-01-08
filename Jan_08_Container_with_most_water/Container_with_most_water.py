class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        m = nums[::-1]
        return m[k-1]