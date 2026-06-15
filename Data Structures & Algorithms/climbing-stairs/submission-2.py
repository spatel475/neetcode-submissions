class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n

        secondLast, last = 2, 3

        for _ in range(4, n + 1):
            secondLast, last = last, last + secondLast

        return last
