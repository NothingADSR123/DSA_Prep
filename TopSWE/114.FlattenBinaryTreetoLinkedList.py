# 114. Flatten Binary Tree to Linked List
# Given the root of a binary tree, flatten the tree into a "linked list":
# The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
# The "linked list" should be in the same order as a pre-order traversal of the binary tree.
# Example 1:
# Input: root = [1,2,5,3,4,null,6]
# Output: [1,null,2,null,3,null,4,null,5,null,6]
# Example 2:
# Input: root = []
# Output: []
# Example 3:
# Input: root = [0]
# Output: [0]

from typing import Optional,TreeNode
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # self.prev= None
        # def helper(node):
        #     if not node : return 
        #     helper(node.right)
        #     helper(node.left)           
        #     node.right=self.prev
        #     node.left=None              #After 6: 6 → None
        #     self.prev=node              # After 5: 5 → 6
        # helper(root)                    # After 4: 4 → 5 → 6
                                        # After 3: 3 → 4 → 5 → 6
                                        # After 2: 2 → 3 → 4 → 5 → 6
                                        # After 1: 1 → 2 → 3 → 4 → 5 → 6
            
        # The other was not O(1) space hence :
        curr=root
        while curr:
            if curr.left:
                prev=curr.left
                while prev.right:
                    prev=prev.right
                prev.right=curr.right              #refer chatgpt or yt whatever
                curr.right=curr.left
                curr.left=None
            curr=curr.right


