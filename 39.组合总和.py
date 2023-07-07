#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
from typing import List


class Solution:
    # def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    #     res = []
    #     for i in range(len(candidates)):
    #         self.search(candidates, target, i, 0, [], res)
    #     return res
    
    # def search(self, candidates, target, x, now, path, res):
    #     path.append(candidates[x])
    #     plus = now + candidates[x]
    #     if (plus == target):
    #         res.append([a for a in path])
    #     elif (plus > target):
    #         pass
    #     else:
    #         for i in range(x, len(candidates)):
    #             self.search(candidates, target, i, plus, path, res)
    #     del path[len(path)-1]
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(candidates, target, x, path, res):
            if (target < 0):
                return 
            if (target == 0):
                res.append(path)
                return
            for i in range(x, len(candidates)):
                dfs(candidates, target-candidates[i], i, path + [candidates[i]], res)
        size = len(candidates)
        if size == 0:
            return []
        path = []
        res = []
        dfs(candidates, target, 0, path, res)
        return res

# @lc code=end

