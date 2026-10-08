class Solution:
    def isPalindrome(self, s: str) -> bool:
        f=''.join([char for char in s if char.isalnum()])
        d=f.lower()
        g=''.join(reversed(d))
        return d==g
        