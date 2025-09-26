# 206. Reverse Linked List
# Given the head of a singly linked list, reverse the list, and return the reversed list.
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
# Example 2:
# Input: head = [1,2]
# Output: [2,1]
# Example 3:
# Input: head = []
# Output: []

from typing import ListNode,Optional
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # prev,cur=None,head
        # while cur:
        #     temp=cur.next
        #     cur.next=prev
        #     prev=cur
        #     cur=temp
        # return prev
# THis is a RECURSIVE Approach
        if not head:
            return None
        newHead=head
        if head.next:
            newHead=self.reverseList(head.next)
            head.next.next=head
        head.next=None
        return newHead

