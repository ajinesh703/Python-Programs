def is_balanced(expression):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
    
    return len(stack) == 0

# Example usage
expression = "{[()]}"
print(is_balanced(expression))  # Output: True

expression = "{[(])}"
print(is_balanced(expression))  # Output: False
