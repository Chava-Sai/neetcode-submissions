class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:

            try:
                stack.append(int(token))
            except ValueError:
                pass 

            if token == "+":
                x = stack.pop()
                y = stack.pop()
                stack.append(x+y)
            elif token == "-":
                x = stack.pop()
                y = stack.pop()
                stack.append(x-y)
            elif token == "*":
                x = stack.pop()
                y = stack.pop()
                stack.append(x*y)
            elif token == "/":
                x = stack.pop()
                y = stack.pop()
                stack.append(x//y)

        return stack[0]
        