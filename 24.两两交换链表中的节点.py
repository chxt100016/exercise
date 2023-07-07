#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
from ast import List
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head is None or head.next is None):
            return head
        
        tail = head
        head = head.next
        tail.next = self.swapPairs(head.next)
        head.next = tail
        return head
            

s = Solution()
e = ListNode(5)
d = ListNode(4, e)
c = ListNode(3, d)
b = ListNode(2, c)
a = ListNode(1, b)

res = s.swapPairs(a)
while res is not None:
    print(res.val)
    res = res.next

            
            
            
        
        

# @lc code=end

