# 21. Merge Two Sorted Lists
# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.
# Example 1:
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:
# Input: list1 = [], list2 = []
# Output: []
# Example 3:
# Input: list1 = [], list2 = [0]
# Output: [0]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import ListNode, Optional
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node1,node2=list1,list2
        dummy=ListNode()
        cur=dummy
        while node1 and node2:
            if node1.val <= node2.val:
                cur.next=node1
                node1=node1.next
            else:
                cur.next=node2
                node2=node2.next
            cur=cur.next
        if node1:
            cur.next=node1
        else:
            cur.next=node2
        return dummy.next
    
            