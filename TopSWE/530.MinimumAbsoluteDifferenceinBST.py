# 530. Minimum Absolute Difference in BST
# Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.
# Example 1:
# Input: root = [4,2,6,1,3]
# Output: 1
# Example 2
# Input: root = [1,0,48,null,null,12,49]
# Output: 1

from typing import TreeNode,Optional
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.mindiff=float('inf')
        self.prev=None
        def inorder(node):
            if not node:
                return None
            inorder(node.left)
            if self.prev != None :
                self.mindiff= min(self.mindiff,(node.val-self.prev.val))
            self.prev=node
            inorder(node.right)
        inorder(root)
        return self.mindiff
        

