class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        hashSet = set()
        maxC = 1
        l, r = 0, 0

        while r < len(s):
            while s[r] in hashSet:
                hashSet.remove(s[l])
                l += 1

            hashSet.add(s[r])
            maxC = max(maxC, r - l + 1)
            r += 1

        return maxC
