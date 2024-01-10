class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zc = 0
        lw = 0
        s = 0
        for i in range(len(nums)):
            zc += (nums[i] == 0)
            while(zc > 1):
                zc -= (nums[s] == 0)
                s += 1
            lw = max(lw, i-s)
        return lw