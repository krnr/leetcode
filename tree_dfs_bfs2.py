#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
                       11
              8                10
      6             7        .    9
  3       5       .   .
1   2   4   .

DFS: 1 2 3 4 5 6 7 8 9 10 11 (post order)
BFS: 11 8 10 6 7 9 3 5 1 2 4 (level order)
"""
import typing as t
from collections import deque, namedtuple

# Node = namedtuple("Node", "value left right")
class Node(namedtuple("Node", "value left right")):
    def __str__(self):
        return f"{self.value} ({self.left}, {self.right})"
    def postorder(self, visitor):
        if self:
            Node.postorder(self.left, visitor)
            Node.postorder(self.right, visitor)
            visitor(self.value)
    def levelorder(self, visitor, to_visit=None):
        if self:
            visitor(self.value)
            if not to_visit:
                to_visit = []
            to_visit += [self.left, self.right]
        if to_visit:
            Node.levelorder(to_visit[0], visitor, to_visit[1:])


tree = Node(11,
            Node(8,
                 Node(6,
                      Node(3,
                           Node(1, None, None),
                           Node(2, None, None)),
                      Node(5,
                           Node(4, None, None),
                           None)),
                 Node(7, None, None)),
            Node(10, None,
                 Node(9, None, None)))


def dfs(node: Node):
    if node.left:
        yield from dfs(node.left)
    if node.right:
        yield from dfs(node.right)
    yield node.value


def bfs(stack: deque):
    while stack:
        current = stack.popleft()
        if current:
            yield current.value
            stack.extend([current.left, current.right])
        yield from bfs(stack)
        

def spotter(value):
    print(f"I've spotted: {value}")


if __name__ == "__main__":
    print(tree)
    print("dfs: ", "")
    traversed = [val for val in dfs(tree)]
    print(traversed)
    assert traversed == [1,2,3,4,5,6,7,8,9,10,11]

    print("bfs: ", "")
    traversed_b = [val for val in bfs(deque([tree]))]
    print(traversed_b)
    assert traversed_b == [11, 8, 10, 6, 7, 9, 3, 5, 1, 2, 4]

    print("class: ")
    tree.postorder(spotter)
    tree.levelorder(spotter)
