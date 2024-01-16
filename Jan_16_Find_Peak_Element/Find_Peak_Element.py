class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 1:
            return -1
        if n == 1:
            return 0
        if (nums[0] > nums[1]):
            return 0
        if (nums[n-1] > nums[n-2]):
            return n-1
        lo, hi = 0, n-2
        while(lo <= hi):
            mid = lo + (hi-lo)//2
            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid
            elif nums[mid] < nums[mid+1]:
                lo = mid+1
            else:
                hi = mid-1  
        return -1