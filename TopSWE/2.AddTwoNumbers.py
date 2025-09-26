# 2. Add Two Numbers
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# Example 1:
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:
# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import ListNode
from typing import Optional
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node1=l1
        node2=l2
        dummy=ListNode(0)
        current=dummy
        carry=0
        while node1 or node2 or carry:
            val1 = node1.val if node1 else 0
            val2 = node2.val if node2 else 0
            sum = val1 + val2 + carry
            carry= sum // 10
            digit= sum%10
            current.next= ListNode(digit)

            current=current.next
            node1= node1.next if node1 else None
            node2= node2.next if node2 else None
        return dummy.next