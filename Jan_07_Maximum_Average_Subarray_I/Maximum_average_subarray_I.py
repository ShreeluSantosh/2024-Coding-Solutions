class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans = sum(nums[:k])
        w = ans
        for i in range(1,len(nums)-k+1):            
            w = w - nums[i-1] + nums[i+k-1]
            ans = max(w , ans)
        return ans/k