from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        storage = {}

        def dfs(node):
            if node in storage:
                return storage[node]

            copy = Node(node.val)
            storage[node] = copy
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy

        return dfs(node)


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

n1.neighbors += [n2, n4]
n2.neighbors += [n1, n3]
n3.neighbors += [n2, n4]
n4.neighbors += [n1, n3]

print(Solution().cloneGraph(n1))
