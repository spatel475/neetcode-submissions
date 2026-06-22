class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def doMath(t):
            if t == "+":
                return stack.pop() + stack.pop()
            if t == "*":
                return stack.pop() * stack.pop()
            if t == "-":
                n1, n2 = stack.pop(), stack.pop()
                return n2 - n1
            if t == "/":
                n1, n2 = stack.pop(), stack.pop()
                return int(float(n2) / n1)

        stack = []
        for t in tokens:
            if t in ["+", "-", "*", "/"]:
                stack.append(doMath(t))
            else:
                stack.append(int(t))

        return int(stack.pop())
