from queue import PriorityQueue

class PriorityQueueExample:
  def __init__(self):
    self.queue = PriorityQueue()
    
  def enqueue(self, item):
    self.queue.put(item)
    print(f"Enqueued: {item}")

  def dequeue(self):
    if not self.queue.empty():
      return self.queue.get()
    
    else:
      return "Queue is empty"

  def is_empty(self):
    return self.queue.empty()
  
pq = PriorityQueueExample()
pq.enqueue((2, "Task 2"))
pq.enqueue((1, "Task 1"))
pq.enqueue((3, "Task 3"))

print("Dequeued:", pq.dequeue())
print("Dequeued:", pq.dequeue())

