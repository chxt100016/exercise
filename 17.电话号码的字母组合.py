#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if (len(digits) == 0):
            return []
    
        data = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        dp = [[]] * len(digits)
        dp[0] = data[digits[0]]
        
        
        for i in range(1, len(digits)):
            arr = data[digits[i]]
            
            dp[i] = [a + b 
                     for a in dp[i-1]
                     for b in arr 
                     ]
        return dp[len(digits) - 1]
        
# @lc code=end

