"""
===========================================================
    Author:        Roberto Palacios
    Created:       2025-07-21
    Last Updated:  2025-07-21
    Problem:       1046 - Last Stone Weight
    Platform:      LeetCode
    Difficulty:    Easy
    Language:      Python 3
    Tags:          Heap
===========================================================

Description:
--------------------
You are given an array of integers stones where stones[i] is the weight of the ith stone.
On each turn, we choose the two heaviest stones and smash them together.
If the weight of the two stones is equal, they both break, and we remove them from our structure.
If the weight of the two stones is not equal, the stone with the greater weight is destroyed. 
Then the stone with the lesser weight is reduced to the difference of the two stones.
The game continues until there is at most one stone left.
Return the weight of the last remaining stone. If there are no stones left, return 0.

Approach:
___________________
Since we are using Python, we can use the heapq module to implement a max heap.
However, we need to convert the stones to negative values to simulate a 'max heap'.
This is because the heapq module in Python implements a min heap by default.
We can then pop the two heaviest stones and smash them together.
If the weight of the two stones is equal, they both break, and we remove them from our 'max heap'.
If the weight of the two stones is not equal, the stone with the greater weight is destroyed.
Then the stone with the lesser weight is reduced to the difference of the two stones.
We can then push the new stone back into our 'max heap'.
We can continue this process until there is at most one stone left.
"""

import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        max_heap = [-s for s in stones]                         # Convert stones to negative values
        heapq.heapify(max_heap)                                 # Convert to max heap

        while len(max_heap) > 1:                                # While there are at least two stones
            first = -heapq.heappop(max_heap)                    # Pop the heaviest stone
            second = -heapq.heappop(max_heap)                   # Pop the second heaviest stone

            if first != second:                                 # If the stones are not equal
                heapq.heappush(max_heap, -(first - second))     # Push the difference back into the heap

        if max_heap:                                            # If there is one stone left
            return -max_heap[0]                                 # Return the weight of the last stone
        else:                                                   # If there are no stones left
            return 0                                            # Return 0