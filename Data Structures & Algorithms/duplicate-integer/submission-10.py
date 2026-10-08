class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        f=set(nums)
        if len(f)<len(nums):
            return True
        else:
            return False
        