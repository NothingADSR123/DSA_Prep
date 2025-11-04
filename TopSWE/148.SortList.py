# 148. Sort List
# Medium
# Given the head of a linked list, return the list after sorting it in ascending order.
# Example 1:
# Input: head = [4,2,1,3]
# Output: [1,2,3,4]
# Example 2:
# Input: head = [-1,5,3,4,0]
# Output: [-1,0,3,4,5]
# Example 3:
# Input: head = []
# Output: []

from typing import Optional,ListNode
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        list1=head
        list2=self.getmid(head)
        tmp=list2.next
        list2.next=None
        list2=tmp
        list1=self.sortList(list1)
        list2=self.sortList(list2)
        return self.merge(list1,list2)

    def getmid(self,head):
        slow=head
        fast=head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow
        
    def merge(self,list1,list2):
        dummy=tail=ListNode()
        while list1 and list2:
            if list1.val<list2.val:
                tail.next=list1
                list1=list1.next 
            elif list1.val>=list2.val:
                tail.next=list2
                list2=list2.next
            tail=tail.next
        if list1:
            tail.next=list1
        if list2:
            tail.next=list2
        return dummy.next
                


