#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        if(len(nums) < 3):
            return res
        nums.sort()
        for a in range(len(nums)-2):
            if a != 0 and nums[a] == nums[a-1]: continue
            left = a + 1
            right = len(nums) - 1
            while (left < right):
                if (left != a+1 and nums[left] == nums[left-1]):
                    left +=1
                elif (right != len(nums)-1 and nums[right] == nums[right+1]):
                    right -=1
                elif (nums[a] + nums[left] + nums[right] > 0):
                    right -=1
                elif (nums[a] + nums[left] + nums[right] < 0):
                    left +=1
                else:
                    res.append([nums[a], nums[left], nums[right]])
                    left +=1
                    right -=1
        return res


s = Solution()
s.threeSum([-2,0,0,2,2])
# @lc code=end

