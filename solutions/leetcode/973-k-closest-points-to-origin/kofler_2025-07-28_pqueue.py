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
            answer.append(list(point)) # Use list() to satisfy type checker.
        return answer
