#
# @lc app=leetcode.cn id=86 lang=python3
#
# [86] 分隔链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        small_now = ListNode()
        small_head = small_now
        large_now = ListNode()
        large_head = large_now
    
        now = head
        while now is not None:
            if now.val < x:
                small_now.next = now
                small_now = small_now.next
            if now.val >= x:
                large_now.next = now
                large_now = large_now.next
            now = now.next    
        
        large_now.next = None
        small_now.next = large_head.next
        return small_head.next
# @lc code=end

