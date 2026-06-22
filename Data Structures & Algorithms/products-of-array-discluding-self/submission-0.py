class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        [1, 1, 2, 8]
        [48,24,6,1]

        [48, 24, 12, 8]
        """

        N = len(nums)
        prefix = [0] * N
        suffix = [0] * N
        result = [0] * N
        prefix[0] = 1
        suffix[-1] = 1

        for i in range(1, N):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        for i in range(N - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        for i in range(N):
            result[i] = prefix[i] * suffix[i]

        return result
