#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(n, leftSize, path, res):
            if n == 0: 
                res.append(path)
                return
            if n > leftSize:
                dfs(n-1, leftSize+1, path + "(", res)
            if(leftSize > 0):
                dfs(n-1, leftSize-1, path + (")"), res)
            
                

        
        res = []
        path = ""
        dfs(2*n, 0, path, res)
        return res
    
# s = Solution()
# res = s.generateParenthesis(3)
# print(res)
# # @lc code=end

