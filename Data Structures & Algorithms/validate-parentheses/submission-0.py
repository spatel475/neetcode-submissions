class Solution:
    def isValid(self, s: str) -> bool:

        dict = {")": "(", "]": "[", "}": "{"}

        stack = []

        for x in s:
            if x in dict.values():
                stack.append(x)
            else:
                if len(stack) == 0:
                    return False

                stackTopMatch = stack.pop() == dict[x]
                if not stackTopMatch:
                    return False

        return len(stack) == 0
