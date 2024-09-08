class QueueUsingStacks:
  def __init__(self):
    self.stack1 = []
    self.stack2 = []

  def enqueue(self, item):
    self.stack1.append(item)
    print(f"Enqueued: {item}")

  def dequeue(self):
    if not self.stack2:
      while self.stack1:
        self.stack2.append(self.stack1.pop())

    if not self.stack2:
      return "Queue is empty"
    return self.stack2.pop()
  
  def display(self):
    if not self.stack2:
      print("Queue:", self.stack1)

    else:
      print("Queue:", list(reversed(self.stack2)) + self.stack1)

qs = QueueUsingStacks()
qs.enqueue(1)
qs.enqueue(2)
qs.enqueue(3)
qs.display()

print("Dequeued:", qs.dequeue())
qs.display()