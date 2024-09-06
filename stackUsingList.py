# Stack implementation using Python list
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

# Example usage
s = Stack()
s.push(10)
s.push(20)
s.push(30)
print(s.pop())  # Output: 30
print(s.peek()) # Output: 20
