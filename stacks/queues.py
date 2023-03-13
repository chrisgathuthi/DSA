from collections import deque

class Queue:
    def __init__(self,*element) -> None:
        self._elements = deque(element)#initial arguments 
        
    def __len__(self):
        return len(self._elements)


    def __iter__(self):
        while len(self._elements) > 0:
            yield self.dequeue()#it will lazy delete element when you loop 


    def enqueue(self,element):
        self._elements.append(element)
    
    def dequeue(self):
        return self._elements.popleft()

class Stack(Queue):
    def dequeue(self):
        return self._elements.pop()#it will pop the last index descending to 0

