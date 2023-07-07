#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        res = 0
        while (right > left):
            capacity = (right - left) * min(height[left], height[right])
            # print(f'left[{left}]: {height[left]}, right[{right}]: {height[right]}, capacity: {capacity}')
            res = capacity if capacity > res else res
            if (height[left] > height[right]):
                right -= 1
            else:
                left += 1
        return res
            
            

        

# @lc code=end

