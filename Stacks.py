# Stacks

# ----- LIFO Stack:

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        self.stack.pop()

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return self.size() == 0

    def __str__(self):
        return str(self.stack)

    def peek(self):
        return self.stack[-1]

    def __eq__(self, other):
        return self.stack == other.stack

s1 = Stack()
s1.push(2)
s1.push(3)
print(s1)

