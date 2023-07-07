#
# @lc app=leetcode.cn id=1262 lang=python3
#
# [1262] 可被三整除的最大和
#

# @lc code=start
from typing import List


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        total_sum = 0
        m = [10000] * 3
        
        for num in nums:
            if num % 3 == 1:
                m[2] = min(m[2], m[1] + num)
                m[1] = min(m[1], num)
            elif num % 3 == 2:
                m[1] = min(m[1], m[2] + num)
                m[2] = min(m[2], num)
                
            total_sum += num
        
        m[0] = 0
        bias = total_sum if m[total_sum % 3] == 10000 else m[total_sum % 3]
        
        return total_sum - bias    
s = Solution()
s.maxSumDivThree([3,6,5,1,8])
# @lc code=end

