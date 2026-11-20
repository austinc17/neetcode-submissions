class Solution:
    def countSeniors(self, details: List[str]) -> int:
        isolated = []
        for s in details:
            isolated.append(int(s[11:13]))
        
        count=0
        for age in isolated:
            if age>60:
                count+=1
        
        return count
        
        
        