class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        res = nums[0]

        while l <= r:
            # array sorted already
            if nums[l] < nums[r]:
                res = min(nums[l], res)
                break

            center = (l + r) // 2
            res = min(nums[center], res)

            if nums[l] <= nums[center]:  # left less than center: right side has rotation
                l = center + 1
            else:  # left greater than center: left side has rotation
                r = center - 1

        return res
