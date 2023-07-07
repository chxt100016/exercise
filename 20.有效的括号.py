#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        if s is None: return False
        answer = None
        for char in s:
            if answer is None:
                if char == '(':
                    answer = ')'
                elif char == '{':
                    answer = '}'
                elif char == '[':
                    answer = ']'
            
            elif char == answer:
                answer = None
            else:
                return False
            
        return answer is None

s = Solution()
s.isValid('()')
# @lc code=end

