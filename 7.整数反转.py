#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        s = '' if x >= 0 else '-'
        x = abs(x)
        
        while (x // 10 > 0):
            s += str(x % 10 )
            x = x // 10
    
        s += str(x)
        res = int(s)        
        if res >= -2 ** 31 and res < 2 ** 31 -1:
            return res
        else:
            return 0
s = Solution()
res = s.reverse(-123)
print(res)
# @lc code=end