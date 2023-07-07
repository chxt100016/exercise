#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] N 字形变换
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2: return s
        resArr = ['' for i in range(numRows)]
        index = 0
        flag = 1
        for i in range(len(s)):
            resArr[index] += s[i]
            
            if i != 0 and index % (numRows-1) == 0:
                flag *= -1
            index = index + flag
        
        return "".join(resArr)
    
s = Solution()
res = s.convert(s='AB', numRows=1)
print(res)
            
            
        
# @lc code=end

