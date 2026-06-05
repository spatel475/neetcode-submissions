class Solution:
    def encode(self, strs: List[str]) -> str:
        x = ""
        for s in strs:
            x += str(len(s)) + "#" + s
        return x

    def decode(self, s: str) -> List[str]:
        words = []
        i = 0

        while i < len(s):
            j = i  # j = delimiter index

            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            wordStart = j + 1
            wordEnd = wordStart + length
            words.append(s[wordStart:wordEnd])
            i = wordEnd
        return words
