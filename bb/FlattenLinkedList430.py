"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        stack = []
        node = head

        def add_child(node):
            if node.next:
                stack.append(node.next)
            if node.child:
                stack.append(node.child)
        if node:
            add_child(node)
        else:
            return node

        while stack:
            node.child = None
            nextNode = stack.pop()
            node.next = nextNode
            nextNode.prev = node
            node = node.next
            add_child(node)

        return head

