#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#

# @lc code=start
# Definition for singly-linked list.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        first = head if left > 1 else None
        pre = None
        left_node = None
        right_node = None
        tail = None
        
        n = 1
        now = head
        inner_tail = None
        while n <= right and now is not None:
            
            if n + 1 == left:
                pre = now
            if n == left:
                left_node = now
            if n == right:
                right_node = now
                tail = now.next
                
            tmp = now
            now = now.next
            if n >= left and n <= right:
                tmp.next = inner_tail
                inner_tail = tmp
                
                
            n +=1
            
        if first and pre:
            pre.next = right_node
        
        if left_node: 
            left_node.next = tail

        return first if first else right_node


a = ListNode(1, None)
print(a.next)
        
# @lc code=end

