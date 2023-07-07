#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        for i in range(len(nums)):
            if i <= farthest:
                farthest = max(farthest, i + nums[i])
                if farthest >= len(nums) - 1:
                    return True
        return False
# @lc code=end

