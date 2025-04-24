from typing import List, Optional


class Node:
    def __init__(self, val: int = 0, neighbors: Optional[List['Node']] = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        nodes: dict[int, Node] = {}
        stack = [node]
        while len(stack) > 0:
            curr = stack.pop()
            if curr.val in nodes:
                continue
            nodes[curr.val] = Node(curr.val, curr.neighbors)

            stack += curr.neighbors

        for _, n in nodes.items():
            n.neighbors = [nodes[curr.val] for curr in n.neighbors]

        return nodes[node.val]
