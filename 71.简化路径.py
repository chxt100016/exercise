#
# @lc app=leetcode.cn id=71 lang=python3
#
# [71] 简化路径
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        arr = path.split("/")
        res = []
        for item in arr:
            if '.' == item:
                continue
            elif '' == item:
                continue
            elif '..' == item:
                if res : res.pop()
            else:
                res.append(item)
        return "/" + "/".join(res)
                
            
            
            
        
# @lc code=end

