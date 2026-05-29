class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # key = number, value = frequency of number
        freq = {}

        for n in nums:
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1

        buckets = [[] for _ in range(len(nums) + 1)]
        for key, val in freq.items():
            buckets[val].append(key)

        result = []

        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
            if len(result) == k:
                return result

        return result
