class Solution:
    def evalRPN(self, tokens):

        stack = []

        for token in tokens:

            # If token is a number, push it onto the stack
            if token not in "+-*/":
                stack.append(int(token))

            else:
                # Pop the two operands
                b = stack.pop()
                a = stack.pop()

                # Perform the operation
                if token == "+":
                    stack.append(a + b)

                elif token == "-":
                    stack.append(a - b)

                elif token == "*":
                    stack.append(a * b)

                elif token == "/":
                    # int() truncates toward zero
                    stack.append(int(a / b))

        # Final result
        return stack[-1]