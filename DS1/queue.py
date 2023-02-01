class Queue:
    def __init__(self,queue) -> None:
        self.queue = []
    
    def enqueue(self,elem):
        self.queue.append(elem)
        return f"{elem} add to the queue"

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def __repr__(self) -> str:
        return self.queue

    def size(self):
        return len(self.queue)


