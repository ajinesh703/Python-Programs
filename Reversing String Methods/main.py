text = "kishan"
reversed_text = ''.join(reversed(text))
print(reversed_text)

# by using loop//

text = "hello"
reversed_text = ""
for i in text:
    reversed_text = i + reversed_text

print(reversed_text)

# by using slicing

text = "python"
reversed_text = text[::-1]
print(reversed_text)

# by using recursion

def reverse_string(text):
    if len(text) == 0:
        return text
    else:
        return reverse_string(text[1:]) + text[0]

text = "hello"
print(reverse_string(text))

# by using stack

text = "hello"
stack = []
for i in text:
    stack.append(i)

reversed_text = ""
while len(stack) > 0:
    reversed_text += stack.pop()

print(reversed_text)

# by using queue

text = "hello"
queue = []
for i in text:
    queue.append(i)

reversed_text = ""
while len(queue) > 0:
    reversed_text += queue.pop(0)

print(reversed_text)

# by using deque

from collections import deque

text = "hello"
deque = deque(text)

reversed_text = ""
while len(deque) > 0:
    reversed_text += deque.pop()

print(reversed_text)

# by using list comprehension

text = "hello"
reversed_text = [text[i] for i in range(len(text)-1, -1, -1)]
print("".join(reversed_text))

# by using reduce

from functools import reduce

text = "hello"
reversed_text = reduce(lambda x, y: y + x, text)
print(reversed_text)

# by using reversed() function

text = "hello"
reversed_text = "".join(reversed(text))
print(reversed_text)

# by using reversed() function

text = "hello"
reversed_text = "".join(reversed(text))
print(reversed_text)

# by using reversed() function

text = "hello"
reversed_text = "".join(reversed(text))
print(reversed_text)
