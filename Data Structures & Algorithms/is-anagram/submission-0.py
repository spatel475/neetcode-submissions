class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s)) != len(t):
            return False

        charMapS = {}
        charMapT = {}

        for x in s:
            if x in charMapS:
                charMapS[x] += 1
            else:
                charMapS[x] = 1

        for x in t:
            if x in charMapT:
                charMapT[x] += 1
            else:
                charMapT[x] = 1

        return charMapS == charMapT
