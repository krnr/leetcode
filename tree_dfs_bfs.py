#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
                    11
           8                10
      6         7              9
  3       5
1   2   4

DFS: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 (post-order)
BFS: 11, 8, 10, 6, 7, 9, 3, 5, 1, 2, 4 (level-order)
"""
import typing as t
from collections import deque, namedtuple

class Node(namedtuple("Node", "value left right")):
    pass


tree = Node(11,
            Node(8,
                 Node(6,
                      Node(3,
                           Node(1, None, None),
                           Node(2, None, None)),
                      Node(5, 
                           Node(4, None, None),
                           None),
                      ),
                 Node(7, None, None)),
            Node(10, None,
                 Node(9, None, None)))


def dfs(node: Node):
    if node.left:
        yield from dfs(node.left)
    if node.right:
        yield from dfs(node.right)
    yield node.value


def bfs(to_visit: deque):
    while to_visit:
        current = to_visit.popleft()
        if current:
            yield current.value
            to_visit.extend([current.left, current.right])
        yield from bfs(to_visit)
        
        
if __name__ == "__main__":
    print("dfs: ") 
    result = [val for val in dfs(tree)]
    print(result)
    print("bfs: ") 
    result = [val for val in bfs(deque([tree]))]
    print(result)
