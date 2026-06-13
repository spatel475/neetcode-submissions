class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l, r = 0, len(numbers) - 1

        while l < r:
            if target - numbers[r] == numbers[l]:
                return [l + 1, r + 1]
            if target - numbers[r] < numbers[l]:
                r -= 1
            else:
                l += 1

        return [l + 1, r + 1]
