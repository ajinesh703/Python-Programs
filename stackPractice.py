def evaluate_postfix(expression):
  stack = []
  
  for char in expression:
    if char.isdigit():
      stack.append(int(char))

    else:
      val2 = stack.pop()
      val1 = stack.pop()
      
      if char == '+':
        stack.append(val1 + val2)

      elif char == '-':
        stack.append(val1 - val2)

      elif char == '*':
        stack.append(val1 * val2)

      elif char == '/':
        stack.append(int(val1 / val2))

  return stack[0]

expression = "231*+9-"
print(evaluate_postfix(expression))

