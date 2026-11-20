class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        streak=0
        best=0
        
        for num in nums:
            if num==1:
                streak+=1
                best=max(best,streak)
            else:
                streak=0
        return best



        