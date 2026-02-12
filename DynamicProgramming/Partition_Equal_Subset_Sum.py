#Lc Problem Link: https://leetcode.com/problems/partition-equal-subset-sum/description/
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s%2 :
            return False
        n = s//2

        arr = [False] * (n+1)
        arr[0] = True

        for val in nums:
            for i in range(len(arr)-1, val-1, -1):
                if arr[i - val]:
                    arr[i] = True

        return arr[n]
