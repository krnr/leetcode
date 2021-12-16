"""
You are given a perfect binary tree where all leaves are on the same level, and
every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next
right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.


Example 1:

Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function
should populate each next pointer to point to its next right node, just like in
Figure B. The serialized output is in level order as connected by the next
pointers, with '#' signifying the end of each level.

Example 2:

Input: root = []
Output: []

Constraints:

The number of nodes in the tree is in the range [0, 2^12 - 1].
-1000 <= Node.val <= 1000

Follow-up:

You may only use constant extra space.
The recursive approach is fine. You may assume implicit stack space does not
count as extra space for this problem.

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
import collections


class SolutionA:
    def connect(self, root: "Optional[Node]") -> "Optional[Node]":
        if not root:
            return root

        next_level = collections.deque()
        next_level.append(root)

        def traverse(this_level):
            next_level = collections.deque()
            current_node = this_level.popleft()
            if current_node.left:
                next_level.append(current_node.left)
                next_level.append(current_node.right)
            while this_level:
                node = this_level.popleft()
                if node.left:
                    next_level.append(node.left)
                    next_level.append(node.right)
                current_node.next = node
                current_node = node
            if next_level:
                return traverse(next_level)

        traverse(next_level)
        return root


class SolutionB:
    def connect(self, root: "Optional[Node]") -> "Optional[Node]":
        def traverse(current_node, next_node):
            if not current_node:
                return current_node
            current_node.next = next_node
            traverse(current_node.left, current_node.right)
            if next_node:
                traverse(current_node.right, next_node.left)
            else:
                traverse(current_node.right, None)

        traverse(root, None)
        return root


class SolutionC:
    def connect(self, root: "Optional[Node]") -> "Optional[Node]":
        curr = root
        while curr and curr.left:
            next_level = curr.left
            while curr:
                curr.left.next = curr.right
                curr.right.next = curr.next.left if curr.next else None
                curr = curr.next
            curr = next_level
        return root
