#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        for i in range(len(strs[0])):
            tmp = None
            flag = True
            for j in range(len(strs)):
                if tmp is None:
                    tmp = strs[j][i]
                elif len(strs[j]) <= i or tmp != strs[j][i] :
                    flag = False
                    break
            if flag:
                res += tmp
            else:
                break
        return res 


s = Solution()
s.longestCommonPrefix([""])
# @lc code=end

