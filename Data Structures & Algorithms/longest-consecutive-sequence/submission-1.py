class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxCount = 0

        for i in nums:
            counter = 1
            num = i
            while num - 1 in nums:
                counter += 1
                num -= 1
            maxCount = max(maxCount, counter)

        return maxCount
