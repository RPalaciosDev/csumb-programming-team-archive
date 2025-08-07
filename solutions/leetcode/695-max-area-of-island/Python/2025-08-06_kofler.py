"""
LINK: https://leetcode.com/problems/max-area-of-island/submissions/1726343575

APPROACH:
(1) Initialize an array to contain the tile that already have been visited.
    Each tile is represented by an integer that corresponds to its placement
    on the grid.
(2) Loop through the grid, row by row; for each element test if the tile is an
    island. If so, call `dfs` on the tile; the function will return the total
    size of the island.
(3) In `dfs` test if the current tile (represented by i and j variables) is out
    of bounds, already visited, or equal to 0 (is water). If that's the case,
    there is nothing to do.
(4) Otherwise, add the current tile to the "already visited" set, and visit the
    four adjacent tiles, calling `dfs` on each.
(5) Lastly, if the current tile is land, increment the current max area count,
    then return the current max area count.
(6) Now, all `dfs` calls are finished for the current island. Test if this max
    size is greater than the max for the whole graph. If so, update it.

NOTES:
Time Complexity
- O(n)

Space Complexity:
- O(n)
"""

from typing import Set

class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        skipped: Set[int] = set()
        max_size = 0
        m = len(grid)
        n = len(grid[0])

        def dfs(i: int, j: int, size: int) -> int:
            idx = (i * n) + j
            if idx in skipped or (i < 0 or i > m - 1 or j < 0 or j > n - 1) or grid[i][j] == 0:
                return size
            skipped.add(idx)

            size = dfs(i + 1, j, size)
            size = dfs(i - 1, j, size)
            size = dfs(i, j + 1, size)
            size = dfs(i, j - 1, size)

            if grid[i][j] == 1:
                size += 1

            return size

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    size = dfs(i, j, 0)
                    max_size = max(max_size, size)

        return max_size
