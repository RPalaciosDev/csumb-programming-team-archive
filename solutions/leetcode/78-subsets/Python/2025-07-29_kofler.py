"""
LINK: https://leetcode.com/problems/subsets/submissions/1716469659

APPROACH:
(1) Initialize a solution list and one that will contain the subsets.
(2) Create a `dfs` function which will be called recursively. Starting with an
    empty `subset` list, it starts at index 0. For the element at index 0,
    there are two possibilities for all future subsets: either the element
    at index 0 is part of the subset, or is not. In the case that it is, it is
    appended to `subset`.
(3) `dfs` is then called again, but at index 1, considering the two
    possibilities. For the "is part of subset" case, the element is appended to
    the list, and `dfs` is called again.
(4) The `index` parameter continues to be incremented, and passed to `dfs`
    recursively. At the top of `dfs`, add a condition, testing if `index` is
    offset past the end of the list. If so, that means that `subset` contains
    a possible subset.
(5) Push the possible subset to the `solution` list. Then, `return`, jumping to
    the previous stack frame. The possibility for "element at index N is in
    subset" has just been considered. Now, consider the possibility that that
    element is not in the subset. Call `pop` on `subset` so this possibility is
    considered. Call `dfs` once more for this case.
(6) Modifying `subset` and calling `dfs` continues to be done until the index
    is past the list on an empty `subset`. Finally, for this last case, append
    the null set to the `answers` array. Execution finally exits from `dfs` and
    answers is returned.

NOTES:
Time Complexity:
- O(n * 2^n)

Space Complexity:
- Linear
"""

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        solution: list[list[int]] = []
        subset: list[int] = []

        def dfs(i: int):
            if i >= len(nums):
                solution.append(list(subset))
                return

            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
            dfs(i + 1)

        dfs(0)        
        return solution
