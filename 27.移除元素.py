#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0
        quick = 0
        while(quick < len(nums)):
            if(nums[quick] != val):
                nums[slow] = nums[quick]
                slow +=1
            quick +=1
        return slow
            
# @lc code=end

