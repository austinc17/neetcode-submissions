class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        f=''.join(sorted(s))
        g=''.join(sorted(t))
        if g==f:
            return True
        else:
            return False
        