from heapq import heappush, heappop
from collections import deque
from itertools import count


class IterableMixin:
    def __len__(self):
        return len(self._elements)
    
    def __iter__(self):
        while len(self) > 0:
            yield self.dequeue()

class PriorityQueue(IterableMixin):
    def __init__(self) -> None:
        self._elements = []
        self._counter = count()

    def enqueue_with_priority(self, priority, value):
        element = (-priority,next(self._counter),value)
        heappush(self._elements,element)#like tuple comparison
    
    def dequeue(self):
        return heappop(self._elements)[-1]




# fruits = []

# heappush(fruits,"oranges")
# heappush(fruits,"bananas")
# heappush(fruits,"mangoes")
# heappush(fruits,"apples")
# heappush(fruits,"pear")
# """
# When you tell Python to compare two string objects by value, 
# it starts looking at their characters pairwise from left to right 
# and checks each pair one by one. The character with a lower Unicode 
# code point is considered smaller, which resolves the word order.
# """
# print(fruits)
# heappop(fruits)
# print(fruits)
