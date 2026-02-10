# Problem link: https://leetcode.com/problems/predict-the-winner/description/
class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        N = len(nums)

        if N%2==0 or N==1:
            return True

        memo = {}
        def score(left, right):
            if left>right:
                return 0
            
            if (left,right) in memo:
                return memo[(left,right)]
            
            score_left = nums[left] - score(left+1,right)
            score_right = nums[right] - score(left,right-1)

            memo[(left,right)] = max(score_left,score_right)
            return memo[(left,right)]
        
        return score(0,N-1) >= 0


        
