class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n

        arr = [0] * (n + 1)
        arr[1] = 1
        arr[2] = 2

        for a in range(3, len(arr)):
            arr[a] = arr[a - 1] + arr[a - 2]

        return arr[n]