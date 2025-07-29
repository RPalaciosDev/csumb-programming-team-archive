"""
LINK: https://leetcode.com/problems/last-stone-weight/submissions/1713815716

APPROACH:
(1) Construct a new array (`weights`) where each index corresponds to a weight
    value; each corresponding value corresponds to its frequency
(2) Initialize i, the right pointer. Iterate through weights from end to
    start. If value is even, those stones are cancelled out. If it's odd, then
    the next-smallest weight must be found.
(3) Initialize j, the left pointer, to find this next-smallest weight. Iterate
    leftward until array ends or a weight with a non-zero frequency is found.
    If array ends, then we know the weight at j represents the last stone left.
(4) If array does not end, then the stones are collided, performing the
    necessary value adjustments in `weights`. After, set i for next iteration.

NOTES:
Time Complexity:
- Note the line that includes the `max()`. Since the next value of i is not
  always set to j, the complexity is worse than O(n). However, I don't think
  it's quite O(n^2). Performance decreases when frequencies of weights are
  quite sparse and shaped like a bi-modal distribution.

Space Complexity:
- Constant
"""


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        weights = [0] * 1_001
        for stone in stones:
            weights[stone] += 1

        new_stone = 0
        i = len(weights) - 1
        while i >= 0:
            freq = weights[i]
            if freq % 2 == 0:
                if freq > 0:
                    new_stone = 0
                i -= 1
                continue

            j = i - 1
            while j >= 0 and weights[j] == 0:
                j -= 1
            if j == -1:
                return i

            new_stone = i - j
            weights[j] -= 1
            weights[new_stone] += 1
            i = max(j, new_stone)

        return new_stone
