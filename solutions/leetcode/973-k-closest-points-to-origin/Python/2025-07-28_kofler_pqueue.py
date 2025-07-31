"""
LINK: https://leetcode.com/problems/k-closest-points-to-origin/submissions/1715199479

APPROACH:
(1) Make a list, which will be used as a heap queue to store distances of
    points to the origin
(2) Loop through `points`: for each point, calculate its distance and append
    the distance-point pair to the array as a tuple.
(3) "heapify" the list. This is faster than using heapq to incrementally add
    new pairs
(3) Pick and return first k points in the list, which are the k closest points
    to the origin.

NOTES:
Time Complexity:
- Linear

Space Complexity:
- Linear
"""

import heapq
from typing import Tuple

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        nearest_points: list[Tuple[int, Tuple[int, int]]] = []
        for x, y in points:
            distance = (x ** 2) + (y ** 2)
            nearest_points.append((distance, (x, y)))
        heapq.heapify(nearest_points)

        answer: list[list[int]] = []
        for _ in range(k):
            _, point = heapq.heappop(nearest_points)
            # Use list() to satisfy type checker at the cost of performance.
            answer.append(list(point))
        return answer
