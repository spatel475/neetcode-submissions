class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        countS = {}

        for i, v in enumerate(nums):
            if target - v in countS:
                return [countS[target - v], i]
            countS[v] = i
        return []
