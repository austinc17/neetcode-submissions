class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        g=''.join(sorted(s))
        f=''.join(sorted(t))
        if g==f:
            return True
        elif g!=f:
            return False
        