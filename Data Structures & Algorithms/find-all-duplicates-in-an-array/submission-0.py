class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        counts={}
        res=[]
        for num in nums:
            counts[num]=counts.get(num,0)+1
        
        for key in counts:
            if counts[key]==2:
                res.append(key)
        return res
        

