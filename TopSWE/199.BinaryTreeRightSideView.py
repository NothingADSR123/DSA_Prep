# 199. Binary Tree Right Side View
# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom. 
# Example 1:
# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]
# Explanation:
# Example 2:
# Input: root = [1,2,3,4,null,null,null,5]
# Output: [1,3,4,5]
# Explanation:
# Example 3:
# Input: root = [1,null,3]
# Output: [1,3]
# Example 4:
# Input: root = []
# Output: []

from typing import Optional,TreeNode,List
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        # There are various ways BFS (right first, left first, last)
        # this was right first where we check with the i==0
        # if not root:
        #     return []
        # res=[]
        # q=deque([root])
        # while q:
        #     for i in range (len(q)):
        #         node=q.popleft()
        #         if i == 0:
        #             res.append(node.val)
        #         if node.right:
        #             q.append(node.right)
        #         if node.left:
        #             q.append(node.left)
        # return res

        # Then there is DFS as always 
        
        res=[]
        def dfs(root,depth):
            if not root :
                return None
            if depth == len(res):
                res.append(root.val)
            dfs(root.right,depth+1)
            dfs(root.left,depth+1)
        dfs(root,0)
        return res