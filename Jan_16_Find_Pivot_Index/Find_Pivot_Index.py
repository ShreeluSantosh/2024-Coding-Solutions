class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftsum = 0
        rightsum = 0
        for i in nums:
            rightsum += i
        for i in range(len(nums)):
            rightsum -= nums[i]
            if leftsum == rightsum:
                return i
            leftsum += nums[i]
        return -1