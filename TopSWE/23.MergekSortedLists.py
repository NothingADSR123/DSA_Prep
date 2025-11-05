# 23. Merge k Sorted Lists
# Hard
# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
# Merge all the linked-lists into one sorted linked-list and return it.
# Example 1:
# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted linked list:
# 1->1->2->3->4->4->5->6
# Example 2:
# Inpt: lists = []
# Output: []
# Example 3:
# Input: lists = [[]]
# Output: []
 
from typing import List, Optional, ListNode
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Not that hard just writing out the coding part was the main thing
        if not lists or len(lists)==0:
            return None
        while len(lists)>1:
            final=[]
            for i in range(0,len(lists),2):
                list1=lists[i] 
                list2=lists[i+1] if i+1<len(lists) else None
                final.append(self.mergefun(list1,list2))
            lists=final
        return lists[0]

    def mergefun(self,l1,l2):
        dummy=tail=ListNode()
        while l1 and l2:
            if l1.val<l2.val:
                tail.next=l1
                l1=l1.next
            else:
                tail.next=l2
                l2=l2.next
            tail=tail.next
        if l1:
            tail.next=l1
        if l2:
            tail.next=l2
        return dummy.next
