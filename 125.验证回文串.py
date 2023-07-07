#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0 :
            return False
        s = "".join(x.lower() for x in s if x.isalnum())
        print(s)
        l = 0
        r = len(s) - 1
        while(l < r):
            if(s[l] != s[r]):
                return False
            l += 1
            r -= 1
        return True
# @lc code=end

