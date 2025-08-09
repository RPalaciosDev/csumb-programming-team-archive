"""
LINK: https://leetcode.com/problems/clone-graph/submissions/1729441515

APPROACH:
(1) First, construct a `visited` dict with integer keys that represent a
    unique node in the tree and values that are the new copied Node object.
(2) Create a `dfs` function that is called on every Node in the tree. First,
    it checks if the node has already been copied before (by a lookup in
    `visited`). If so it returns that Node.
(3) Otherwise, a copy of the existing Node must be done. Perform a copy,
    supplying the known values to the constructor (`val`). Then, call `dfs` on
    each neighbor of the current Node. `dfs` always returns a copied node, so
    append the result of each call to the `.neighbors` property. This current
    node is now fully copied.
(4) Lastly, return the copied node (in `dfs()`).

NOTES:
Time Complexity:
- O(n)

Space Complexity:
- O(n)
"""

from typing import Optional, Mapping

class Node:
    def __init__(self, val: int = 0, neighbors: None | list['Node'] = None): pass
    val: int
    neighbors: list['Node']

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        visited: Mapping[int, Node] = {}

        def dfs(node: Node) -> Node:
            if node.val in visited:
                return visited[node.val]

            copy = Node(node.val)
            visited[node.val] = copy

            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy

        return dfs(node)
