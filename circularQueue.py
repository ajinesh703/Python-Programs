class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    def enqueue(self, item):
        if (self.rear + 1) % self.size == self.front:
            print("Queue is Full")
        elif self.front == -1:
            self.front = self.rear = 0
            self.queue[self.rear] = item
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = item
        print(f"Enqueued: {item}")

    def dequeue(self):
        if self.front == -1:
            print("Queue is Empty")
        elif self.front == self.rear:
            temp = self.queue[self.front]
            self.front = self.rear = -1
            return temp
        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            return temp

    def display(self):
        if self.front == -1:
            print("Queue is Empty")
        elif self.rear >= self.front:
            print("Queue:", self.queue[self.front:self.rear + 1])
        else:
            print("Queue:", self.queue[self.front:] + self.queue[:self.rear + 1])

# Example Usage
cq = CircularQueue(5)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
cq.display()
print("Dequeued:", cq.dequeue())
cq.display()
