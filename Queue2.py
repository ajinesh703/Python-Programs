from collections import deque

class Queue:
  def __init__(self):
    self.queue = deque()
    
  def enqueue(self, item):
    self.queue.append(item)
    print(f"Enqueued: {item}")

  def dequeue(self):
    if not self.is_empty():
      return self.queue.popleft()
    else:
      return "Queue is empty"

  def is_empty(self):
    return len(self.queue) == 0
  
  def front(self):
    if not self.is_empty():
      return self.queue[0]
    
    else:
      return "Queue is empty"

  def display(self):
    print("Queue:", list(self.queue))

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.display()

print("Dequeued:", q.dequeue())

q.display()


    
    