# 106. Construct Binary Tree from Inorder and Postorder Traversal
# Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.
# Example 1:
# Inut: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
# Output: [3,9,20,null,null,15,7]
# Example 2:
# Input: inorder = [-1], postorder = [-1]
# Output: [-1]

# THIS IS NOT THE MOST OPTIMAL APPROACH IT IS IN O(N²)

from typing import Optional,TreeNode,List
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not postorder or not inorder:
            return None 
        root=TreeNode(postorder[-1])
        mid=inorder.index(postorder[-1])
        root.right=self.buildTree(inorder[mid+1:],postorder[mid:-1])
        root.left=self.buildTree(inorder[:mid],postorder[:mid])
        return root