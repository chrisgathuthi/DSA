from heapq import heappush, heappop
from collections import deque


class PriorityQueue:
    def __init__(self) -> None:
        self._elements = []

    def enqueue_with_priority(self, priority, value):
        heappush(self._elements,(-priority,value))#like tuple comparison
    
    def dequeue(self):
        return heappop(self._elements)[1]








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
