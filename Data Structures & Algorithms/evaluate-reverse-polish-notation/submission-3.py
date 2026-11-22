class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:

            if token.isdigit():

                stack.append(int(token))

            elif token == "+":
                x = stack.pop()
                y = stack.pop()
                stack.append(x+y)
            elif token == "-":
                x = stack.pop()
                y = stack.pop()
                stack.append(x-y)
            elif token == "*":
                print(stack)
                x = stack.pop()
                y = stack.pop()
                stack.append(x*y)
            elif token == "/":
                x = stack.pop()
                y = stack.pop()
                stack.append(x//y)

        return stack[0]
        