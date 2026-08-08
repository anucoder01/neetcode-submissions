class MinStack:

    def __init__(self):
        # Normal stack stores all values
        self.stack = []

        # Min stack stores the minimum value
        # at each position
        self.minStack = []

    def push(self, val):

        self.stack.append(val)

        # If minStack is empty, val is the minimum
        # Otherwise, store the smaller of val and current minimum
        if not self.minStack:
            self.minStack.append(val)
        else:
            self.minStack.append(
                min(val, self.minStack[-1])
            )

    def pop(self):

        # Remove from both stacks
        self.stack.pop()
        self.minStack.pop()

    def top(self):

        # Return top element
        return self.stack[-1]

    def getMin(self):

        # Top of minStack is always the minimum
        return self.minStack[-1]