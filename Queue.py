class Queue:
  def __init__(self):
    self.queue = []
    
  def enqueue(self, item):
    self.queue.append(item)
    print(f"Enqueued: {item}")

  def dequeue(self):
    if not self.is_empty():
      return self.dequeue.pop(0)

    else:
      return "Queue is empty"

  def is_empty(self):
    return len(self.queue) == 0
  
  def front(self):
    return len(self.queue) == 0
  
  def is_empty(self):
    return len(self.queue) == 0
  
  def front(self):
    if not self.is_empty():
      return self.queue[0]

    else:
      return "Queue is empty"

  def display(self):
    print("Queue:", self.queue)

q = Queue()
q.enqueue(90)
q.enqueue(80)
q.enqueue(54)
q.display()

print("Dequeued:", q.dequeue())

q.display()