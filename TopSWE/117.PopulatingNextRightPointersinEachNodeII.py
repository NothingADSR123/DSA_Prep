# 117. Populating Next Right Pointers in Each Node II
# Given a binary tree
# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
# Initially, all next pointers are set to NULL.
# Example 1:
# Input: root = [1,2,3,4,5,null,7]
# Output: [1,#,2,3,#,4,5,7,#]
# Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
# Example 2:
# Input: root = []
# Output: []

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from typing import Node,deque
class Solution:
    def connect(self, root: 'Node') -> 'Node':

        # BFS SOlved khud se hello 
        if not root:
            return None
        q=deque([root])
        while q:
            prev=None
            for i in range(len(q)):
                node=q.popleft()
                if prev:
                    prev.next=node
                prev=node
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return root

        # BFS with DUMMY head OPTIMAL in memory as well 
# class Solution:
#     def connect(self, root: 'Node') -> 'Node':
#         if not root:
#             return None
        
#         curr = root
#         while curr:
#             dummy = Node(0)  # dummy head for next level
#             tail = dummy     # tail builds links
#             while curr:
#                 if curr.left:
#                     tail.next = curr.left
#                     tail = tail.next
#                 if curr.right:
#                     tail.next = curr.right
#                     tail = tail.next
#                 curr = curr.next
#             curr = dummy.next  # move to next level
#         return root
