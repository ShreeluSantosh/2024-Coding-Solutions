class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        c = 0
        for i in nums:
            if i != 0:
                p *= i
            else:
                c += 1
            if c > 1:
                p = 0
                break
        for i in range(len(nums)):
            if c > 1:
                nums[i] = 0
            elif c == 1:
                if nums[i] == 0:
                    nums[i] = p
                else:
                    nums[i] = 0
            else:
                nums[i] = p//nums[i]
        return nums