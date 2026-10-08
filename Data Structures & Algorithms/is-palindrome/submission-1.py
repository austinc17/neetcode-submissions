class Solution:
    def isPalindrome(self, s: str) -> bool:
        f=''.join([char for char in s if char.isalnum()])
        g=f.lower()
        r=''.join(reversed(g))
        return g==r
        

        