LC problem link: https://leetcode.com/problems/subsets/description/
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        res = []
        path = []
        def backtrack(idx):
            res.append(path[:])
            for i in range(idx,N):
                path.append(nums[i])
                backtrack(i+1)
                path.pop()
        backtrack(0)

        return res



