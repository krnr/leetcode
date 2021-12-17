"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:

Input: head = [1,2]
Output: [2,1]

Example 3:

Input: head = []
Output: []

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
"""
from typing import *


class SolutionI:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        new_root = None
        while head:
            current_node, next_node = head, head.next
            current_node.next = new_root
            head = next_node
            new_root = current_node
        return new_root


class SolutionR:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        def reverse(node, prev=None):
            if not node:
                return prev
            new_node = node.next
            node.next = prev
            return reverse(new_node, node)
        def reverse(head)
