class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:

            if token.isdigit():

                stack.append(int(token))

            if token == "+":
                x = stack.pop()
                y = stack.pop()
                stack.append(x+y)
            if token == "-":
                x = stack.pop()
                y = stack.pop()
                stack.append(x-y)
            if token == "*":
                x = stack.pop()
                y = stack.pop()
                stack.append(x*y)
            if token == "/":
                x = stack.pop()
                y = stack.pop()
                stack.append(x//y)

        return stack[0]
        