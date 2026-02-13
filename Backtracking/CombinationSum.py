LC Problem link: https://leetcode.com/problems/combination-sum/description/
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        N = len(candidates)
        candidates.sort()
        res=[]

        def backtrack(start,path,sums):
            if sums == target:
                res.append(path[:])
                return
            
            if sums > target:
                return
            
            for i in range(start,N):

                path.append(candidates[i])
                backtrack(i,path,sums+candidates[i])
                path.pop()
            
        backtrack(0,[],0)

        return res
