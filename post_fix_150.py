class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        operators = {"+", "-", "*", "/"}

        for token in tokens:
            if token not in operators:
                stack.append(int(token))
                continue

            right = stack.pop()
            left = stack.pop()

            if token == "+":
                stack.append(left + right)
            elif token == "-":
                stack.append(left - right)
            elif token == "*":
                stack.append(left * right)
            else:
                quotient = abs(left) // abs(right)
                if (left < 0) != (right < 0):
                    quotient = -quotient
                stack.append(quotient)

        return stack[-1]
       