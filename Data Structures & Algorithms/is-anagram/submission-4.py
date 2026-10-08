class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        f=sorted(s)
        d=sorted(t)
        if f==d:
            return True
        else:
            return False
        