"""
===========================================================
    Author:        Roberto Palacios
    Created:       2025-07-21
    Last Updated:  2025-07-21
    Problem:       703 - Kth Largest Element in a Stream
    Platform:      LeetCode
    Difficulty:    Easy
    Language:      Python 3
    Tags:          Heap
===========================================================

Description:
--------------------
Design a class to find the kth largest element in a stream.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
Implement the KthLargest class:
- KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
- int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.

Approach:
___________________
We can use a min heap to keep track of the k largest elements.
If the size of the heap exceeds k, we can pop the smallest elements until the size of the heap is k.
When adding a new element, we can push the new element into the heap if there is space.
If the new element is larger than the smallest element in the heap, we can replace the smallest element.
Otherwise, we can ignore the new element.
We can then return the smallest element.
"""

import heapq
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]): 
        self.k = k                                  # k is the number of top elements

        self.heap = nums                              # copy nums list and (min)heapify
        heapq.heapify(self.heap)

        while len(self.heap) > k:                     # if the size of the heap exceeds k, pop min element
            heapq.heappop(self.heap)
            
    def add(self, val: int) -> int:
        if len(self.heap) < self.k:                  # If there is room in the heap
            heapq.heappush(self.heap, val)

        elif val > self.heap[0]:                      # otherwise if the added value is larger than the minimum, replace it
            heapq.heapreplace(self.heap, val)

        return self.heap[0]                           # return the smallest element