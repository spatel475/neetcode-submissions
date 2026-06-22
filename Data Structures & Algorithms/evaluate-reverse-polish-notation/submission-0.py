class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def doMath(t):
            if t == "+":
                return int(stack.pop()) + int(stack.pop())
            if t == "*":
                return int(stack.pop()) * int(stack.pop())
            if t == "-":
                n1, n2 = int(stack.pop()), int(stack.pop())
                return n2 - n1
            if t == "/":
                n1, n2 = int(stack.pop()), int(stack.pop())
                return n2 / n1

        stack = []
        for t in tokens:
            if t in ["+", "-", "*", "/"]:
                stack.append(doMath(t))
            else:
                stack.append(t)

        return int(stack.pop())
