#
# @lc app=leetcode.cn id=97 lang=python3
#
# [97] 交错字符串
#

# @lc code=start
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        n1 = len(s1)
        n2 = len(s2)
        n3 = len(s3)
        if n1 == 0 and n2 == 0 and n3 == 0: return True
        if n1+n2 != n3: return False
        
        dp = [[False] * (n2 + 1) for i in range(n1 + 1)]
        for i in range(n1 + 1):
            for j in range(n2 + 1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                if i - 1 >= 0 and dp[i-1][j] == True and s1[i - 1] == s3[i + j - 1]:
                    dp [i][j] = True
                elif j - 1 >= 0 and dp[i][j-1] == True and s2[j - 1] == s3[i + j - 1]:
                    dp [i][j] = True
        
        
        return dp[n1][n2]
                    
                    
                
# @lc code=end

