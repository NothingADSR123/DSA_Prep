# 230. Kth Smallest Element in a BST
# Mediu
# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
# Example 1
# Input: root = [3,1,4,null,2], k = 1
# Output: 1
# Example 2:
# Input: root = [5,3,6,2,4,null,null,1], k = 3
# Output: 3

from typing import Optional,TreeNode
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Not Optimal
        # self.res=[]
        # def inorder(node):
        #     if not node:
        #         return None
        #     inorder(node.left)
        #     self.res.append(node.val)
        #     inorder(node.right)
        # inorder(root)
        # return self.res[k-1]

        # # Optimal 
        # self.k=k
        # self.ans=None
        # def inorder(node):
        #     if not node :
        #         return None
        #     inorder(node.left)
        #     self.k-=1
        #     if self.k==0:
        #         self.ans=node.val
        #         return self.ans
        #     inorder(node.right)
        # inorder(root)
        # return self.ans

        # One more optimal 
        stack = []
        while True:
            while root:
                stack.append(root)   # push left path
                root = root.left
            root = stack.pop()       # process node
            k -= 1
            if k == 0:
                return root.val
            root = root.right        # now visit right subtree


