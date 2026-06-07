class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
            # return nums[0] > 0

        target = len(nums) - 1
        i = len(nums) - 2

        while i >= 0:
            if i + nums[i] >= target:
                target = i
            i -= 1

        return target == 0
